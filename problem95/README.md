# 🧮 Project Euler Problem 95: Amicable Chains

<div align="center">

![Project Euler](https://img.shields.io/badge/Project-Euler-6B4F2A?style=for-the-badge&logo=projecteuler&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Solved-success?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Graph%20Theory%20%C2%B7%20Functional%20Graphs%20&%20Cycle%20Detection-blue?style=for-the-badge)

</div>

---

## 📜 Problem Statement

Find the smallest member of the longest amicable chain with no element exceeding one million.

🔗 **Project Euler Link:** [Problem 95](https://projecteuler.net/problem=95)

---

## 💡 Key Learnings & Mathematical Insights

- **Proper Divisor Sieve**: Compute proper divisor sums for all $n \le 10^6$ in $O(N \log N)$ using a divisor sieve.
- **Cycle Detection**: Follow directed edges $n \to \sigma(n) - n$ while detecting loops and tracking visited elements.

---

## 💻 Code Explanation

### 📄 `main.py`
- **Role / Purpose**: Solution implementation for Problem 95.
- **Key Logic**: Defines functions: `sumOfProperDivisorsOf()`, `amicableChainLength()`, `minMember()`, `main()`.
- **How It Works**:
  - Implements the mathematical formula and pruning rules described above.
  - Efficiently iterates through the search space and produces the final answer.

---

## ⏱️ Complexity Analysis

| Metric | Complexity | Description |
| :--- | :--- | :--- |
| **Time Complexity** | $O(N \log N)$ | Fast execution adhering to Project Euler's 1-minute performance rule. |
| **Space Complexity** | $O(N)$ | Efficient memory allocation. |

---

## 🚀 How to Run

```bash
python3 main.py
```

**Verified Answer / Result:**
```text
14316
```
