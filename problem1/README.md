# 🧮 Project Euler Problem 1: Multiples of 3 or 5

<div align="center">

![Project Euler](https://img.shields.io/badge/Project-Euler-6B4F2A?style=for-the-badge&logo=projecteuler&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Solved-success?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Math%20%C2%B7%20Arithmetic%20Progressions-blue?style=for-the-badge)

</div>

---

## 📜 Problem Statement

Find the sum of all the multiples of 3 or 5 below 1000.

🔗 **Project Euler Link:** [Problem 1](https://projecteuler.net/problem=1)

---

## 💡 Key Learnings & Mathematical Insights

- **Inclusion-Exclusion Principle**: Multiples of 15 (LCM of 3 and 5) are counted twice if summing multiples of 3 and 5 independently: $\text{Sum} = S(3) + S(5) - S(15)$.
- **Closed-Form Arithmetic Series**: The sum of multiples of $k$ up to $N$ is $k \cdot \frac{p(p+1)}{2}$ where $p = \lfloor \frac{N-1}{k} \rfloor$. Computes in $O(1)$ constant time vs $O(N)$ iteration.

---

## 💻 Code Explanation

### 📄 `better.py`
- **Role / Purpose**: Solution implementation for Problem 1 (Alternative / Optimized approach).
- **Key Logic**: Defines functions: `SumDivisibleBy()`.
- **How It Works**:
  - Implements the mathematical formula and pruning rules described above.
  - Efficiently iterates through the search space and produces the final answer.

### 📄 `main.py`
- **Role / Purpose**: Solution implementation for Problem 1.
- **Key Logic**: Uses procedural script execution.
- **How It Works**:
  - Implements the mathematical formula and pruning rules described above.
  - Efficiently iterates through the search space and produces the final answer.

---

## ⏱️ Complexity Analysis

| Metric | Complexity | Description |
| :--- | :--- | :--- |
| **Time Complexity** | $O(1) \text{ with arithmetic series } / O(N) \text{ loop}$ | Fast execution adhering to Project Euler's 1-minute performance rule. |
| **Space Complexity** | $O(1)$ | Efficient memory allocation. |

---

## 🚀 How to Run

```bash
python3 better.py
```

**Verified Answer / Result:**
```text
233168
```
