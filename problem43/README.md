# 🧮 Project Euler Problem 43: Sub-string Divisibility

<div align="center">

![Project Euler](https://img.shields.io/badge/Project-Euler-6B4F2A?style=for-the-badge&logo=projecteuler&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Solved-success?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Combinatorics%20%C2%B7%20Permutations%20&%20Pruning-blue?style=for-the-badge)

</div>

---

## 📜 Problem Statement

Find the sum of all 0 to 9 pandigital numbers with sub-string divisibility properties.

🔗 **Project Euler Link:** [Problem 43](https://projecteuler.net/problem=43)

---

## 💡 Key Learnings & Mathematical Insights

- **Pandigital Permutations**: Iterate permutations of '0123456789'.
- **Window Modulo Checks**: Check 3-digit slices modulo 2, 3, 5, 7, 11, 13, 17.

---

## 💻 Code Explanation

### 📄 `main.py`
- **Role / Purpose**: Solution implementation for Problem 43.
- **Key Logic**: Defines functions: `isPandigitalZeroToNine()`, `property()`, `main()` (imports: `itertools`).
- **How It Works**:
  - Implements the mathematical formula and pruning rules described above.
  - Efficiently iterates through the search space and produces the final answer.

---

## ⏱️ Complexity Analysis

| Metric | Complexity | Description |
| :--- | :--- | :--- |
| **Time Complexity** | $O(10!)$ | Fast execution adhering to Project Euler's 1-minute performance rule. |
| **Space Complexity** | $O(1)$ | Efficient memory allocation. |

---

## 🚀 How to Run

```bash
python3 main.py
```

**Verified Answer / Result:**
```text
16695334890
```
