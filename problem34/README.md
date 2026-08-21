# 🧮 Project Euler Problem 34: Digit Factorials

<div align="center">

![Project Euler](https://img.shields.io/badge/Project-Euler-6B4F2A?style=for-the-badge&logo=projecteuler&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Solved-success?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Search%20%C2%B7%20Factorions-blue?style=for-the-badge)

</div>

---

## 📜 Problem Statement

Find the sum of all numbers which are equal to the sum of the factorial of their digits (excluding 1 and 2).

🔗 **Project Euler Link:** [Problem 34](https://projecteuler.net/problem=34)

---

## 💡 Key Learnings & Mathematical Insights

- **Upper Bound Constraint**: For $k=7$ digits, $7 \times 9! = 2,540,160 < 10^7$, establishing an upper bound of $2.54 \times 10^6$.
- **Lookup Table**: Precompute $0!, 1!, \dots, 9!$ in a list for fast access.

---

## 💻 Code Explanation

### 📄 `main.py`
- **Role / Purpose**: Solution implementation for Problem 34.
- **Key Logic**: Defines functions: `fact()`, `digit_fact()`, `result()`.
- **How It Works**:
  - Implements the mathematical formula and pruning rules described above.
  - Efficiently iterates through the search space and produces the final answer.

---

## ⏱️ Complexity Analysis

| Metric | Complexity | Description |
| :--- | :--- | :--- |
| **Time Complexity** | $O(M \cdot D)$ | Fast execution adhering to Project Euler's 1-minute performance rule. |
| **Space Complexity** | $O(1)$ | Efficient memory allocation. |

---

## 🚀 How to Run

```bash
python3 main.py
```

**Verified Answer / Result:**
```text
40730
```
