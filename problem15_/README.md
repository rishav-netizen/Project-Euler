# 🧮 Project Euler Problem 15: Lattice Paths

<div align="center">

![Project Euler](https://img.shields.io/badge/Project-Euler-6B4F2A?style=for-the-badge&logo=projecteuler&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Solved-success?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Combinatorics%20%C2%B7%20Binomial%20Coefficients-blue?style=for-the-badge)

</div>

---

## 📜 Problem Statement

Starting in the top left corner of a $20 \times 20$ grid, and only being able to move to the right and down, how many such routes are there through the grid?

🔗 **Project Euler Link:** [Problem 15](https://projecteuler.net/problem=15)

---

## 💡 Key Learnings & Mathematical Insights

- **Combinatorial Equivalence**: Traversing an $N \times N$ grid requires exactly $N$ Right moves and $N$ Down moves ($2N$ total steps).
- **Binomial Formula**: Total distinct paths $= \binom{2N}{N} = \frac{(2N)!}{(N!)^2} = \binom{40}{20} = 137,846,528,820$.

---

## 💻 Code Explanation

### 📄 `main.py`
- **Role / Purpose**: Solution implementation for Problem 15.
- **Key Logic**: Uses procedural script execution.
- **How It Works**:
  - Implements the mathematical formula and pruning rules described above.
  - Efficiently iterates through the search space and produces the final answer.

---

## ⏱️ Complexity Analysis

| Metric | Complexity | Description |
| :--- | :--- | :--- |
| **Time Complexity** | $O(N) / O(1)$ | Fast execution adhering to Project Euler's 1-minute performance rule. |
| **Space Complexity** | $O(1)$ | Efficient memory allocation. |

---

## 🚀 How to Run

```bash
python3 main.py
```

**Verified Answer / Result:**
```text
137846528820
```
