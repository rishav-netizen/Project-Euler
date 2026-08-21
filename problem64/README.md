# 🧮 Project Euler Problem 64: Odd Period Square Roots

<div align="center">

![Project Euler](https://img.shields.io/badge/Project-Euler-6B4F2A?style=for-the-badge&logo=projecteuler&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Solved-success?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Number%20Theory%20%C2%B7%20Continued%20Fractions%20&%20Periodicity-blue?style=for-the-badge)

</div>

---

## 📜 Problem Statement

How many continued fractions for $N \le 10000$ have an odd period length?

🔗 **Project Euler Link:** [Problem 64](https://projecteuler.net/problem=64)

---

## 💡 Key Learnings & Mathematical Insights

- **Continued Fraction Step**: $m_{k+1} = d_k a_k - m_k$, $d_{k+1} = \frac{N - m_{k+1}^2}{d_k}$, $a_{k+1} = \lfloor \frac{a_0 + m_{k+1}}{d_{k+1}} \rfloor$.
- **Period Termination**: The period repeats as soon as $a_k = 2a_0$.

---

## 💻 Code Explanation

### 📄 `main.py`
- **Role / Purpose**: Solution implementation for Problem 64.
- **Key Logic**: Defines functions: `get_period_length()`, `main()` (imports: `math`).
- **How It Works**:
  - Implements the mathematical formula and pruning rules described above.
  - Efficiently iterates through the search space and produces the final answer.

---

## ⏱️ Complexity Analysis

| Metric | Complexity | Description |
| :--- | :--- | :--- |
| **Time Complexity** | $O(N \cdot \text{period})$ | Fast execution adhering to Project Euler's 1-minute performance rule. |
| **Space Complexity** | $O(1)$ | Efficient memory allocation. |

---

## 🚀 How to Run

```bash
python3 main.py
```

**Verified Answer / Result:**
```text
1322
```
