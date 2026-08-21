# 🧮 Project Euler Problem 35: Circular Primes

<div align="center">

![Project Euler](https://img.shields.io/badge/Project-Euler-6B4F2A?style=for-the-badge&logo=projecteuler&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Solved-success?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Number%20Theory%20%C2%B7%20Prime%20Permutations-blue?style=for-the-badge)

</div>

---

## 📜 Problem Statement

How many circular primes are there below one million?

🔗 **Project Euler Link:** [Problem 35](https://projecteuler.net/problem=35)

---

## 💡 Key Learnings & Mathematical Insights

- **Cyclic Rotations**: Generate rotations of string representation: `s[i:] + s[:i]`.
- **Digit Filtering**: Discard any multi-digit number containing even digits (0, 2, 4, 6, 8) or 5, since one rotation would end in that digit and be composite.

---

## 💻 Code Explanation

### 📄 `main.py`
- **Role / Purpose**: Solution implementation for Problem 35.
- **Key Logic**: Defines functions: `primes_less_than()`, `isCircularPrime()`.
- **How It Works**:
  - Implements the mathematical formula and pruning rules described above.
  - Efficiently iterates through the search space and produces the final answer.

---

## ⏱️ Complexity Analysis

| Metric | Complexity | Description |
| :--- | :--- | :--- |
| **Time Complexity** | $O(N \log \log N) \text{ sieve} + O(N \cdot D)$ | Fast execution adhering to Project Euler's 1-minute performance rule. |
| **Space Complexity** | $O(N)$ | Efficient memory allocation. |

---

## 🚀 How to Run

```bash
python3 main.py
```

**Verified Answer / Result:**
```text
55
```
