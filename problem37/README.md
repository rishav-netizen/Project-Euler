# 🧮 Project Euler Problem 37: Truncatable Primes

<div align="center">

![Project Euler](https://img.shields.io/badge/Project-Euler-6B4F2A?style=for-the-badge&logo=projecteuler&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Solved-success?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Number%20Theory%20%C2%B7%20Primes%20&%20Branching%20Search-blue?style=for-the-badge)

</div>

---

## 📜 Problem Statement

Find the sum of the only eleven primes that are both truncatable from left to right and right to left (excluding 2, 3, 5, 7).

🔗 **Project Euler Link:** [Problem 37](https://projecteuler.net/problem=37)

---

## 💡 Key Learnings & Mathematical Insights

- **Prefix & Suffix Pruning**: Test all prefixes `str(n)[:i]` and suffixes `str(n)[i:]`.
- **Digit Filter**: Digits must come from $\{1, 3, 7, 9\}$ with $\{2, 3, 5, 7\}$ only allowed as the first digit.

---

## 💻 Code Explanation

### 📄 `main.py`
- **Role / Purpose**: Solution implementation for Problem 37.
- **Key Logic**: Defines functions: `primes_till()`, `isTruncable()`, `main()`.
- **How It Works**:
  - Implements the mathematical formula and pruning rules described above.
  - Efficiently iterates through the search space and produces the final answer.

---

## ⏱️ Complexity Analysis

| Metric | Complexity | Description |
| :--- | :--- | :--- |
| **Time Complexity** | $O(\text{search tree})$ | Fast execution adhering to Project Euler's 1-minute performance rule. |
| **Space Complexity** | $O(N)$ | Efficient memory allocation. |

---

## 🚀 How to Run

```bash
python3 main.py
```

**Verified Answer / Result:**
```text
748317
```
