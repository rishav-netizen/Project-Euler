# 🧮 Project Euler Problem 2: Even Fibonacci Numbers

<div align="center">

![Project Euler](https://img.shields.io/badge/Project-Euler-6B4F2A?style=for-the-badge&logo=projecteuler&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Solved-success?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Math%20%C2%B7%20Sequences%20&%20Series-blue?style=for-the-badge)

</div>

---

## 📜 Problem Statement

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

🔗 **Project Euler Link:** [Problem 2](https://projecteuler.net/problem=2)

---

## 💡 Key Learnings & Mathematical Insights

- **Parity Structure**: Fibonacci terms follow *odd, odd, even, odd, odd, even...* Every 3rd Fibonacci number is even ($F_3=2, F_6=8, F_9=34, \dots$).
- **Direct Recurrence**: Even terms satisfy $E_n = 4E_{n-1} + E_{n-2}$, which allows stepping directly through even terms without computing odd terms.

---

## 💻 Code Explanation

### 📄 `main.py`
- **Role / Purpose**: Solution implementation for Problem 2.
- **Key Logic**: Defines functions: `fib()`, `print_fib()`, `evenFibSum()`.
- **How It Works**:
  - Implements the mathematical formula and pruning rules described above.
  - Efficiently iterates through the search space and produces the final answer.

---

## ⏱️ Complexity Analysis

| Metric | Complexity | Description |
| :--- | :--- | :--- |
| **Time Complexity** | $O(\log N)$ | Fast execution adhering to Project Euler's 1-minute performance rule. |
| **Space Complexity** | $O(1)$ | Efficient memory allocation. |

---

## 🚀 How to Run

```bash
python3 main.py
```

**Verified Answer / Result:**
```text
4613732
```
