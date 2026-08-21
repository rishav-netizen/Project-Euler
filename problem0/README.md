# 🧮 Project Euler Problem 0: Sum of Squares of Odd Numbers

<div align="center">

![Project Euler](https://img.shields.io/badge/Project-Euler-6B4F2A?style=for-the-badge&logo=projecteuler&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Solved-success?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Warmup%20%C2%B7%20Arithmetic-blue?style=for-the-badge)

</div>

---

## 📜 Problem Statement

Calculate the sum of squares of all numbers ending in an odd digit (1, 3, 5, 7, 9) below 225,000.

🔗 **Project Euler Link:** [Problem 0](#)

---

## 💡 Key Learnings & Mathematical Insights

- **Odd Residue Filtering**: Checking `(i % 10) in {1, 3, 5, 7, 9}` isolates all odd integers by their last base-10 digit.
- **Accumulator Pattern**: Iterates through the range $[1, 225000)$ and accumulates $i^2$ for all matching odd numbers.

---

## 💻 Code Explanation

### 📄 `main.py`
- **Role / Purpose**: Solution implementation for Problem 0.
- **Key Logic**: Uses procedural script execution.
- **How It Works**:
  - Implements the mathematical formula and pruning rules described above.
  - Efficiently iterates through the search space and produces the final answer.

---

## ⏱️ Complexity Analysis

| Metric | Complexity | Description |
| :--- | :--- | :--- |
| **Time Complexity** | $O(N)$ | Fast execution adhering to Project Euler's 1-minute performance rule. |
| **Space Complexity** | $O(1)$ | Efficient memory allocation. |

---

## 🚀 How to Run

```bash
python3 main.py
```

**Verified Answer / Result:**
```text
1898437499962500
```
