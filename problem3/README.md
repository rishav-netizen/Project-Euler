# 🧮 Project Euler Problem 3: Largest Prime Factor

<div align="center">

![Project Euler](https://img.shields.io/badge/Project-Euler-6B4F2A?style=for-the-badge&logo=projecteuler&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Solved-success?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Number%20Theory%20%C2%B7%20Prime%20Factorization-blue?style=for-the-badge)

</div>

---

## 📜 Problem Statement

What is the largest prime factor of the number 600,851,475,143?

🔗 **Project Euler Link:** [Problem 3](https://projecteuler.net/problem=3)

---

## 💡 Key Learnings & Mathematical Insights

- **Trial Division & Continuous Reduction**: Dividing out each factor $d$ completely as soon as discovered ensures that every subsequent divisor found is prime.
- **Square Root Bound**: Iterating divisors only up to $\sqrt{N}$ is sufficient; any remaining cofactor $> 1$ is guaranteed to be prime.

---

## 💻 Code Explanation

### 📄 `main.py`
- **Role / Purpose**: Solution implementation for Problem 3.
- **Key Logic**: Defines functions: `isPrime()`, `maxPrimeFactorOf()`, `largestPrimeFactor()`.
- **How It Works**:
  - Implements the mathematical formula and pruning rules described above.
  - Efficiently iterates through the search space and produces the final answer.

---

## ⏱️ Complexity Analysis

| Metric | Complexity | Description |
| :--- | :--- | :--- |
| **Time Complexity** | $O(\sqrt{N})$ | Fast execution adhering to Project Euler's 1-minute performance rule. |
| **Space Complexity** | $O(1)$ | Efficient memory allocation. |

---

## 🚀 How to Run

```bash
python3 main.py
```

**Verified Answer / Result:**
```text
6857
```
