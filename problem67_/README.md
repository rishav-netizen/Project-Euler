# 🧮 Project Euler Problem 67: Maximum Path Sum II

<div align="center">

![Project Euler](https://img.shields.io/badge/Project-Euler-6B4F2A?style=for-the-badge&logo=projecteuler&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Solved-success?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Dynamic%20Programming%20%C2%B7%20Bottom-Up%20DP-blue?style=for-the-badge)

</div>

---

## 📜 Problem Statement

Find the maximum total from top to bottom of the 100-row triangle.

🔗 **Project Euler Link:** [Problem 67](https://projecteuler.net/problem=67)

---

## 💡 Key Learnings & Mathematical Insights

- **Exponential Search Failure**: $2^{99} \approx 6.33 \times 10^{29}$ total paths impossible to search naively.
- **Bottom-Up Dynamic Programming**: Reduce from row 98 upwards in $O(R^2)$ operations.

---

## 💻 Code Explanation

### 📄 `main.py`
- **Role / Purpose**: Solution implementation for Problem 67.
- **Key Logic**: Uses procedural script execution.
- **How It Works**:
  - Implements the mathematical formula and pruning rules described above.
  - Efficiently iterates through the search space and produces the final answer.

---

## ⏱️ Complexity Analysis

| Metric | Complexity | Description |
| :--- | :--- | :--- |
| **Time Complexity** | $O(R^2) = O(10000)$ | Fast execution adhering to Project Euler's 1-minute performance rule. |
| **Space Complexity** | $O(1) \text{ in-place}$ | Efficient memory allocation. |

---

## 🚀 How to Run

```bash
python3 main.py
```

**Verified Answer / Result:**
```text
7273
```
