# 🧮 Project Euler Problem 58: Spiral Primes

<div align="center">

![Project Euler](https://img.shields.io/badge/Project-Euler-6B4F2A?style=for-the-badge&logo=projecteuler&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Solved-success?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Number%20Theory%20%C2%B7%20Spiral%20Diagonals%20&%20Primality-blue?style=for-the-badge)

</div>

---

## 📜 Problem Statement

Starting with 1 and spiralling outwards, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?

🔗 **Project Euler Link:** [Problem 58](https://projecteuler.net/problem=58)

---

## 💡 Key Learnings & Mathematical Insights

- **Corner Polynomials**: For side $s = 2k+1$, corners are $s^2, s^2-(s-1), s^2-2(s-1), s^2-3(s-1)$.
- **Composite Corner**: $s^2$ is never prime for $s > 1$. Only test the other 3 corners.

---

## 💻 Code Explanation

### 📄 `main.py`
- **Role / Purpose**: Solution implementation for Problem 58.
- **Key Logic**: Defines functions: `is_prime()`, `main()`.
- **How It Works**:
  - Implements the mathematical formula and pruning rules described above.
  - Efficiently iterates through the search space and produces the final answer.

---

## ⏱️ Complexity Analysis

| Metric | Complexity | Description |
| :--- | :--- | :--- |
| **Time Complexity** | $O(K \sqrt{N})$ | Fast execution adhering to Project Euler's 1-minute performance rule. |
| **Space Complexity** | $O(1)$ | Efficient memory allocation. |

---

## 🚀 How to Run

```bash
python3 main.py
```

**Verified Answer / Result:**
```text
26241
```
