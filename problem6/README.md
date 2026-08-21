# 🧮 Project Euler Problem 6: Sum Square Difference

<div align="center">

![Project Euler](https://img.shields.io/badge/Project-Euler-6B4F2A?style=for-the-badge&logo=projecteuler&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Solved-success?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Math%20%C2%B7%20Closed-Form%20Polynomials-blue?style=for-the-badge)

</div>

---

## 📜 Problem Statement

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

🔗 **Project Euler Link:** [Problem 6](https://projecteuler.net/problem=6)

---

## 💡 Key Learnings & Mathematical Insights

- **Sum of First $n$ Numbers**: $S_1 = \frac{n(n+1)}{2}$.
- **Sum of First $n$ Squares**: $S_2 = \frac{n(n+1)(2n+1)}{6}$.
- **Closed-Form Difference**: $\Delta = S_1^2 - S_2 = \frac{n(n+1)(n-1)(3n+2)}{12}$. Evaluates instantly in $O(1)$ time.

---

## 💻 Code Explanation

### 📄 `main.py`
- **Role / Purpose**: Solution implementation for Problem 6.
- **Key Logic**: Defines functions: `sumOfSquares()`, `sumOf()`.
- **How It Works**:
  - Implements the mathematical formula and pruning rules described above.
  - Efficiently iterates through the search space and produces the final answer.

---

## ⏱️ Complexity Analysis

| Metric | Complexity | Description |
| :--- | :--- | :--- |
| **Time Complexity** | $O(1)$ | Fast execution adhering to Project Euler's 1-minute performance rule. |
| **Space Complexity** | $O(1)$ | Efficient memory allocation. |

---

## 🚀 How to Run

```bash
python3 main.py
```

**Verified Answer / Result:**
```text
25164150
```
