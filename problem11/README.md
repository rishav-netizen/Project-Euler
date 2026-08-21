# 🧮 Project Euler Problem 11: Largest Product in a Grid

<div align="center">

![Project Euler](https://img.shields.io/badge/Project-Euler-6B4F2A?style=for-the-badge&logo=projecteuler&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Solved-success?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Algorithms%20%C2%B7%202D%20Grid%20Traversal-blue?style=for-the-badge)

</div>

---

## 📜 Problem Statement

In the $20 \times 20$ grid, what is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally)?

🔗 **Project Euler Link:** [Problem 11](https://projecteuler.net/problem=11)

---

## 💡 Key Learnings & Mathematical Insights

- **4-Direction Vectors**: For every cell $(r, c)$, check 4 non-redundant directions: Horizontal $(\to)$, Vertical $(\downarrow)$, Main Diagonal $(\searrow)$, and Anti-Diagonal $(\swarrow)$.
- **Boundary Checking**: Restrict loop bounds so 4 consecutive items stay within $[0, 19]$.

---

## 💻 Code Explanation

### 📄 `correct.py`
- **Role / Purpose**: Solution implementation for Problem 11 (Alternative / Optimized approach).
- **Key Logic**: Uses procedural script execution.
- **How It Works**:
  - Implements the mathematical formula and pruning rules described above.
  - Efficiently iterates through the search space and produces the final answer.

### 📄 `main.py`
- **Role / Purpose**: Solution implementation for Problem 11.
- **Key Logic**: Uses procedural script execution.
- **How It Works**:
  - Implements the mathematical formula and pruning rules described above.
  - Efficiently iterates through the search space and produces the final answer.

---

## ⏱️ Complexity Analysis

| Metric | Complexity | Description |
| :--- | :--- | :--- |
| **Time Complexity** | $O(R \cdot C)$ | Fast execution adhering to Project Euler's 1-minute performance rule. |
| **Space Complexity** | $O(1)$ | Efficient memory allocation. |

---

## 🚀 How to Run

```bash
python3 correct.py
```

**Verified Answer / Result:**
```text
70600674
```
