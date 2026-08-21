<div align="center">

# 🧮 Project Euler Solutions

### Mathematical Problems · Algorithms · Python

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Project Euler](https://img.shields.io/badge/Project-Euler-6B4F2A?style=for-the-badge&logo=projecteuler&logoColor=white)
![Problems Solved](https://img.shields.io/badge/Problems_Solved-81%2F85-success?style=for-the-badge)
![Beautiful Soup](https://img.shields.io/badge/Beautiful_Soup-Web_Scraping-4B8BBE?style=for-the-badge)
![Requests](https://img.shields.io/badge/Requests-HTTP-2C5BB4?style=for-the-badge&logo=python&logoColor=white)
![Rich](https://img.shields.io/badge/Rich-Terminal_UI-8A2BE2?style=for-the-badge)
![LaTeX](https://img.shields.io/badge/LaTeX-008080?style=for-the-badge&logo=latex&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)
![macOS](https://img.shields.io/badge/macOS-000000?style=for-the-badge&logo=apple&logoColor=white)

*A structured collection of solutions to Project Euler problems with dedicated documentation, algorithmic breakdowns, mathematical proofs, and automated tooling.*

<br>

**Solve · Scrape · Document · Optimize · Repeat**

</div>

---

## 📖 About This Repository

This repository contains my solutions to **Project Euler** problems, accompanied by in-depth **problem READMEs** documenting the mathematical insights, algorithms, and complexity analyses used.

It also includes:
- A **command-line problem scraper** (`scraper.py`) for fetching clean problem statements directly from Project Euler.
- An **automation generator** (`folders.py`) for batch-generating problem workspace directories.
- Individual **`output.txt`** result logs verifying answers for each problem.

---

## 🗂️ Repository Structure

```text
projectEuler/
├── problem0/
│   ├── main.py
│   ├── output.txt
│   └── README.md
├── problem1/
│   ├── main.py
│   ├── better.py
│   ├── output.txt
│   └── README.md
├── ...
├── scraper.py
├── folders.py
└── README.md
```

Each solved problem directory contains:
- `main.py`: Primary Python solution implementation (plus alternative/optimized scripts where applicable).
- `README.md`: Problem description, key learnings, mathematical theorems, code walkthrough, and complexity breakdown.
- `output.txt`: Captured output from running the solution.

---

## 🕸️ Project Euler Problem Scraper

The repository includes `scraper.py`, a small CLI tool that fetches any Project Euler problem statement directly from the website and displays it in styled terminal format.

### 🔧 Scraper Tech Stack

| Library | Purpose |
| :--- | :--- |
| `requests` | Sends HTTP requests to Project Euler |
| `beautifulsoup4` | Parses HTML and extracts problem content |
| `pylatexenc` | Converts embedded LaTeX expressions to clean terminal text |
| `rich` | Terminal colors and formatting |

### Usage

```bash
python3 scraper.py 10
```

---

## 📁 Problem Boilerplate Generator

`folders.py` automates directory creation and boilerplate setup for batches of problems using Python's built-in `pathlib` module:

```bash
python3 folders.py
```

---

## 🧩 Solutions & Learnings

<details open>
<summary><b>📋 View All Solutions & Documentation (85 Problems)</b></summary>
<br>

| Problem | Title | Problem Link | Solution | Learnings & Breakdown | Status |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **0** | Sum of Squares of Odd Numbers | Warmup | [View Code](./problem0/main.py) | [View README](./problem0/README.md) | ✅ Solved |
| **1** | Multiples of 3 or 5 | [Problem 1](https://projecteuler.net/problem=1) | [View Code](./problem1/better.py) | [View README](./problem1/README.md) | ✅ Solved |
| **2** | Even Fibonacci Numbers | [Problem 2](https://projecteuler.net/problem=2) | [View Code](./problem2/main.py) | [View README](./problem2/README.md) | ✅ Solved |
| **3** | Largest Prime Factor | [Problem 3](https://projecteuler.net/problem=3) | [View Code](./problem3/main.py) | [View README](./problem3/README.md) | ✅ Solved |
| **4** | Largest Palindrome Product | [Problem 4](https://projecteuler.net/problem=4) | [View Code](./problem4/main.py) | [View README](./problem4/README.md) | ✅ Solved |
| **5** | Smallest Multiple | [Problem 5](https://projecteuler.net/problem=5) | [View Code](./problem5/main.py) | [View README](./problem5/README.md) | ✅ Solved |
| **6** | Sum Square Difference | [Problem 6](https://projecteuler.net/problem=6) | [View Code](./problem6/main.py) | [View README](./problem6/README.md) | ✅ Solved |
| **7** | 10001st Prime | [Problem 7](https://projecteuler.net/problem=7) | [View Code](./problem7/main.py) | [View README](./problem7/README.md) | ✅ Solved |
| **8** | Largest Product in a Series | [Problem 8](https://projecteuler.net/problem=8) | [View Code](./problem8/main.py) | [View README](./problem8/README.md) | ✅ Solved |
| **9** | Special Pythagorean Triplet | [Problem 9](https://projecteuler.net/problem=9) | [View Code](./problem9/bruteForce.py) | [View README](./problem9/README.md) | ✅ Solved |
| **10** | Summation of Primes | [Problem 10](https://projecteuler.net/problem=10) | [View Code](./problem10/main.py) | [View README](./problem10/README.md) | ✅ Solved |
| **11** | Largest Product in a Grid | [Problem 11](https://projecteuler.net/problem=11) | [View Code](./problem11/correct.py) | [View README](./problem11/README.md) | ✅ Solved |
| **12** | Highly Divisible Triangular Number | [Problem 12](https://projecteuler.net/problem=12) | [View Code](./problem12/main.py) | [View README](./problem12/README.md) | ✅ Solved |
| **13** | Large Sum | [Problem 13](https://projecteuler.net/problem=13) | [View Code](./problem13_/main.py) | [View README](./problem13_/README.md) | ✅ Solved |
| **14** | Longest Collatz Sequence | [Problem 14](https://projecteuler.net/problem=14) | [View Code](./problem14/main.py) | [View README](./problem14/README.md) | ✅ Solved |
| **15** | Lattice Paths | [Problem 15](https://projecteuler.net/problem=15) | [View Code](./problem15_/main.py) | [View README](./problem15_/README.md) | ✅ Solved |
| **16** | Power Digit Sum | [Problem 16](https://projecteuler.net/problem=16) | [View Code](./problem16/main.py) | [View README](./problem16/README.md) | ✅ Solved |
| **17** | Number Letter Counts | [Problem 17](https://projecteuler.net/problem=17) | [View Code](./problem17_/main.py) | [View README](./problem17_/README.md) | ✅ Solved |
| **18** | Maximum Path Sum I | [Problem 18](https://projecteuler.net/problem=18) | [View Code](./problem18/main.py) | [View README](./problem18/README.md) | ✅ Solved |
| **19** | Counting Sundays | [Problem 19](https://projecteuler.net/problem=19) | [View Code](./problem19/main.py) | [View README](./problem19/README.md) | ✅ Solved |
| **20** | Factorial Digit Sum | [Problem 20](https://projecteuler.net/problem=20) | [View Code](./problem20/main.py) | [View README](./problem20/README.md) | ✅ Solved |
| **21** | Amicable Numbers | [Problem 21](https://projecteuler.net/problem=21) | [View Code](./problem21/main.py) | [View README](./problem21/README.md) | ✅ Solved |
| **22** | Names Scores | [Problem 22](https://projecteuler.net/problem=22) | [View Code](./problem22/main.py) | [View README](./problem22/README.md) | ✅ Solved |
| **23** | Non-Abundant Sums | [Problem 23](https://projecteuler.net/problem=23) | [View Code](./problem23/main.py) | [View README](./problem23/README.md) | ✅ Solved |
| **24** | Lexicographic Permutations | [Problem 24](https://projecteuler.net/problem=24) | [View Code](./problem24/main.py) | [View README](./problem24/README.md) | ✅ Solved |
| **25** | 1000-digit Fibonacci Number | [Problem 25](https://projecteuler.net/problem=25) | [View Code](./problem25/main.py) | [View README](./problem25/README.md) | ✅ Solved |
| **26** | Reciprocal Cycles | [Problem 26](https://projecteuler.net/problem=26) | [View Code](./problem26/main.py) | [View README](./problem26/README.md) | ✅ Solved |
| **27** | Quadratic Primes | [Problem 27](https://projecteuler.net/problem=27) | [View Code](./problem27_/main.py) | [View README](./problem27_/README.md) | ✅ Solved |
| **28** | Number Spiral Diagonals | [Problem 28](https://projecteuler.net/problem=28) | [View Code](./problem28/main.py) | [View README](./problem28/README.md) | ✅ Solved |
| **29** | Distinct Powers | [Problem 29](https://projecteuler.net/problem=29) | [View Code](./problem29/main.py) | [View README](./problem29/README.md) | ✅ Solved |
| **30** | Digit Fifth Powers | [Problem 30](https://projecteuler.net/problem=30) | [View Code](./problem30_/main.py) | [View README](./problem30_/README.md) | ✅ Solved |
| **31** | Coin Sums | [Problem 31](https://projecteuler.net/problem=31) | [View Code](./problem31_*/main.py) | [View README](./problem31_*/README.md) | ✅ Solved |
| **32** | Pandigital Products | [Problem 32](https://projecteuler.net/problem=32) | [View Code](./problem32/main.py) | [View README](./problem32/README.md) | ✅ Solved |
| **33** | Digit Cancelling Fractions | [Problem 33](https://projecteuler.net/problem=33) | [View Code](./problem33/main.py) | [View README](./problem33/README.md) | ✅ Solved |
| **34** | Digit Factorials | [Problem 34](https://projecteuler.net/problem=34) | [View Code](./problem34/main.py) | [View README](./problem34/README.md) | ✅ Solved |
| **35** | Circular Primes | [Problem 35](https://projecteuler.net/problem=35) | [View Code](./problem35_/main.py) | [View README](./problem35_/README.md) | ✅ Solved |
| **36** | Double-Base Palindromes | [Problem 36](https://projecteuler.net/problem=36) | [View Code](./problem36_/main.py) | [View README](./problem36_/README.md) | ✅ Solved |
| **37** | Truncatable Primes | [Problem 37](https://projecteuler.net/problem=37) | [View Code](./problem37/main.py) | [View README](./problem37/README.md) | ✅ Solved |
| **38** | Pandigital Multiples | [Problem 38](https://projecteuler.net/problem=38) | [View Code](./problem38/main.py) | [View README](./problem38/README.md) | ✅ Solved |
| **39** | Integer Right Triangles | [Problem 39](https://projecteuler.net/problem=39) | [View Code](./problem39/main.py) | [View README](./problem39/README.md) | ✅ Solved |
| **40** | Champernowne's Constant | [Problem 40](https://projecteuler.net/problem=40) | [View Code](./problem40/main.py) | [View README](./problem40/README.md) | ✅ Solved |
| **41** | Pandigital Prime | [Problem 41](https://projecteuler.net/problem=41) | [View Code](./problem41/main.py) | [View README](./problem41/README.md) | ✅ Solved |
| **42** | Coded Triangle Numbers | [Problem 42](https://projecteuler.net/problem=42) | [View Code](./problem42/main.py) | [View README](./problem42/README.md) | ✅ Solved |
| **43** | Sub-string Divisibility | [Problem 43](https://projecteuler.net/problem=43) | [View Code](./problem43/main.py) | [View README](./problem43/README.md) | ✅ Solved |
| **44** | Pentagon Numbers | [Problem 44](https://projecteuler.net/problem=44) | [View Code](./problem44/main.py) | [View README](./problem44/README.md) | ✅ Solved |
| **45** | Triangular, Pentagonal, and Hexagonal | [Problem 45](https://projecteuler.net/problem=45) | [View Code](./problem45/main.py) | [View README](./problem45/README.md) | ✅ Solved |
| **46** | Goldbach's Other Conjecture | [Problem 46](https://projecteuler.net/problem=46) | [View Code](./problem46_/main.py) | [View README](./problem46_/README.md) | ✅ Solved |
| **47** | Distinct Primes Factors | [Problem 47](https://projecteuler.net/problem=47) | [View Code](./problem47_/codex_optimized.py) | [View README](./problem47_/README.md) | ✅ Solved |
| **48** | Self Powers | [Problem 48](https://projecteuler.net/problem=48) | [View Code](./problem48/main.py) | [View README](./problem48/README.md) | ✅ Solved |
| **49** | Prime Permutations | [Problem 49](https://projecteuler.net/problem=49) | [View Code](./problem49_/better.py) | [View README](./problem49_/README.md) | ✅ Solved |
| **50** | Consecutive Prime Sum | [Problem 50](https://projecteuler.net/problem=50) | [View Code](./problem50_?/fun.py) | [View README](./problem50_?/README.md) | ✅ Solved |
| **51** | Prime Digit Replacements | [Problem 51](https://projecteuler.net/problem=51) | [View Code](./problem51_/main.py) | [View README](./problem51_/README.md) | ✅ Solved |
| **52** | Permuted Multiples | [Problem 52](https://projecteuler.net/problem=52) | [View Code](./problem52/main.py) | [View README](./problem52/README.md) | ✅ Solved |
| **53** | Combinatoric Selections | [Problem 53](https://projecteuler.net/problem=53) | [View Code](./problem53/main.py) | [View README](./problem53/README.md) | ✅ Solved |
| **54** | Poker Hands | [Problem 54](https://projecteuler.net/problem=54) | [View Code](./problem54/better.py) | [View README](./problem54/README.md) | ✅ Solved |
| **55** | Lychrel Numbers | [Problem 55](https://projecteuler.net/problem=55) | [View Code](./problem55/main.py) | [View README](./problem55/README.md) | ✅ Solved |
| **56** | Powerful Digit Sum | [Problem 56](https://projecteuler.net/problem=56) | [View Code](./problem56/main.py) | [View README](./problem56/README.md) | ✅ Solved |
| **57** | Square Root Convergents | [Problem 57](https://projecteuler.net/problem=57) | [View Code](./problem57/main.py) | [View README](./problem57/README.md) | ✅ Solved |
| **58** | Spiral Primes | [Problem 58](https://projecteuler.net/problem=58) | [View Code](./problem58/main.py) | [View README](./problem58/README.md) | ✅ Solved |
| **59** | XOR Decryption | [Problem 59](https://projecteuler.net/problem=59) | [View Code](./problem59/main.py) | [View README](./problem59/README.md) | ✅ Solved |
| **60** | Prime Pair Sets | [Problem 60](https://projecteuler.net/problem=60) | [View Code](./problem60/main.py) | [View README](./problem60/README.md) | ✅ Solved |
| **61** | Cyclical Figurate Numbers | [Problem 61](https://projecteuler.net/problem=61) | [View Code](./problem61!/main.py) | — | ❌ Unsolved |
| **62** | Cubic Permutations | [Problem 62](https://projecteuler.net/problem=62) | [View Code](./problem62/main.py) | [View README](./problem62/README.md) | ✅ Solved |
| **63** | Powerful Digit Counts | [Problem 63](https://projecteuler.net/problem=63) | [View Code](./problem63/main.py) | [View README](./problem63/README.md) | ✅ Solved |
| **64** | Odd Period Square Roots | [Problem 64](https://projecteuler.net/problem=64) | [View Code](./problem64/main.py) | [View README](./problem64/README.md) | ✅ Solved |
| **65** | Convergents of e | [Problem 65](https://projecteuler.net/problem=65) | [View Code](./problem65/main.py) | — | ❌ Unsolved |
| **67** | Maximum Path Sum II | [Problem 67](https://projecteuler.net/problem=67) | [View Code](./problem67_/main.py) | [View README](./problem67_/README.md) | ✅ Solved |
| **69** | Totient Maximum | [Problem 69](https://projecteuler.net/problem=69) | [View Code](./problem69_/main.py) | [View README](./problem69_/README.md) | ✅ Solved |
| **72** | Counting Fractions | [Problem 72](https://projecteuler.net/problem=72) | [View Code](./problem72/main.py) | [View README](./problem72/README.md) | ✅ Solved |
| **74** | Digit Factorial Chains | [Problem 74](https://projecteuler.net/problem=74) | [View Code](./problem74/main.py) | [View README](./problem74/README.md) | ✅ Solved |
| **76** | Counting Summations | [Problem 76](https://projecteuler.net/problem=76) | [View Code](./problem76/main.py) | [View README](./problem76/README.md) | ✅ Solved |
| **77** | Prime Summations | [Problem 77](https://projecteuler.net/problem=77) | [View Code](./problem77/main.py) | [View README](./problem77/README.md) | ✅ Solved |
| **78** | Coin Partitions | [Problem 78](https://projecteuler.net/problem=78) | [View Code](./problem78/main.py) | [View README](./problem78/README.md) | ✅ Solved |
| **79** | Passcode Derivation | [Problem 79](https://projecteuler.net/problem=79) | [View Code](./problem79_/main.py) | [View README](./problem79_/README.md) | ✅ Solved |
| **80** | Square Root Digital Expansion | [Problem 80](https://projecteuler.net/problem=80) | [View Code](./problem80/better.py) | [View README](./problem80/README.md) | ✅ Solved |
| **81** | Path Sum: Two Ways | [Problem 81](https://projecteuler.net/problem=81) | [View Code](./problem81/main.py) | [View README](./problem81/README.md) | ✅ Solved |
| **82** | Path Sum: Three Ways | [Problem 82](https://projecteuler.net/problem=82) | [View Code](./problem82!/main.py) | — | ❌ Unsolved |
| **85** | Counting Rectangles | [Problem 85](https://projecteuler.net/problem=85) | [View Code](./problem85/main.py) | [View README](./problem85/README.md) | ✅ Solved |
| **87** | Prime Power Triples | [Problem 87](https://projecteuler.net/problem=87) | [View Code](./problem87/main.py) | [View README](./problem87/README.md) | ✅ Solved |
| **89** | Roman Numerals | [Problem 89](https://projecteuler.net/problem=89) | [View Code](./problem89!/main.py) | — | ❌ Unsolved |
| **92** | Square Digit Chains | [Problem 92](https://projecteuler.net/problem=92) | [View Code](./problem92/main.py) | [View README](./problem92/README.md) | ✅ Solved |
| **95** | Amicable Chains | [Problem 95](https://projecteuler.net/problem=95) | [View Code](./problem95/main.py) | [View README](./problem95/README.md) | ✅ Solved |
| **97** | Large Non-Mersenne Prime | [Problem 97](https://projecteuler.net/problem=97) | [View Code](./problem97/main.py) | [View README](./problem97/README.md) | ✅ Solved |
| **99** | Largest Exponential | [Problem 99](https://projecteuler.net/problem=99) | [View Code](./problem99/main.py) | [View README](./problem99/README.md) | ✅ Solved |
| **104** | Pandigital Fibonacci Ends | [Problem 104](https://projecteuler.net/problem=104) | [View Code](./problem104/main.py) | [View README](./problem104/README.md) | ✅ Solved |

</details>

---

## 🧠 Concepts & Techniques Practiced

`Number Theory` · `Sieve of Eratosthenes` · `Euler's Totient Function` · `Modular Arithmetic` · `Dynamic Programming` · `Integer Partitions` · `Combinatorics` · `Permutations & Factoradics` · `Binet's Formula` · `Continued Fractions` · `Pythagorean Triples` · `Topological Sorting` · `Graph Cliques` · `Functional Graph Cycles` · `BigInt Precision` · `Sliding Window` · `Web Scraping`

---

## ⚙️ Running a Solution

Run any solution directly from the repository root:

```bash
python3 problem10/main.py
```

Or navigate into the problem directory:

```bash
cd problem10
python3 main.py
```

---

## 🚀 Progress Summary

- **Total Solved Problems:** `81`
- **Solved Problem Numbers:** `0–60`, `62–64`, `67`, `69`, `72`, `74`, `76–81`, `85`, `87`, `92`, `95`, `97`, `99`, and `104`.
- **In-Progress / Unsolved:** `61`, `65`, `82`, `89`.

---

## ⚠️ Project Euler Spoiler Notice

This repository contains working solutions and mathematical explanations. If you are solving these problems yourself, consider attempting them independently before viewing the source code and documentation.

---

<div align="center">

### 🧠 Mathematics × Algorithms × Code

**Project Euler · Python · Web Scraping · Problem Solving**

*Solving one problem at a time. Optimizing one solution at a time.*

⭐ **If you find this repository helpful, consider giving it a star!**

</div>
