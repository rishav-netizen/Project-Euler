from bs4 import BeautifulSoup
import requests
from sys import argv
from pylatexenc.latex2text import LatexNodes2Text
from rich.console import Console

console = Console() 

argc = len(argv)
if argc != 2:
    console.print("[bold red]Usage: python3 scraper.py 'problem number'[/bold red]")
    exit(1)

n = argv[1] # problem number
url = f"https://projecteuler.net/problem={n}"
try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    console.print(f"[bold red]Request failed:[/bold red] {e}")
    exit(2)

# searchable html object
soup = BeautifulSoup(response.text, "html.parser")
problemName = soup.find('h2').text
problemNumber = soup.find('h3').text
problemStatementRaw = soup.find('div', "problem_content").text
problemStatementClean = LatexNodes2Text().latex_to_text(problemStatementRaw)

console.print(f"[bold blue]{problemNumber}[/bold blue]: [bold yellow]{problemName}[/bold yellow]")
console.print(f"[white]{problemStatementClean}[/white]")
