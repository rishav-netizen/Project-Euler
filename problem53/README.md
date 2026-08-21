# 🧮 Project Euler Problem 53: Combinatoric Selections

<div align="center">

![Project Euler](https://img.shields.io/badge/Project-Euler-6B4F2A?style=for-the-badge&logo=projecteuler&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Solved-success?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Combinatorics%20%C2%B7%20Pascal's%20Triangle%20Symmetry-blue?style=for-the-badge)

</div>

---

## 📜 Problem Statement

How many values of $\binom{n}{r}$, for $1 \le n \le 100$, are greater than one-million?

🔗 **Project Euler Link:** [Problem 53](https://projecteuler.net/problem=53)

---

## 💡 Key Learnings & Mathematical Insights

- **Pascal Symmetry**: $\binom{n}{r} = \binom{n}{n-r}$.
- **Early Stopping**: Find the first $r$ where $\binom{n}{r} > 10^6$; then all values between $r$ and $n-r$ are also $> 10^6$, adding $(n - 2r + 1)$ to total.

---

## 💻 Code Explanation

### 📄 `main.py`
- **Role / Purpose**: Solution implementation for Problem 53.
- **Key Logic**: Uses procedural script execution (imports: `math`).
- **How It Works**:
  - Implements the mathematical formula and pruning rules described above.
  - Efficiently iterates through the search space and produces the final answer.

---

## ⏱️ Complexity Analysis

| Metric | Complexity | Description |
| :--- | :--- | :--- |
| **Time Complexity** | $O(N^2) / O(N)$ | Fast execution adhering to Project Euler's 1-minute performance rule. |
| **Space Complexity** | $O(1)$ | Efficient memory allocation. |

---

## 🚀 How to Run

```bash
python3 main.py
```

**Verified Answer / Result:**
```text
4075
```
