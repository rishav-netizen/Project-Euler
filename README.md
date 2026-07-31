<div align="center">

# 🧮 Project Euler Solutions

### Mathematical Problems · Algorithms · Python

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Project Euler](https://img.shields.io/badge/Project-Euler-6B4F2A?style=for-the-badge)
![Beautiful Soup](https://img.shields.io/badge/Beautiful_Soup-Web_Scraping-4B8BBE?style=for-the-badge)
![Requests](https://img.shields.io/badge/Requests-HTTP-2C5BB4?style=for-the-badge&logo=python&logoColor=white)
![Rich](https://img.shields.io/badge/Rich-Terminal_UI-8A2BE2?style=for-the-badge)
![LaTeX](https://img.shields.io/badge/LaTeX-008080?style=for-the-badge&logo=latex&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)
![VS Code](https://img.shields.io/badge/VS_Code-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white)
![macOS](https://img.shields.io/badge/macOS-000000?style=for-the-badge&logo=apple&logoColor=white)

*A collection of my solutions to Project Euler problems while practicing mathematics, algorithms, problem solving, and Python.*

<br>

**Solve · Scrape · Optimize · Repeat**

</div>

---

## 📖 About This Repository

This repository contains my solutions to **Project Euler** problems, along with a small **command-line web scraper** for quickly fetching and displaying problem statements. Each problem is kept in its own directory and, in general, contains a `main.py` implementation.

The goal of this repository is not only to reach the correct answer, but also to improve my understanding of **algorithmic thinking, mathematical reasoning, optimization, and Python programming**.

> Solutions are written as part of my learning process, so implementations may evolve as I discover cleaner or more efficient approaches.

---

## 🗂️ Repository Structure

```text
projectEuler/
├── problem0/
├── problem1/
├── problem2/
├── ...
├── problem67/
├── problem92/
├── scraper.py
├── folders.py
└── README.md
```

Most problem directories follow this structure:

```text
problemN/
└── main.py
```

---

## 🕸️ Project Euler Problem Scraper

This repository also includes `scraper.py`, a small command-line web scraper that fetches a Project Euler problem directly from the website and prints a clean, readable version in the terminal.

### 🔧 Scraper Tech Stack

| Library | Purpose |
| :--- | :--- |
| `requests` | Sends the HTTP request to Project Euler |
| `beautifulsoup4` | Parses the returned HTML and extracts the problem content |
| `pylatexenc` | Converts LaTeX expressions into readable terminal text |
| `rich` | Adds styled and colored terminal output |

### Usage

Pass the Project Euler problem number as a command-line argument:

```bash
python3 scraper.py 10
```

The script fetches `https://projecteuler.net/problem=10` and displays the problem number, title, and cleaned problem statement directly in the terminal.

If no problem number is supplied, the script prints the expected usage format. It also handles request failures and exits with an error message if the problem page cannot be fetched.

### 📦 Installation & Setup

Clone the repository and move into it:

```bash
git clone https://github.com/rishav-netizen/projectEuler.git
cd projectEuler
```

#### Option 1 — Install directly

Install all libraries required by the scraper:

```bash
python3 -m pip install requests beautifulsoup4 pylatexenc rich
```

#### Option 2 — Use a virtual environment

Using a virtual environment keeps the scraper dependencies isolated from the rest of your Python installation:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install requests beautifulsoup4 pylatexenc rich
```

When you are finished, leave the virtual environment with:

```bash
deactivate
```

### ✅ Verify the Installation

You can quickly check that all required libraries are available with:

```bash
python3 -c "import requests, bs4, pylatexenc, rich; print('All scraper dependencies installed successfully!')"
```

Then try the scraper:

```bash
python3 scraper.py 10
```
---

## 📁 Automatic Problem Folder Generator

The repository also includes `folders.py`, a small automation utility I use to generate the directory structure for new Project Euler problems instead of manually creating every folder and file.

It uses Python's built-in [`pathlib`](https://docs.python.org/3/library/pathlib.html) module, so **no additional library installation is required**.

### ⚙️ How It Works

The script defines the first and last problem numbers to generate:

```python
baseProblem = 92
finalProblem = 92
```

It then loops through that range and uses `Path` to create a directory for every problem:

```python
folder = Path(f"problem{i}")
folder.mkdir(exist_ok=True)
```

Inside each generated directory, the script automatically creates two starter files:

```python
(folder / "main.py").touch(exist_ok=True)
(folder / "output.txt").touch(exist_ok=True)
```

This means generating a problem produces a structure like:

```text
problem92/
├── main.py
└── output.txt
```

### 🚀 Generate Multiple Problems at Once

The useful part is that `baseProblem` and `finalProblem` can represent an entire range. For example:

```python
baseProblem = 93
finalProblem = 100
```

Running the script would automatically prepare:

```text
problem93/
problem94/
problem95/
...
problem100/
```

with a `main.py` and `output.txt` already created inside every directory.

Run the generator from the repository root with:

```bash
python3 folders.py
```

### 🛡️ Safe to Run Again

Both `mkdir()` and `touch()` use `exist_ok=True`. This allows the generator to be run again without failing just because a generated folder or starter file already exists.

> 💡 **Why I made it:** As the number of solved problems grows, this removes repetitive setup work and lets me create the boilerplate for an entire batch of Project Euler problems with one command.

---

## 🛠️ Tools & Technologies

<div align="center">

| Category | Technologies |
| :--- | :--- |
| **Language** | Python 3 |
| **Problem Solving** | Project Euler · Algorithms · Mathematics |
| **Web Scraping** | Requests · Beautiful Soup |
| **Text Processing** | pylatexenc · LaTeX |
| **Terminal Output** | Rich |
| **Version Control** | Git · GitHub |
| **Automation** | pathlib · Folder/File Generation |
| **Development** | VS Code · macOS Terminal |

</div>

---

## 💻 Quick Start

```bash
# Clone the repository
git clone https://github.com/rishav-netizen/projectEuler.git

# Enter the project
cd projectEuler

# Create an isolated Python environment
python3 -m venv .venv
source .venv/bin/activate

# Install scraper dependencies
python3 -m pip install requests beautifulsoup4 pylatexenc rich

# Generate starter problem directories/files when needed
python3 folders.py

# Fetch a Project Euler problem
python3 scraper.py 10

# Run its solution
python3 problem10/main.py
```

---


---

## 🧩 Solutions

<details open>
<summary><b>📋 View Project Euler Solutions</b></summary>
<br>

| Problem | Problem Link | Solution | Status |
| :---: | :---: | :---: | :---: |
| **0** | [View Problem](https://projecteuler.net/problem=0) | [View Code](./problem0/main.py) | ✅ Solved |
| **1** | [View Problem](https://projecteuler.net/problem=1) | [View Code](./problem1/main.py) | ✅ Solved |
| **2** | [View Problem](https://projecteuler.net/problem=2) | [View Code](./problem2/main.py) | ✅ Solved |
| **3** | [View Problem](https://projecteuler.net/problem=3) | [View Code](./problem3/main.py) | ✅ Solved |
| **4** | [View Problem](https://projecteuler.net/problem=4) | [View Code](./problem4/main.py) | ✅ Solved |
| **5** | [View Problem](https://projecteuler.net/problem=5) | [View Code](./problem5/main.py) | ✅ Solved |
| **6** | [View Problem](https://projecteuler.net/problem=6) | [View Code](./problem6/main.py) | ✅ Solved |
| **7** | [View Problem](https://projecteuler.net/problem=7) | [View Code](./problem7/main.py) | ✅ Solved |
| **8** | [View Problem](https://projecteuler.net/problem=8) | [View Code](./problem8/main.py) | ✅ Solved |
| **9** | [View Problem](https://projecteuler.net/problem=9) | [View Code](./problem9/main.py) | ✅ Solved |
| **10** | [View Problem](https://projecteuler.net/problem=10) | [View Code](./problem10/main.py) | ✅ Solved |
| **11** | [View Problem](https://projecteuler.net/problem=11) | [View Code](./problem11/main.py) | ✅ Solved |
| **12** | [View Problem](https://projecteuler.net/problem=12) | [View Code](./problem12/main.py) | ✅ Solved |
| **13** | [View Problem](https://projecteuler.net/problem=13) | [View Code](./problem13/main.py) | ✅ Solved |
| **14** | [View Problem](https://projecteuler.net/problem=14) | [View Code](./problem14/main.py) | ✅ Solved |
| **15** | [View Problem](https://projecteuler.net/problem=15) | [View Code](./problem15/main.py) | ✅ Solved |
| **16** | [View Problem](https://projecteuler.net/problem=16) | [View Code](./problem16/main.py) | ✅ Solved |
| **17** | [View Problem](https://projecteuler.net/problem=17) | [View Code](./problem17/main.py) | ✅ Solved |
| **18** | [View Problem](https://projecteuler.net/problem=18) | [View Code](./problem18/main.py) | ✅ Solved |
| **19** | [View Problem](https://projecteuler.net/problem=19) | [View Code](./problem19/main.py) | ✅ Solved |
| **20** | [View Problem](https://projecteuler.net/problem=20) | [View Code](./problem20/main.py) | ✅ Solved |
| **21** | [View Problem](https://projecteuler.net/problem=21) | [View Code](./problem21/main.py) | ✅ Solved |
| **22** | [View Problem](https://projecteuler.net/problem=22) | [View Code](./problem22/main.py) | ✅ Solved |
| **23** | [View Problem](https://projecteuler.net/problem=23) | [View Code](./problem23/main.py) | ✅ Solved |
| **24** | [View Problem](https://projecteuler.net/problem=24) | [View Code](./problem24/main.py) | ✅ Solved |
| **25** | [View Problem](https://projecteuler.net/problem=25) | [View Code](./problem25/main.py) | ✅ Solved |
| **26** | [View Problem](https://projecteuler.net/problem=26) | [View Code](./problem26/main.py) | ✅ Solved |
| **27** | [View Problem](https://projecteuler.net/problem=27) | [View Code](./problem27/main.py) | ✅ Solved |
| **28** | [View Problem](https://projecteuler.net/problem=28) | [View Code](./problem28/main.py) | ✅ Solved |
| **29** | [View Problem](https://projecteuler.net/problem=29) | [View Code](./problem29/main.py) | ✅ Solved |
| **30** | [View Problem](https://projecteuler.net/problem=30) | [View Code](./problem30/main.py) | ✅ Solved |
| **31** | [View Problem](https://projecteuler.net/problem=31) | [View Code](./problem31_*/main.py) | ✅ Solved |
| **32** | [View Problem](https://projecteuler.net/problem=32) | [View Code](./problem32/main.py) | ✅ Solved |
| **33** | [View Problem](https://projecteuler.net/problem=33) | [View Code](./problem33/main.py) | ✅ Solved |
| **34** | [View Problem](https://projecteuler.net/problem=34) | [View Code](./problem34/main.py) | ✅ Solved |
| **35** | [View Problem](https://projecteuler.net/problem=35) | [View Code](./problem35_*/main.py) | ✅ Solved |
| **36** | [View Problem](https://projecteuler.net/problem=36) | [View Code](./problem36_*/main.py) | ✅ Solved |
| **37** | [View Problem](https://projecteuler.net/problem=37) | [View Code](./problem37/main.py) | ✅ Solved |
| **38** | [View Problem](https://projecteuler.net/problem=38) | [View Code](./problem38/main.py) | ✅ Solved |
| **39** | [View Problem](https://projecteuler.net/problem=39) | [View Code](./problem39/main.py) | ✅ Solved |
| **40** | [View Problem](https://projecteuler.net/problem=40) | [View Code](./problem40/main.py) | ✅ Solved |
| **41** | [View Problem](https://projecteuler.net/problem=41) | [View Code](./problem41/main.py) | ✅ Solved |
| **42** | [View Problem](https://projecteuler.net/problem=42) | [View Code](./problem42/main.py) | ✅ Solved |
| **43** | [View Problem](https://projecteuler.net/problem=43) | [View Code](./problem43/main.py) | ✅ Solved |
| **44** | [View Problem](https://projecteuler.net/problem=44) | [View Code](./problem44/main.py) | ✅ Solved |
| **45** | [View Problem](https://projecteuler.net/problem=45) | [View Code](./problem45/main.py) | ✅ Solved |
| **46** | [View Problem](https://projecteuler.net/problem=46) | [View Code](./problem46/main.py) | ✅ Solved |
| **47** | [View Problem](https://projecteuler.net/problem=47) | [View Code](./problem47_*/main.py) | ✅ Solved |
| **48」 | [View Problem](https://projecteuler.net/problem=48) | [View Code](./problem48_*/main.py) | ✅ Solved |
| **49** | [View Problem](https://projecteuler.net/problem=49) | [View Code](./problem49_*/main.py) | ✅ Solved |
| **50** | [View Problem](https://projecteuler.net/problem=50) | [View Code](./problem50_*/main.py) | ✅ Solved |
| **51** | [View Problem](https://projecteuler.net/problem=51) | [View Code](./problem51_*/main.py) | ✅ Solved |
| **52** | [View Problem](https://projecteuler.net/problem=52) | [View Code](./problem52/main.py) | ✅ Solved |
| **53** | [View Problem](https://projecteuler.net/problem=53) | [View Code](./problem53/main.py) | ✅ Solved |
| **54** | [View Problem](https://projecteuler.net/problem=54) | [View Code](./problem54/main.py) | ✅ Solved |
| **55** | [View Problem](https://projecteuler.net/problem=55) | [View Code](./problem55/main.py) | ✅ Solved |
| **56** | [View Problem](https://projecteuler.net/problem=56) | [View Code](./problem56/main.py) | ✅ Solved |
| **57** | [View Problem](https://projecteuler.net/problem=57) | [View Code](./problem57/main.py) | ✅ Solved |
| **58** | [View Problem](https://projecteuler.net/problem=58) | [View Code](./problem58/main.py) | ✅ Solved |
| **59** | [View Problem](https://projecteuler.net/problem=59) | [View Code](./problem59/main.py) | ✅ Solved |
| **60** | [View Problem](https://projecteuler.net/problem=60) | [View Code](./problem60/main.py) | ✅ Solved |
| **61** | [View Problem](https://projecteuler.net/problem=61) | [View Code](./problem61!/main.py) | ✅ Solved |
| **62** | [View Problem](https://projecteuler.net/problem=62) | [View Code](./problem62/main.py) | ✅ Solved |
| **63** | [View Problem](https://projecteuler.net/problem=63) | [View Code](./problem63/main.py) | ✅ Solved |
| **64** | [View Problem](https://projecteuler.net/problem=64) | [View Code](./problem64/main.py) | ✅ Solved |
| **65** | [View Problem](https://projecteuler.net/problem=65) | [View Code](./problem65/main.py) | ✅ Solved |
| **67** | [View Problem](https://projecteuler.net/problem=67) | [View Code](./problem67_/main.py) | ✅ Solved |
| **92** | [View Problem](https://projecteuler.net/problem=92) | [View Code](./problem92/main.py) | ✅ Solved |
| **97** | [View Problem](https://projecteuler.net/problem=97) | [View Code](./problem97/main.py) | ✅ Solved |

</details>

> The table reflects the problem directories currently present in this repository.

---

## 🧠 Concepts Practiced

`Algorithms` · `Number Theory` · `Prime Numbers` · `Combinatorics` · `Dynamic Programming` · `Sequences` · `Recursion` · `Searching` · `Optimization` · `Python` · `Web Scraping` · `HTTP Requests` · `HTML Parsing` · `LaTeX Processing` · `CLI Tools` · `File System Automation` · `pathlib`

## 🌟 Repository Highlights

- 🧮 Dozens of solved Project Euler problems
- 🕸️ Built-in CLI problem scraper
- 📁 Automatic problem directory and starter-file generator
- 🎨 Rich terminal formatting
- ∑ LaTeX-to-text conversion for mathematical expressions
- ⚡ Focus on efficient mathematical and algorithmic solutions
- 📂 One-directory-per-problem organization
- 🔄 Continuously expanding as more problems are solved

---


---

## ⚙️ Running a Solution

Move into any problem directory and run its Python file:

```bash
cd problem10
python3 main.py
```

Or run it directly from the repository root:

```bash
python3 problem10/main.py
```

---

## 📝 Approach

For each problem, I generally try to:

- Understand the mathematical idea behind the problem
- Start with a straightforward solution
- Identify unnecessary computation or repeated work
- Improve the algorithm when a more efficient approach is possible
- Keep the Python implementation readable and concise

---

## 🚀 Progress

**Problems currently represented in this repository:** `0–65`, `67`, and `92`

This repository is a continuous learning project and will grow as I solve more Project Euler problems.

---

## ⚠️ Project Euler Spoiler Notice

This repository contains working solutions to Project Euler problems. If you are currently solving these problems yourself, consider attempting them before looking at the source code.

---

<div align="center">

### 🧠 Mathematics × Algorithms × Code

**Project Euler · Python · Web Scraping · Problem Solving**

*Solving one problem at a time. Optimizing one solution at a time.*

⭐ **If you find this repository interesting, consider giving it a star!**

</div>