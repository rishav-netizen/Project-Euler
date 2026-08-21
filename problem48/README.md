# 🧮 Project Euler Problem 48: Self Powers

<div align="center">

![Project Euler](https://img.shields.io/badge/Project-Euler-6B4F2A?style=for-the-badge&logo=projecteuler&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Solved-success?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Math%20%C2%B7%20Modular%20Arithmetic-blue?style=for-the-badge)

</div>

---

## 📜 Problem Statement

Find the last ten digits of the series, $1^1 + 2^2 + 3^3 + \dots + 1000^{1000}$.

🔗 **Project Euler Link:** [Problem 48](https://projecteuler.net/problem=48)

---

## 💡 Key Learnings & Mathematical Insights

- **Modular Arithmetic**: $\sum_{n=1}^{1000} n^n \pmod{10^{10}}$.
- **`pow(n, n, 10**10)`**: Computes modular powers in $O(\log n)$ without big integer memory explosion.

---

## 💻 Code Explanation

### 📄 `main.py`
- **Role / Purpose**: Solution implementation for Problem 48.
- **Key Logic**: Uses procedural script execution.
- **How It Works**:
  - Implements the mathematical formula and pruning rules described above.
  - Efficiently iterates through the search space and produces the final answer.

---

## ⏱️ Complexity Analysis

| Metric | Complexity | Description |
| :--- | :--- | :--- |
| **Time Complexity** | $O(N \log N)$ | Fast execution adhering to Project Euler's 1-minute performance rule. |
| **Space Complexity** | $O(1)$ | Efficient memory allocation. |

---

## 🚀 How to Run

```bash
python3 main.py
```

**Verified Answer / Result:**
```text
9110846700
```
