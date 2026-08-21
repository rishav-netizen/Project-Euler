# 🧮 Project Euler Problem 81: Path Sum: Two Ways

<div align="center">

![Project Euler](https://img.shields.io/badge/Project-Euler-6B4F2A?style=for-the-badge&logo=projecteuler&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Solved-success?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Dynamic%20Programming%20%C2%B7%20Grid%20Minimum%20Path%20Sum-blue?style=for-the-badge)

</div>

---

## 📜 Problem Statement

Find the minimal path sum from top left to bottom right moving only right and down in the $80 \times 80$ matrix.

🔗 **Project Euler Link:** [Problem 81](https://projecteuler.net/problem=81)

---

## 💡 Key Learnings & Mathematical Insights

- **2D DP State Transition**: `dp[r][c] = matrix[r][c] + min(dp[r-1][c], dp[r][c-1])`.
- **Edge Accumulations**: Prefix sum first row and first column.

---

## 💻 Code Explanation

### 📄 `main.py`
- **Role / Purpose**: Solution implementation for Problem 81.
- **Key Logic**: Uses procedural script execution.
- **How It Works**:
  - Implements the mathematical formula and pruning rules described above.
  - Efficiently iterates through the search space and produces the final answer.

---

## ⏱️ Complexity Analysis

| Metric | Complexity | Description |
| :--- | :--- | :--- |
| **Time Complexity** | $O(R \cdot C)$ | Fast execution adhering to Project Euler's 1-minute performance rule. |
| **Space Complexity** | $O(R \cdot C)$ | Efficient memory allocation. |

---

## 🚀 How to Run

```bash
python3 main.py
```

**Verified Answer / Result:**
```text
427337
```
