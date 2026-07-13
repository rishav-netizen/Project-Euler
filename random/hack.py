#!/usr/bin/env python3
"""
Passive website source scanner.

Use this only on websites you own or have explicit permission to assess. The
script fetches public HTML/source files, like what you can see through browser
Inspect/View Source, and reports risky patterns. It does not exploit anything,
submit forms, brute force, or bypass authentication.

Examples:
    python3 hack.py https://example.com
    python3 hack.py https://example.com --max-assets 25 --json
"""

from __future__ import annotations

import argparse
import json
import re
import ssl
import sys
from dataclasses import asdict, dataclass
from html.parser import HTMLParser
from typing import Iterable
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin, urlparse
from urllib.request import Request, urlopen


USER_AGENT = "PassiveSourceScanner/1.0"
DEFAULT_TIMEOUT = 10


@dataclass(frozen=True)
class Finding:
    severity: str
    url: str
    line: int
    rule: str
    evidence: str
    advice: str


@dataclass(frozen=True)
class FetchedPage:
    url: str
    status: int
    content_type: str
    text: str


class SourceLinkParser(HTMLParser):
    def __init__(self, base_url: str) -> None:
        super().__init__()
        self.base_url = base_url
        self.scripts: set[str] = set()
        self.stylesheets: set[str] = set()
        self.forms: list[tuple[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_map = {name.lower(): value for name, value in attrs}

        if tag == "script" and attrs_map.get("src"):
            self.scripts.add(urljoin(self.base_url, attrs_map["src"] or ""))

        if tag == "link" and attrs_map.get("rel") and attrs_map.get("href"):
            rel = (attrs_map["rel"] or "").lower()
            if "stylesheet" in rel:
                self.stylesheets.add(urljoin(self.base_url, attrs_map["href"] or ""))

        if tag == "form":
            action = urljoin(self.base_url, attrs_map.get("action") or self.base_url)
            method = (attrs_map.get("method") or "get").upper()
            self.forms.append((method, action))


RULES: tuple[tuple[str, str, re.Pattern[str], str], ...] = (
    (
        "HIGH",
        "Possible AWS access key in public source",
        re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
        "Remove the key, rotate it immediately, and move secrets server-side.",
    ),
    (
        "HIGH",
        "Possible private key block in public source",
        re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----"),
        "Remove the private key, rotate it, and check deployment artifacts.",
    ),
    (
        "HIGH",
        "Possible GitHub token in public source",
        re.compile(r"\bgh[pousr]_[A-Za-z0-9_]{30,}\b"),
        "Revoke the token and avoid embedding credentials in client code.",
    ),
    (
        "MEDIUM",
        "Possible generic secret assignment",
        re.compile(
            r"""(?ix)
            \b(?:api[_-]?key|secret|token|password|passwd|pwd)\b
            \s*[:=]\s*
            ['"][^'"]{8,}['"]
            """
        ),
        "Confirm this is not a real credential. Public client code cannot keep secrets.",
    ),
    (
        "MEDIUM",
        "DOM injection sink",
        re.compile(r"\b(?:innerHTML|outerHTML|insertAdjacentHTML|document\.write)\b"),
        "Ensure user-controlled data is sanitized before reaching this DOM sink.",
    ),
    (
        "MEDIUM",
        "Dynamic JavaScript execution",
        re.compile(r"\b(?:eval|new\s+Function|setTimeout|setInterval)\s*\("),
        "Avoid dynamic code execution or strictly validate the input source.",
    ),
    (
        "LOW",
        "Debug logging left in client source",
        re.compile(r"\bconsole\.(?:log|debug|trace)\s*\("),
        "Remove noisy debug output from production bundles.",
    ),
    (
        "LOW",
        "Source map reference",
        re.compile(r"sourceMappingURL=.*\.map\b"),
        "Verify source maps do not expose private source, comments, or internal paths.",
    ),
    (
        "LOW",
        "TODO/FIXME marker in public source",
        re.compile(r"\b(?:TODO|FIXME|HACK|XXX)\b"),
        "Review whether this exposes implementation details or unfinished security work.",
    ),
)


def is_http_url(url: str) -> bool:
    return urlparse(url).scheme in {"http", "https"}


def same_origin(first: str, second: str) -> bool:
    first_parts = urlparse(first)
    second_parts = urlparse(second)
    return (
        first_parts.scheme,
        first_parts.hostname,
        first_parts.port,
    ) == (
        second_parts.scheme,
        second_parts.hostname,
        second_parts.port,
    )


def fetch(url: str, timeout: int, insecure_tls: bool) -> FetchedPage:
    context = ssl._create_unverified_context() if insecure_tls else None
    request = Request(url, headers={"User-Agent": USER_AGENT})

    with urlopen(request, timeout=timeout, context=context) as response:
        content_type = response.headers.get("Content-Type", "")
        charset = response.headers.get_content_charset() or "utf-8"
        raw = response.read()
        text = raw.decode(charset, errors="replace")
        status = getattr(response, "status", 200)
        return FetchedPage(url=url, status=status, content_type=content_type, text=text)


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def redacted(value: str, max_len: int = 100) -> str:
    compact = " ".join(value.strip().split())
    if len(compact) > max_len:
        return compact[: max_len - 3] + "..."
    return compact


def scan_text(page: FetchedPage) -> list[Finding]:
    findings: list[Finding] = []

    if page.url.startswith("http://"):
        findings.append(
            Finding(
                severity="MEDIUM",
                url=page.url,
                line=1,
                rule="Page loaded over HTTP",
                evidence="http://",
                advice="Serve the site over HTTPS and redirect HTTP to HTTPS.",
            )
        )

    for severity, rule, pattern, advice in RULES:
        for match in pattern.finditer(page.text):
            findings.append(
                Finding(
                    severity=severity,
                    url=page.url,
                    line=line_number(page.text, match.start()),
                    rule=rule,
                    evidence=redacted(match.group(0)),
                    advice=advice,
                )
            )

    if "text/html" in page.content_type or "<html" in page.text[:1000].lower():
        parser = SourceLinkParser(page.url)
        parser.feed(page.text)
        for method, action in parser.forms:
            if method == "POST" and action.startswith("http://"):
                findings.append(
                    Finding(
                        severity="HIGH",
                        url=page.url,
                        line=1,
                        rule="Form posts over HTTP",
                        evidence=f"{method} {action}",
                        advice="Submit credentials or sensitive form data only over HTTPS.",
                    )
                )

    return findings


def discover_same_origin_assets(page: FetchedPage) -> list[str]:
    if "text/html" not in page.content_type and "<html" not in page.text[:1000].lower():
        return []

    parser = SourceLinkParser(page.url)
    parser.feed(page.text)
    assets = sorted(parser.scripts | parser.stylesheets)
    return [asset for asset in assets if is_http_url(asset) and same_origin(page.url, asset)]


def scan_url(
    start_url: str,
    max_assets: int,
    timeout: int,
    insecure_tls: bool,
) -> tuple[list[Finding], list[str]]:
    findings: list[Finding] = []
    errors: list[str] = []
    queued = [start_url]
    seen: set[str] = set()

    while queued and len(seen) <= max_assets:
        url = queued.pop(0)
        if url in seen:
            continue
        seen.add(url)

        try:
            page = fetch(url, timeout=timeout, insecure_tls=insecure_tls)
        except HTTPError as exc:
            errors.append(f"{url}: HTTP {exc.code}")
            continue
        except URLError as exc:
            errors.append(f"{url}: {exc.reason}")
            continue
        except TimeoutError:
            errors.append(f"{url}: timed out")
            continue
        except Exception as exc:  # noqa: BLE001 - CLI should report and keep scanning.
            errors.append(f"{url}: {exc}")
            continue

        findings.extend(scan_text(page))

        if len(seen) == 1:
            queued.extend(discover_same_origin_assets(page)[:max_assets])

    return findings, errors


def print_text_report(findings: Iterable[Finding], errors: Iterable[str]) -> None:
    severity_rank = {"HIGH": 0, "MEDIUM": 1, "LOW": 2}
    ordered = sorted(findings, key=lambda item: (severity_rank[item.severity], item.url, item.line))

    if not ordered:
        print("No risky source-code patterns found.")
    else:
        for finding in ordered:
            print(f"[{finding.severity}] {finding.rule}")
            print(f"  URL: {finding.url}:{finding.line}")
            print(f"  Evidence: {finding.evidence}")
            print(f"  Advice: {finding.advice}")
            print()

    error_list = list(errors)
    if error_list:
        print("Fetch errors:")
        for error in error_list:
            print(f"  - {error}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Passively scan public website source for risky client-side patterns."
    )
    parser.add_argument("urls", nargs="+", help="Authorized http(s) URLs to inspect")
    parser.add_argument("--max-assets", type=int, default=20, help="same-origin JS/CSS assets per page")
    parser.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT, help="request timeout in seconds")
    parser.add_argument("--json", action="store_true", help="print JSON instead of text")
    parser.add_argument("--insecure-tls", action="store_true", help="skip TLS certificate verification")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    all_findings: list[Finding] = []
    all_errors: list[str] = []

    for url in args.urls:
        if not is_http_url(url):
            all_errors.append(f"{url}: only http(s) URLs are supported")
            continue

        findings, errors = scan_url(
            start_url=url,
            max_assets=max(0, args.max_assets),
            timeout=max(1, args.timeout),
            insecure_tls=args.insecure_tls,
        )
        all_findings.extend(findings)
        all_errors.extend(errors)

    if args.json:
        print(
            json.dumps(
                {
                    "findings": [asdict(finding) for finding in all_findings],
                    "errors": all_errors,
                },
                indent=2,
            )
        )
    else:
        print_text_report(all_findings, all_errors)

    return 1 if all_findings else 0


if __name__ == "__main__":
    sys.exit(main())
