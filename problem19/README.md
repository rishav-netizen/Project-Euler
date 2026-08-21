# 🧮 Project Euler Problem 19: Counting Sundays

<div align="center">

![Project Euler](https://img.shields.io/badge/Project-Euler-6B4F2A?style=for-the-badge&logo=projecteuler&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Solved-success?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Date%20Math%20%C2%B7%20Modular%20Arithmetic-blue?style=for-the-badge)

</div>

---

## 📜 Problem Statement

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

🔗 **Project Euler Link:** [Problem 19](https://projecteuler.net/problem=19)

---

## 💡 Key Learnings & Mathematical Insights

- **Leap Year Rules**: Divisible by 4, except century years unless divisible by 400 (1900 is not, 2000 is).
- **Modular Day Advancing**: Advance day counter by number of days in each month modulo 7 and check if `day % 7 == 0`.

---

## 💻 Code Explanation

### 📄 `main.py`
- **Role / Purpose**: Solution implementation for Problem 19.
- **Key Logic**: Defines functions: `isLeapYear()`, `main()`.
- **How It Works**:
  - Implements the mathematical formula and pruning rules described above.
  - Efficiently iterates through the search space and produces the final answer.

---

## ⏱️ Complexity Analysis

| Metric | Complexity | Description |
| :--- | :--- | :--- |
| **Time Complexity** | $O(Y \cdot 12) = O(1200)$ | Fast execution adhering to Project Euler's 1-minute performance rule. |
| **Space Complexity** | $O(1)$ | Efficient memory allocation. |

---

## 🚀 How to Run

```bash
python3 main.py
```

**Verified Answer / Result:**
```text
171
```
