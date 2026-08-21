# 🧮 Project Euler Problem 41: Pandigital Prime

<div align="center">

![Project Euler](https://img.shields.io/badge/Project-Euler-6B4F2A?style=for-the-badge&logo=projecteuler&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Solved-success?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Number%20Theory%20%C2%B7%20Divisibility%20by%203%20&%20Primes-blue?style=for-the-badge)

</div>

---

## 📜 Problem Statement

What is the largest n-digit pandigital prime that exists?

🔗 **Project Euler Link:** [Problem 41](https://projecteuler.net/problem=41)

---

## 💡 Key Learnings & Mathematical Insights

- **Divisibility by 3 Elimination**: 8-digit pandigital sum is $\sum_{1}^8 i = 36$ (divisible by 3) and 9-digit is $\sum_{1}^9 i = 45$ (divisible by 3). Neither can ever be prime!
- **7-Digit Search Space**: The maximum pandigital prime must have at most 7 digits ($1+\dots+7=28 \not\equiv 0 \pmod 3$). Search permutations of '7654321' downwards.

---

## 💻 Code Explanation

### 📄 `main.py`
- **Role / Purpose**: Solution implementation for Problem 41.
- **Key Logic**: Defines functions: `isPandigitalPrime()`, `isPrime()`, `sumTill()`.
- **How It Works**:
  - Implements the mathematical formula and pruning rules described above.
  - Efficiently iterates through the search space and produces the final answer.

---

## ⏱️ Complexity Analysis

| Metric | Complexity | Description |
| :--- | :--- | :--- |
| **Time Complexity** | $O(7! \cdot \sqrt{N})$ | Fast execution adhering to Project Euler's 1-minute performance rule. |
| **Space Complexity** | $O(1)$ | Efficient memory allocation. |

---

## 🚀 How to Run

```bash
python3 main.py
```

**Verified Answer / Result:**
```text
7652413
```
