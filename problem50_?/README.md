# 🧮 Project Euler Problem 50: Consecutive Prime Sum

<div align="center">

![Project Euler](https://img.shields.io/badge/Project-Euler-6B4F2A?style=for-the-badge&logo=projecteuler&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Solved-success?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Number%20Theory%20%C2%B7%20Prefix%20Sums%20&%20Sliding%20Window-blue?style=for-the-badge)

</div>

---

## 📜 Problem Statement

Which prime, below one-million, can be written as the sum of the most consecutive primes?

🔗 **Project Euler Link:** [Problem 50](https://projecteuler.net/problem=50)

---

## 💡 Key Learnings & Mathematical Insights

- **Prefix Sum Array**: $S[k] = \sum_{i=0}^{k-1} p_i$. Any contiguous sum is $S[j] - S[i]$ in $O(1)$ time.
- **Window Size Descent**: Start search from largest possible prime window down to 1.

---

## 💻 Code Explanation

### 📄 `fun.py`
- **Role / Purpose**: Solution implementation for Problem 50 (Alternative / Optimized approach).
- **Key Logic**: Uses procedural script execution.
- **How It Works**:
  - Implements the mathematical formula and pruning rules described above.
  - Efficiently iterates through the search space and produces the final answer.

### 📄 `main.py`
- **Role / Purpose**: Solution implementation for Problem 50.
- **Key Logic**: Defines functions: `prime_sieve()`, `isPrime()`, `main()` (imports: `time`).
- **How It Works**:
  - Implements the mathematical formula and pruning rules described above.
  - Efficiently iterates through the search space and produces the final answer.

---

## ⏱️ Complexity Analysis

| Metric | Complexity | Description |
| :--- | :--- | :--- |
| **Time Complexity** | $O(P^2) / O(P)$ | Fast execution adhering to Project Euler's 1-minute performance rule. |
| **Space Complexity** | $O(P)$ | Efficient memory allocation. |

---

## 🚀 How to Run

```bash
python3 fun.py
```

**Verified Answer / Result:**
```text
997651
```
