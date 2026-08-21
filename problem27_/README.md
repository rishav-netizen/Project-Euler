# 🧮 Project Euler Problem 27: Quadratic Primes

<div align="center">

![Project Euler](https://img.shields.io/badge/Project-Euler-6B4F2A?style=for-the-badge&logo=projecteuler&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Solved-success?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Number%20Theory%20%C2%B7%20Euler's%20Quadratic%20Polynomial-blue?style=for-the-badge)

</div>

---

## 📜 Problem Statement

Find the product of the coefficients, $a$ and $b$, for the quadratic expression $n^2 + an + b$ that produces the maximum number of primes for consecutive values of $n$, starting with $n = 0$, where $|a| < 1000$ and $|b| \le 1000$.

🔗 **Project Euler Link:** [Problem 27](https://projecteuler.net/problem=27)

---

## 💡 Key Learnings & Mathematical Insights

- **Prime $b$ Constraint**: At $n=0$, $0^2 + 0a + b = b$, so $b$ must be a positive prime $\le 1000$.
- **Odd $a$ Constraint**: For $n=1$, $1 + a + b$ must be odd prime, so $a$ must be odd.

---

## 💻 Code Explanation

### 📄 `main.py`
- **Role / Purpose**: Solution implementation for Problem 27.
- **Key Logic**: Defines functions: `isPrime()`.
- **How It Works**:
  - Implements the mathematical formula and pruning rules described above.
  - Efficiently iterates through the search space and produces the final answer.

---

## ⏱️ Complexity Analysis

| Metric | Complexity | Description |
| :--- | :--- | :--- |
| **Time Complexity** | $O(|a| \cdot |b_{\text{primes}}| \cdot \text{len})$ | Fast execution adhering to Project Euler's 1-minute performance rule. |
| **Space Complexity** | $O(1)$ | Efficient memory allocation. |

---

## 🚀 How to Run

```bash
python3 main.py
```

**Verified Answer / Result:**
```text
-59231
```
