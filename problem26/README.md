# 🧮 Project Euler Problem 26: Reciprocal Cycles

<div align="center">

![Project Euler](https://img.shields.io/badge/Project-Euler-6B4F2A?style=for-the-badge&logo=projecteuler&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Solved-success?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Number%20Theory%20%C2%B7%20Multiplicative%20Order-blue?style=for-the-badge)

</div>

---

## 📜 Problem Statement

Find the value of $d < 1000$ for which $1/d$ contains the longest recurring cycle in its decimal fraction part.

🔗 **Project Euler Link:** [Problem 26](https://projecteuler.net/problem=26)

---

## 💡 Key Learnings & Mathematical Insights

- **Long Division Remainder Tracking**: A recurring cycle begins when a remainder repeats in long division.
- **Multiplicative Order**: For $\gcd(d, 10) = 1$, cycle length is the smallest $k$ such that $10^k \equiv 1 \pmod d$ (maximum period $d-1$ occurs when 10 is a primitive root mod $d$).

---

## 💻 Code Explanation

### 📄 `main.py`
- **Role / Purpose**: Solution implementation for Problem 26.
- **Key Logic**: Uses procedural script execution.
- **How It Works**:
  - Implements the mathematical formula and pruning rules described above.
  - Efficiently iterates through the search space and produces the final answer.

---

## ⏱️ Complexity Analysis

| Metric | Complexity | Description |
| :--- | :--- | :--- |
| **Time Complexity** | $O(D^2)$ | Fast execution adhering to Project Euler's 1-minute performance rule. |
| **Space Complexity** | $O(D)$ | Efficient memory allocation. |

---

## 🚀 How to Run

```bash
python3 main.py
```

**Verified Answer / Result:**
```text
983
```
