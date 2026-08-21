# 🧮 Project Euler Problem 52: Permuted Multiples

<div align="center">

![Project Euler](https://img.shields.io/badge/Project-Euler-6B4F2A?style=for-the-badge&logo=projecteuler&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Solved-success?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Search%20%C2%B7%20Digit%20Signatures-blue?style=for-the-badge)

</div>

---

## 📜 Problem Statement

Find the smallest positive integer, $x$, such that $2x, 3x, 4x, 5x$, and $6x$, contain the same digits.

🔗 **Project Euler Link:** [Problem 52](https://projecteuler.net/problem=52)

---

## 💡 Key Learnings & Mathematical Insights

- **Permutation Signature**: Check `sorted(str(x)) == sorted(str(2*x)) == ... == sorted(str(6*x))`.
- **Leading Digit Bound**: For $6x$ to have the same digit count as $x$, $x$ must start with 1.

---

## 💻 Code Explanation

### 📄 `main.py`
- **Role / Purpose**: Solution implementation for Problem 52.
- **Key Logic**: Uses procedural script execution.
- **How It Works**:
  - Implements the mathematical formula and pruning rules described above.
  - Efficiently iterates through the search space and produces the final answer.

---

## ⏱️ Complexity Analysis

| Metric | Complexity | Description |
| :--- | :--- | :--- |
| **Time Complexity** | $O(\text{search})$ | Fast execution adhering to Project Euler's 1-minute performance rule. |
| **Space Complexity** | $O(1)$ | Efficient memory allocation. |

---

## 🚀 How to Run

```bash
python3 main.py
```

**Verified Answer / Result:**
```text
142857
```
