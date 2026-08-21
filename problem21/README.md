# 🧮 Project Euler Problem 21: Amicable Numbers

<div align="center">

![Project Euler](https://img.shields.io/badge/Project-Euler-6B4F2A?style=for-the-badge&logo=projecteuler&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Solved-success?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Number%20Theory%20%C2%B7%20Proper%20Divisors-blue?style=for-the-badge)

</div>

---

## 📜 Problem Statement

Evaluate the sum of all the amicable numbers under 10000.

🔗 **Project Euler Link:** [Problem 21](https://projecteuler.net/problem=21)

---

## 💡 Key Learnings & Mathematical Insights

- **Amicable Pair**: $a \ne b$ such that $d(a) = b$ and $d(b) = a$, where $d(n)$ is the sum of proper divisors.
- **Divisor Precomputation**: Compute $d(n)$ in $O(\sqrt{n})$ for each $n < 10000$ and check reciprocity.

---

## 💻 Code Explanation

### 📄 `main.py`
- **Role / Purpose**: Solution implementation for Problem 21.
- **Key Logic**: Defines functions: `d()`.
- **How It Works**:
  - Implements the mathematical formula and pruning rules described above.
  - Efficiently iterates through the search space and produces the final answer.

---

## ⏱️ Complexity Analysis

| Metric | Complexity | Description |
| :--- | :--- | :--- |
| **Time Complexity** | $O(N \sqrt{N})$ | Fast execution adhering to Project Euler's 1-minute performance rule. |
| **Space Complexity** | $O(1) / O(N)$ | Efficient memory allocation. |

---

## 🚀 How to Run

```bash
python3 main.py
```

**Verified Answer / Result:**
```text
31626
```
