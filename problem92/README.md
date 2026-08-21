# 🧮 Project Euler Problem 92: Square Digit Chains

<div align="center">

![Project Euler](https://img.shields.io/badge/Project-Euler-6B4F2A?style=for-the-badge&logo=projecteuler&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Solved-success?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Search%20%C2%B7%20Memoization%20&%20Cycle%20Convergence-blue?style=for-the-badge)

</div>

---

## 📜 Problem Statement

A number chain is created by continuously adding the square of the digits. Every number arrives at 1 or 89. How many starting numbers below ten million arrive at 89?

🔗 **Project Euler Link:** [Problem 92](https://projecteuler.net/problem=92)

---

## 💡 Key Learnings & Mathematical Insights

- **Domain Reduction**: For any $n < 10^7$, the sum of squares of digits is at most $7 \times 9^2 = 567$.
- **Precomputed Small Cache**: Precompute whether $1 \le k \le 567$ ends in 1 or 89; then any large number resolves in 1 step.

---

## 💻 Code Explanation

### 📄 `main.py`
- **Role / Purpose**: Solution implementation for Problem 92.
- **Key Logic**: Defines functions: `square_digit()`, `arrives_at()`, `main()`.
- **How It Works**:
  - Implements the mathematical formula and pruning rules described above.
  - Efficiently iterates through the search space and produces the final answer.

---

## ⏱️ Complexity Analysis

| Metric | Complexity | Description |
| :--- | :--- | :--- |
| **Time Complexity** | $O(N)$ | Fast execution adhering to Project Euler's 1-minute performance rule. |
| **Space Complexity** | $O(567) = O(1)$ | Efficient memory allocation. |

---

## 🚀 How to Run

```bash
python3 main.py
```

**Verified Answer / Result:**
```text
8581146
```
