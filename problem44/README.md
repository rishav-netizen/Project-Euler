# 🧮 Project Euler Problem 44: Pentagon Numbers

<div align="center">

![Project Euler](https://img.shields.io/badge/Project-Euler-6B4F2A?style=for-the-badge&logo=projecteuler&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Solved-success?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Math%20%C2%B7%20Polygonal%20Numbers-blue?style=for-the-badge)

</div>

---

## 📜 Problem Statement

Find the pair of pentagonal numbers, $P_j$ and $P_k$, for which their sum and difference are pentagonal and $D = |P_k - P_j|$ is minimised.

🔗 **Project Euler Link:** [Problem 44](https://projecteuler.net/problem=44)

---

## 💡 Key Learnings & Mathematical Insights

- **Pentagonal Test Formula**: $P = \frac{n(3n-1)}{2} \iff n = \frac{1 + \sqrt{1 + 24P}}{6}$. Integer iff $(1 + \sqrt{1+24P}) \% 6 == 0$.
- **Search Loop**: Iterate $k=1,2,\dots$ and $j < k$ checking if $P_k - P_j$ and $P_k + P_j$ are both pentagonal.

---

## 💻 Code Explanation

### 📄 `main.py`
- **Role / Purpose**: Solution implementation for Problem 44.
- **Key Logic**: Defines functions: `P()`.
- **How It Works**:
  - Implements the mathematical formula and pruning rules described above.
  - Efficiently iterates through the search space and produces the final answer.

### 📄 `sample.py`
- **Role / Purpose**: Solution implementation for Problem 44 (Alternative / Optimized approach).
- **Key Logic**: Defines functions: `is_pent()` (imports: `math`).
- **How It Works**:
  - Implements the mathematical formula and pruning rules described above.
  - Efficiently iterates through the search space and produces the final answer.

---

## ⏱️ Complexity Analysis

| Metric | Complexity | Description |
| :--- | :--- | :--- |
| **Time Complexity** | $O(N^2)$ | Fast execution adhering to Project Euler's 1-minute performance rule. |
| **Space Complexity** | $O(N)$ | Efficient memory allocation. |

---

## 🚀 How to Run

```bash
python3 main.py
```

**Verified Answer / Result:**
```text
5482660
```
