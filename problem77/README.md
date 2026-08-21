# 🧮 Project Euler Problem 77: Prime Summations

<div align="center">

![Project Euler](https://img.shields.io/badge/Project-Euler-6B4F2A?style=for-the-badge&logo=projecteuler&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Solved-success?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Dynamic%20Programming%20%C2%B7%20Prime%20Partitions-blue?style=for-the-badge)

</div>

---

## 📜 Problem Statement

What is the first value which can be written as the sum of primes in over five thousand different ways?

🔗 **Project Euler Link:** [Problem 77](https://projecteuler.net/problem=77)

---

## 💡 Key Learnings & Mathematical Insights

- **Prime Coin Change**: Dynamic programming with prime numbers as coin values.
- **First Exceeding 5000**: Increases target until `dp[n] > 5000` (reaches 71).

---

## 💻 Code Explanation

### 📄 `main.py`
- **Role / Purpose**: Solution implementation for Problem 77.
- **Key Logic**: Defines functions: `primesTill()`, `main()`.
- **How It Works**:
  - Implements the mathematical formula and pruning rules described above.
  - Efficiently iterates through the search space and produces the final answer.

---

## ⏱️ Complexity Analysis

| Metric | Complexity | Description |
| :--- | :--- | :--- |
| **Time Complexity** | $O(N \cdot \pi(N))$ | Fast execution adhering to Project Euler's 1-minute performance rule. |
| **Space Complexity** | $O(N)$ | Efficient memory allocation. |

---

## 🚀 How to Run

```bash
python3 main.py
```

**Verified Answer / Result:**
```text
71
```
