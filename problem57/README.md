# 🧮 Project Euler Problem 57: Square Root Convergents

<div align="center">

![Project Euler](https://img.shields.io/badge/Project-Euler-6B4F2A?style=for-the-badge&logo=projecteuler&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Solved-success?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Math%20%C2%B7%20Continued%20Fractions%20&%20Recurrences-blue?style=for-the-badge)

</div>

---

## 📜 Problem Statement

In the first 1,000 expansions of the continued fraction for $\sqrt{2}$, how many fractions contain a numerator with more digits than the denominator?

🔗 **Project Euler Link:** [Problem 57](https://projecteuler.net/problem=57)

---

## 💡 Key Learnings & Mathematical Insights

- **Numerator & Denominator Recurrence**: $N_{k+1} = N_k + 2D_k$ and $D_{k+1} = N_k + D_k$.
- **Digit Count Comparison**: Directly check `len(str(N)) > len(str(D))` across 1000 iterations.

---

## 💻 Code Explanation

### 📄 `main.py`
- **Role / Purpose**: Solution implementation for Problem 57.
- **Key Logic**: Uses procedural script execution.
- **How It Works**:
  - Implements the mathematical formula and pruning rules described above.
  - Efficiently iterates through the search space and produces the final answer.

---

## ⏱️ Complexity Analysis

| Metric | Complexity | Description |
| :--- | :--- | :--- |
| **Time Complexity** | $O(K) \text{ where } K=1000$ | Fast execution adhering to Project Euler's 1-minute performance rule. |
| **Space Complexity** | $O(1)$ | Efficient memory allocation. |

---

## 🚀 How to Run

```bash
python3 main.py
```

**Verified Answer / Result:**
```text
153
```
