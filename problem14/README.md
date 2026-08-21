# 🧮 Project Euler Problem 14: Longest Collatz Sequence

<div align="center">

![Project Euler](https://img.shields.io/badge/Project-Euler-6B4F2A?style=for-the-badge&logo=projecteuler&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Solved-success?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Dynamic%20Programming%20%C2%B7%20Memoization-blue?style=for-the-badge)

</div>

---

## 📜 Problem Statement

Which starting number, under one million, produces the longest Collatz sequence?

🔗 **Project Euler Link:** [Problem 14](https://projecteuler.net/problem=14)

---

## 💡 Key Learnings & Mathematical Insights

- **Collatz Trajectory**: $n \to n/2$ (even) and $n \to 3n+1$ (odd).
- **Memoization / Dynamic Programming**: Caching sequence lengths of visited numbers avoids recalculating overlapping subproblems.

---

## 💻 Code Explanation

### 📄 `main.py`
- **Role / Purpose**: Solution implementation for Problem 14.
- **Key Logic**: Uses procedural script execution.
- **How It Works**:
  - Implements the mathematical formula and pruning rules described above.
  - Efficiently iterates through the search space and produces the final answer.

---

## ⏱️ Complexity Analysis

| Metric | Complexity | Description |
| :--- | :--- | :--- |
| **Time Complexity** | $O(N)$ | Fast execution adhering to Project Euler's 1-minute performance rule. |
| **Space Complexity** | $O(N) / O(1)$ | Efficient memory allocation. |

---

## 🚀 How to Run

```bash
python3 main.py
```

**Verified Answer / Result:**
```text
837799
```
