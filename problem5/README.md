# 🧮 Project Euler Problem 5: Smallest Multiple

<div align="center">

![Project Euler](https://img.shields.io/badge/Project-Euler-6B4F2A?style=for-the-badge&logo=projecteuler&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Solved-success?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Number%20Theory%20%C2%B7%20LCM%20&%20GCD-blue?style=for-the-badge)

</div>

---

## 📜 Problem Statement

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

🔗 **Project Euler Link:** [Problem 5](https://projecteuler.net/problem=5)

---

## 💡 Key Learnings & Mathematical Insights

- **Prime Power Decomposition**: The least common multiple $\text{LCM}(1, 2, \dots, 20)$ is the product of the highest prime powers $\le 20$: $2^4 \times 3^2 \times 5^1 \times 7^1 \times 11^1 \times 13^1 \times 17^1 \times 19^1 = 232,792,560$.
- **GCD-based LCM**: Alternatively, compute iteratively using $\text{LCM}(a, b) = \frac{a \times b}{\gcd(a, b)}$.

---

## 💻 Code Explanation

### 📄 `main.py`
- **Role / Purpose**: Solution implementation for Problem 5.
- **Key Logic**: Uses procedural script execution.
- **How It Works**:
  - Implements the mathematical formula and pruning rules described above.
  - Efficiently iterates through the search space and produces the final answer.

---

## ⏱️ Complexity Analysis

| Metric | Complexity | Description |
| :--- | :--- | :--- |
| **Time Complexity** | $O(N \log N) / O(1)$ | Fast execution adhering to Project Euler's 1-minute performance rule. |
| **Space Complexity** | $O(1)$ | Efficient memory allocation. |

---

## 🚀 How to Run

```bash
python3 main.py
```

**Verified Answer / Result:**
```text
232792560
```
