# 🧮 Project Euler Problem 56: Powerful Digit Sum

<div align="center">

![Project Euler](https://img.shields.io/badge/Project-Euler-6B4F2A?style=for-the-badge&logo=projecteuler&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Solved-success?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Math%20%C2%B7%20Power%20Digit%20Sums-blue?style=for-the-badge)

</div>

---

## 📜 Problem Statement

Considering natural numbers of the form $a^b$, where $a, b < 100$, what is the maximum digital sum?

🔗 **Project Euler Link:** [Problem 56](https://projecteuler.net/problem=56)

---

## 💡 Key Learnings & Mathematical Insights

- **Search Space**: Focus search on upper range $90 \le a, b < 100$.
- **Digit Sum**: Compute `sum(int(d) for d in str(a**b))`.

---

## 💻 Code Explanation

### 📄 `main.py`
- **Role / Purpose**: Solution implementation for Problem 56.
- **Key Logic**: Defines functions: `digitSum()`.
- **How It Works**:
  - Implements the mathematical formula and pruning rules described above.
  - Efficiently iterates through the search space and produces the final answer.

---

## ⏱️ Complexity Analysis

| Metric | Complexity | Description |
| :--- | :--- | :--- |
| **Time Complexity** | $O(N^2 \cdot D)$ | Fast execution adhering to Project Euler's 1-minute performance rule. |
| **Space Complexity** | $O(D)$ | Efficient memory allocation. |

---

## 🚀 How to Run

```bash
python3 main.py
```

**Verified Answer / Result:**
```text
972
```
