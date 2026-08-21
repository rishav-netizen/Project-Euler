# 🧮 Project Euler Problem 30: Digit Fifth Powers

<div align="center">

![Project Euler](https://img.shields.io/badge/Project-Euler-6B4F2A?style=for-the-badge&logo=projecteuler&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Solved-success?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Search%20%C2%B7%20Upper%20Bound%20Analysis-blue?style=for-the-badge)

</div>

---

## 📜 Problem Statement

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

🔗 **Project Euler Link:** [Problem 30](https://projecteuler.net/problem=30)

---

## 💡 Key Learnings & Mathematical Insights

- **Upper Bound Constraint**: A $k$-digit number has maximum digit 5th power sum $k \times 9^5 = k \times 59049$. For $k=6$, $6 \times 59049 = 354294$. For $k=7$, $7 \times 59049 = 413343 < 10^6$. Hence, no solution can exceed 354,294.
- **1-Digit Exclusion**: Single digits like $1^5 = 1$ are explicitly excluded.

---

## 💻 Code Explanation

### 📄 `main.py`
- **Role / Purpose**: Solution implementation for Problem 30.
- **Key Logic**: Defines functions: `digitPowerSum()`.
- **How It Works**:
  - Implements the mathematical formula and pruning rules described above.
  - Efficiently iterates through the search space and produces the final answer.

---

## ⏱️ Complexity Analysis

| Metric | Complexity | Description |
| :--- | :--- | :--- |
| **Time Complexity** | $O(M \cdot D) \text{ where } M = 354294$ | Fast execution adhering to Project Euler's 1-minute performance rule. |
| **Space Complexity** | $O(1)$ | Efficient memory allocation. |

---

## 🚀 How to Run

```bash
python3 main.py
```

**Verified Answer / Result:**
```text
443839
```
