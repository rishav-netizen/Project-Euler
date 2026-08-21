# 🧮 Project Euler Problem 46: Goldbach's Other Conjecture

<div align="center">

![Project Euler](https://img.shields.io/badge/Project-Euler-6B4F2A?style=for-the-badge&logo=projecteuler&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Solved-success?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Number%20Theory%20%C2%B7%20Prime%20&%20Square%20Decompositions-blue?style=for-the-badge)

</div>

---

## 📜 Problem Statement

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square ($n = p + 2k^2$)?

🔗 **Project Euler Link:** [Problem 46](https://projecteuler.net/problem=46)

---

## 💡 Key Learnings & Mathematical Insights

- **Decomposition Test**: For odd composite $n$, iterate $k=1, 2, \dots$ while $2k^2 < n$, and test if $n - 2k^2$ is prime.
- **First Counterexample**: The loop terminates at $n = 5777$.

---

## 💻 Code Explanation

### 📄 `main.py`
- **Role / Purpose**: Solution implementation for Problem 46.
- **Key Logic**: Defines functions: `get_primes_till()`.
- **How It Works**:
  - Implements the mathematical formula and pruning rules described above.
  - Efficiently iterates through the search space and produces the final answer.

---

## ⏱️ Complexity Analysis

| Metric | Complexity | Description |
| :--- | :--- | :--- |
| **Time Complexity** | $O(N \sqrt{N})$ | Fast execution adhering to Project Euler's 1-minute performance rule. |
| **Space Complexity** | $O(N)$ | Efficient memory allocation. |

---

## 🚀 How to Run

```bash
python3 main.py
```

**Verified Answer / Result:**
```text
5777
```
