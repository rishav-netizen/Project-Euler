# 🧮 Project Euler Problem 80: Square Root Digital Expansion

<div align="center">

![Project Euler](https://img.shields.io/badge/Project-Euler-6B4F2A?style=for-the-badge&logo=projecteuler&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Solved-success?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Math%20%C2%B7%20High%20Precision%20Square%20Roots-blue?style=for-the-badge)

</div>

---

## 📜 Problem Statement

For the first one hundred natural numbers, find the total of the digital sums of the first one hundred decimal digits for all irrational square roots.

🔗 **Project Euler Link:** [Problem 80](https://projecteuler.net/problem=80)

---

## 💡 Key Learnings & Mathematical Insights

- **Integer Scaling**: Multiply $N$ by $10^{200}$ and compute $\lfloor \sqrt{N \cdot 10^{200}} \rfloor = \lfloor \sqrt{N} \cdot 10^{100} \rfloor$.
- **Sum Leading 100 Digits**: Skip perfect squares and sum the first 100 digits.

---

## 💻 Code Explanation

### 📄 `better.py`
- **Role / Purpose**: Solution implementation for Problem 80 (Alternative / Optimized approach).
- **Key Logic**: Defines functions: `isPerfectSquare()`, `digitalSumOf()`, `main()` (imports: `math`).
- **How It Works**:
  - Implements the mathematical formula and pruning rules described above.
  - Efficiently iterates through the search space and produces the final answer.

### 📄 `main.py`
- **Role / Purpose**: Solution implementation for Problem 80.
- **Key Logic**: Defines functions: `isPerfectSquare()`, `digitalSumOf()`, `main()` (imports: `math, decimal`).
- **How It Works**:
  - Implements the mathematical formula and pruning rules described above.
  - Efficiently iterates through the search space and produces the final answer.

---

## ⏱️ Complexity Analysis

| Metric | Complexity | Description |
| :--- | :--- | :--- |
| **Time Complexity** | $O(N \cdot \text{isqrt})$ | Fast execution adhering to Project Euler's 1-minute performance rule. |
| **Space Complexity** | $O(1)$ | Efficient memory allocation. |

---

## 🚀 How to Run

```bash
python3 better.py
```

**Verified Answer / Result:**
```text
40886
```
