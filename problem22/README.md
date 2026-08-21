# 🧮 Project Euler Problem 22: Names Scores

<div align="center">

![Project Euler](https://img.shields.io/badge/Project-Euler-6B4F2A?style=for-the-badge&logo=projecteuler&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Solved-success?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-File%20Parsing%20%C2%B7%20Sorting%20&%20Scoring-blue?style=for-the-badge)

</div>

---

## 📜 Problem Statement

What is the total of all the name scores in the 5000+ names file?

🔗 **Project Euler Link:** [Problem 22](https://projecteuler.net/problem=22)

---

## 💡 Key Learnings & Mathematical Insights

- **Lexicographical Sorting**: Clean quotation marks, split by commas, and sort alphabetically.
- **Score Metric**: Position index (1-based) $\times$ sum of alphabetical letter positions (`ord(c) - 64`).

---

## 💻 Code Explanation

### 📄 `main.py`
- **Role / Purpose**: Solution implementation for Problem 22.
- **Key Logic**: Defines functions: `alphabeticIndex()`.
- **How It Works**:
  - Implements the mathematical formula and pruning rules described above.
  - Efficiently iterates through the search space and produces the final answer.

---

## ⏱️ Complexity Analysis

| Metric | Complexity | Description |
| :--- | :--- | :--- |
| **Time Complexity** | $O(N \log N + N \cdot L)$ | Fast execution adhering to Project Euler's 1-minute performance rule. |
| **Space Complexity** | $O(N)$ | Efficient memory allocation. |

---

## 🚀 How to Run

```bash
python3 main.py
```

**Verified Answer / Result:**
```text
871198282
```
