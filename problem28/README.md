# 🧮 Project Euler Problem 28: Number Spiral Diagonals

<div align="center">

![Project Euler](https://img.shields.io/badge/Project-Euler-6B4F2A?style=for-the-badge&logo=projecteuler&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Solved-success?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Math%20%C2%B7%20Closed-Form%20Polynomials-blue?style=for-the-badge)

</div>

---

## 📜 Problem Statement

What is the sum of the numbers on the diagonals in a $1001 \times 1001$ spiral formed in the same way?

🔗 **Project Euler Link:** [Problem 28](https://projecteuler.net/problem=28)

---

## 💡 Key Learnings & Mathematical Insights

- **Corner Formula**: On layer $k$ (side $s = 2k+1$), the four corners are $s^2, s^2-(s-1), s^2-2(s-1), s^2-3(s-1)$.
- **Layer Sum**: Sum of 4 corners $= 4s^2 - 6(s-1) = 16k^2 + 4k + 4$. Summing $k=1$ to $500$ plus the center (1) gives the exact diagonal sum in $O(1)$ or $O(N)$.

---

## 💻 Code Explanation

### 📄 `main.py`
- **Role / Purpose**: Solution implementation for Problem 28.
- **Key Logic**: Defines functions: `cornerSum()`.
- **How It Works**:
  - Implements the mathematical formula and pruning rules described above.
  - Efficiently iterates through the search space and produces the final answer.

---

## ⏱️ Complexity Analysis

| Metric | Complexity | Description |
| :--- | :--- | :--- |
| **Time Complexity** | $O(N) / O(1)$ | Fast execution adhering to Project Euler's 1-minute performance rule. |
| **Space Complexity** | $O(1)$ | Efficient memory allocation. |

---

## 🚀 How to Run

```bash
python3 main.py
```

**Verified Answer / Result:**
```text
669171001
```
