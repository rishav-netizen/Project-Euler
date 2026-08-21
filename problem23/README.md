# 🧮 Project Euler Problem 23: Non-Abundant Sums

<div align="center">

![Project Euler](https://img.shields.io/badge/Project-Euler-6B4F2A?style=for-the-badge&logo=projecteuler&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Solved-success?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Number%20Theory%20%C2%B7%20Abundant%20Numbers-blue?style=for-the-badge)

</div>

---

## 📜 Problem Statement

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

🔗 **Project Euler Link:** [Problem 23](https://projecteuler.net/problem=23)

---

## 💡 Key Learnings & Mathematical Insights

- **Abundant Classification**: $n$ is abundant if proper divisor sum $d(n) > n$.
- **Pairwise Sum Sieve**: Find all abundant numbers up to limit 28,123. Mark all pairwise sums $a+b \le 28123$ in a boolean array, then sum unmarked indices.

---

## 💻 Code Explanation

### 📄 `main.py`
- **Role / Purpose**: Solution implementation for Problem 23.
- **Key Logic**: Defines functions: `sumOfProperDivisors()`, `isAbundant()`.
- **How It Works**:
  - Implements the mathematical formula and pruning rules described above.
  - Efficiently iterates through the search space and produces the final answer.

---

## ⏱️ Complexity Analysis

| Metric | Complexity | Description |
| :--- | :--- | :--- |
| **Time Complexity** | $O(A^2) \text{ where } A \approx 6965$ | Fast execution adhering to Project Euler's 1-minute performance rule. |
| **Space Complexity** | $O(N)$ | Efficient memory allocation. |

---

## 🚀 How to Run

```bash
python3 main.py
```

**Verified Answer / Result:**
```text
4179871
```
