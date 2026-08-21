# 🧮 Project Euler Problem 45: Triangular, Pentagonal, and Hexagonal

<div align="center">

![Project Euler](https://img.shields.io/badge/Project-Euler-6B4F2A?style=for-the-badge&logo=projecteuler&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Solved-success?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Math%20%C2%B7%20Polygonal%20Intersection-blue?style=for-the-badge)

</div>

---

## 📜 Problem Statement

Find the next triangle number after $T_{285} = 40755$ that is also pentagonal and hexagonal.

🔗 **Project Euler Link:** [Problem 45](https://projecteuler.net/problem=45)

---

## 💡 Key Learnings & Mathematical Insights

- **Hexagonal is a Subset of Triangular**: $H_m = m(2m-1) = T_{2m-1}$. Every hexagonal number is already triangular!
- **Pentagonal Test on Hexagonals**: Generate $H_m$ for $m > 143$ and test if $H_m$ is pentagonal.

---

## 💻 Code Explanation

### 📄 `main.py`
- **Role / Purpose**: Solution implementation for Problem 45.
- **Key Logic**: Defines functions: `T()`, `P()`, `H()`.
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
1533776805
```
