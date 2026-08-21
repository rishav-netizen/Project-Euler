# 🧮 Project Euler Problem 24: Lexicographic Permutations

<div align="center">

![Project Euler](https://img.shields.io/badge/Project-Euler-6B4F2A?style=for-the-badge&logo=projecteuler&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Solved-success?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Combinatorics%20%C2%B7%20Factoradic%20Number%20System-blue?style=for-the-badge)

</div>

---

## 📜 Problem Statement

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

🔗 **Project Euler Link:** [Problem 24](https://projecteuler.net/problem=24)

---

## 💡 Key Learnings & Mathematical Insights

- **Factoradic Direct Indexing**: For $k=1,000,000$, iteratively divide $(k-1)$ by $(n-1)!$ to directly extract each digit in $O(N)$ without generating permutations.
- **`itertools.permutations`**: Direct slice / nth extraction in Python is clean and fast.

---

## 💻 Code Explanation

### 📄 `main.py`
- **Role / Purpose**: Solution implementation for Problem 24.
- **Key Logic**: Defines functions: `fact()`.
- **How It Works**:
  - Implements the mathematical formula and pruning rules described above.
  - Efficiently iterates through the search space and produces the final answer.

---

## ⏱️ Complexity Analysis

| Metric | Complexity | Description |
| :--- | :--- | :--- |
| **Time Complexity** | $O(N) / O(K)$ | Fast execution adhering to Project Euler's 1-minute performance rule. |
| **Space Complexity** | $O(N)$ | Efficient memory allocation. |

---

## 🚀 How to Run

```bash
python3 main.py
```

**Verified Answer / Result:**
```text
2783915460
```
