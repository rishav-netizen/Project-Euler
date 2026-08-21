# 🧮 Project Euler Problem 12: Highly Divisible Triangular Number

<div align="center">

![Project Euler](https://img.shields.io/badge/Project-Euler-6B4F2A?style=for-the-badge&logo=projecteuler&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Solved-success?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Number%20Theory%20%C2%B7%20Divisor%20Function-blue?style=for-the-badge)

</div>

---

## 📜 Problem Statement

What is the value of the first triangle number to have over five hundred divisors?

🔗 **Project Euler Link:** [Problem 12](https://projecteuler.net/problem=12)

---

## 💡 Key Learnings & Mathematical Insights

- **Divisor Counting in $O(\sqrt{N})$**: Pair factors $i$ and $n/i$ up to $\sqrt{n}$.
- **Coprime Factorization**: For $T_n = \frac{n(n+1)}{2}$, since $\gcd(n, n+1) = 1$, $d(T_n) = d(n/2) \cdot d(n+1)$ (if $n$ even) or $d(n) \cdot d((n+1)/2)$ (if $n$ odd).

---

## 💻 Code Explanation

### 📄 `main.py`
- **Role / Purpose**: Solution implementation for Problem 12.
- **Key Logic**: Defines functions: `primeFactorsOf()`, `triangularNumber()`.
- **How It Works**:
  - Implements the mathematical formula and pruning rules described above.
  - Efficiently iterates through the search space and produces the final answer.

---

## ⏱️ Complexity Analysis

| Metric | Complexity | Description |
| :--- | :--- | :--- |
| **Time Complexity** | $O(\sqrt{T_n}) \text{ per step}$ | Fast execution adhering to Project Euler's 1-minute performance rule. |
| **Space Complexity** | $O(1)$ | Efficient memory allocation. |

---

## 🚀 How to Run

```bash
python3 main.py
```

**Verified Answer / Result:**
```text
76576500
```
