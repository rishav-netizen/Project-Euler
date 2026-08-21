# 🧮 Project Euler Problem 42: Coded Triangle Numbers

<div align="center">

![Project Euler](https://img.shields.io/badge/Project-Euler-6B4F2A?style=for-the-badge&logo=projecteuler&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Solved-success?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Word%20Scoring%20%C2%B7%20Quadratic%20Formula-blue?style=for-the-badge)

</div>

---

## 📜 Problem Statement

Using a 2000-word file, how many words are triangle words (where word value is a triangle number $t_n = \frac{1}{2}n(n+1)$)?

🔗 **Project Euler Link:** [Problem 42](https://projecteuler.net/problem=42)

---

## 💡 Key Learnings & Mathematical Insights

- **Inverse Triangle Test**: $t_n = \frac{n(n+1)}{2} \iff 8t + 1 = (2n+1)^2$. $x$ is triangular iff $\sqrt{8x+1}$ is an integer.
- **Precomputed Triangle Set**: Max word score is small ($< 500$), so test membership in a set of precomputed triangle numbers.

---

## 💻 Code Explanation

### 📄 `main.py`
- **Role / Purpose**: Solution implementation for Problem 42.
- **Key Logic**: Defines functions: `triangleNumber()`, `wordValue()`.
- **How It Works**:
  - Implements the mathematical formula and pruning rules described above.
  - Efficiently iterates through the search space and produces the final answer.

---

## ⏱️ Complexity Analysis

| Metric | Complexity | Description |
| :--- | :--- | :--- |
| **Time Complexity** | $O(W \cdot L)$ | Fast execution adhering to Project Euler's 1-minute performance rule. |
| **Space Complexity** | $O(1)$ | Efficient memory allocation. |

---

## 🚀 How to Run

```bash
python3 main.py
```

**Verified Answer / Result:**
```text
162
```
