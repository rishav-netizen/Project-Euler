# 🧮 Project Euler Problem 18: Maximum Path Sum I

<div align="center">

![Project Euler](https://img.shields.io/badge/Project-Euler-6B4F2A?style=for-the-badge&logo=projecteuler&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Solved-success?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Dynamic%20Programming%20%C2%B7%20Bottom-Up%20DP-blue?style=for-the-badge)

</div>

---

## 📜 Problem Statement

Find the maximum total from top to bottom of the 15-row triangle.

🔗 **Project Euler Link:** [Problem 18](https://projecteuler.net/problem=18)

---

## 💡 Key Learnings & Mathematical Insights

- **Bottom-Up DP**: Instead of exploring $2^{14}$ paths, collapse from row $n-2$ up to row 0.
- **Optimal Substructure**: `triangle[r][c] += max(triangle[r+1][c], triangle[r+1][c+1])`. In-place and non-recursive.

---

## 💻 Code Explanation

### 📄 `main.py`
- **Role / Purpose**: Solution implementation for Problem 18.
- **Key Logic**: Uses procedural script execution.
- **How It Works**:
  - Implements the mathematical formula and pruning rules described above.
  - Efficiently iterates through the search space and produces the final answer.

---

## ⏱️ Complexity Analysis

| Metric | Complexity | Description |
| :--- | :--- | :--- |
| **Time Complexity** | $O(R^2)$ | Fast execution adhering to Project Euler's 1-minute performance rule. |
| **Space Complexity** | $O(1) \text{ in-place}$ | Efficient memory allocation. |

---

## 🚀 How to Run

```bash
python3 main.py
```

**Verified Answer / Result:**
```text
1074
```
