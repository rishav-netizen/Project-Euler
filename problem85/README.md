# 🧮 Project Euler Problem 85: Counting Rectangles

<div align="center">

![Project Euler](https://img.shields.io/badge/Project-Euler-6B4F2A?style=for-the-badge&logo=projecteuler&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Solved-success?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Combinatorics%20%C2%B7%20Rectangle%20Counting-blue?style=for-the-badge)

</div>

---

## 📜 Problem Statement

Find the area of the grid with the number of sub-rectangles nearest to two million.

🔗 **Project Euler Link:** [Problem 85](https://projecteuler.net/problem=85)

---

## 💡 Key Learnings & Mathematical Insights

- **Rectangle Count in $m \times n$**: $\binom{m+1}{2} \times \binom{n+1}{2} = \frac{m(m+1)n(n+1)}{4}$.
- **Target Proximity**: Iterate $m$ and solve for $n$ to minimize $|\text{count} - 2,000,000|$.

---

## 💻 Code Explanation

### 📄 `main.py`
- **Role / Purpose**: Solution implementation for Problem 85.
- **Key Logic**: Defines functions: `rects()`, `main()`.
- **How It Works**:
  - Implements the mathematical formula and pruning rules described above.
  - Efficiently iterates through the search space and produces the final answer.

---

## ⏱️ Complexity Analysis

| Metric | Complexity | Description |
| :--- | :--- | :--- |
| **Time Complexity** | $O(\sqrt{\text{target}})$ | Fast execution adhering to Project Euler's 1-minute performance rule. |
| **Space Complexity** | $O(1)$ | Efficient memory allocation. |

---

## 🚀 How to Run

```bash
python3 main.py
```

**Verified Answer / Result:**
```text
2772
```
