# 🧮 Project Euler Problem 7: 10001st Prime

<div align="center">

![Project Euler](https://img.shields.io/badge/Project-Euler-6B4F2A?style=for-the-badge&logo=projecteuler&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Solved-success?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Number%20Theory%20%C2%B7%20Prime%20Generation-blue?style=for-the-badge)

</div>

---

## 📜 Problem Statement

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13. What is the 10001st prime number?

🔗 **Project Euler Link:** [Problem 7](https://projecteuler.net/problem=7)

---

## 💡 Key Learnings & Mathematical Insights

- **Trial Division with 6k ± 1**: Check primality by testing divisors up to $\sqrt{n}$, skipping multiples of 2 and 3.
- **Prime Number Theorem Upper Bound**: $p_n \approx n \ln n + n \ln \ln n$. For $n=10001$, $p_n < 115000$, keeping the search space very compact.

---

## 💻 Code Explanation

### 📄 `main.py`
- **Role / Purpose**: Solution implementation for Problem 7.
- **Key Logic**: Defines functions: `isPrime()`, `NthPrime()`.
- **How It Works**:
  - Implements the mathematical formula and pruning rules described above.
  - Efficiently iterates through the search space and produces the final answer.

---

## ⏱️ Complexity Analysis

| Metric | Complexity | Description |
| :--- | :--- | :--- |
| **Time Complexity** | $O(N \sqrt{p_N})$ | Fast execution adhering to Project Euler's 1-minute performance rule. |
| **Space Complexity** | $O(1)$ | Efficient memory allocation. |

---

## 🚀 How to Run

```bash
python3 main.py
```

**Verified Answer / Result:**
```text
104743
```
