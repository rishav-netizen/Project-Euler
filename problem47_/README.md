# 🧮 Project Euler Problem 47: Distinct Primes Factors

<div align="center">

![Project Euler](https://img.shields.io/badge/Project-Euler-6B4F2A?style=for-the-badge&logo=projecteuler&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Solved-success?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Number%20Theory%20%C2%B7%20Sieve%20Factorization-blue?style=for-the-badge)

</div>

---

## 📜 Problem Statement

Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?

🔗 **Project Euler Link:** [Problem 47](https://projecteuler.net/problem=47)

---

## 💡 Key Learnings & Mathematical Insights

- **Sieve Factor Counter**: Run a sieve array that increments factor counts `count[m] += 1` for all multiples of each prime.
- **Consecutive Streak Tracker**: Scan array for index $i$ where `count[i] == count[i+1] == count[i+2] == count[i+3] == 4`.

---

## 💻 Code Explanation

### 📄 `codex_optimized.py`
- **Role / Purpose**: Solution implementation for Problem 47 (Alternative / Optimized approach).
- **Key Logic**: Defines functions: `primes_upto()`, `first_consecutive_numbers()` (imports: `array, math`).
- **How It Works**:
  - Implements the mathematical formula and pruning rules described above.
  - Efficiently iterates through the search space and produces the final answer.

### 📄 `main.py`
- **Role / Purpose**: Solution implementation for Problem 47.
- **Key Logic**: Defines functions: `factors_of()`.
- **How It Works**:
  - Implements the mathematical formula and pruning rules described above.
  - Efficiently iterates through the search space and produces the final answer.

### 📄 `seive_optimization.py`
- **Role / Purpose**: Solution implementation for Problem 47 (Alternative / Optimized approach).
- **Key Logic**: Uses procedural script execution.
- **How It Works**:
  - Implements the mathematical formula and pruning rules described above.
  - Efficiently iterates through the search space and produces the final answer.

---

## ⏱️ Complexity Analysis

| Metric | Complexity | Description |
| :--- | :--- | :--- |
| **Time Complexity** | $O(N \log \log N)$ | Fast execution adhering to Project Euler's 1-minute performance rule. |
| **Space Complexity** | $O(N)$ | Efficient memory allocation. |

---

## 🚀 How to Run

```bash
python3 codex_optimized.py
```

**Verified Answer / Result:**
```text
134043
```
