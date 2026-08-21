# 🧮 Project Euler Problem 76: Counting Summations

<div align="center">

![Project Euler](https://img.shields.io/badge/Project-Euler-6B4F2A?style=for-the-badge&logo=projecteuler&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Solved-success?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Dynamic%20Programming%20%C2%B7%20Integer%20Partitions-blue?style=for-the-badge)

</div>

---

## 📜 Problem Statement

How many different ways can one hundred be written as a sum of at least two positive integers?

🔗 **Project Euler Link:** [Problem 76](https://projecteuler.net/problem=76)

---

## 💡 Key Learnings & Mathematical Insights

- **Partition Function**: `dp[i] += dp[i - num]` for $1 \le \text{num} < 100$.
- **Result**: `dp[100]` gives all partitions into at least two numbers.

---

## 💻 Code Explanation

### 📄 `main.py`
- **Role / Purpose**: Solution implementation for Problem 76.
- **Key Logic**: Defines functions: `main()`.
- **How It Works**:
  - Implements the mathematical formula and pruning rules described above.
  - Efficiently iterates through the search space and produces the final answer.

---

## ⏱️ Complexity Analysis

| Metric | Complexity | Description |
| :--- | :--- | :--- |
| **Time Complexity** | $O(N^2)$ | Fast execution adhering to Project Euler's 1-minute performance rule. |
| **Space Complexity** | $O(N)$ | Efficient memory allocation. |

---

## 🚀 How to Run

```bash
python3 main.py
```

**Verified Answer / Result:**
```text
190569291
```
