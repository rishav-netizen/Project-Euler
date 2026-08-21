# 🧮 Project Euler Problem 49: Prime Permutations

<div align="center">

![Project Euler](https://img.shields.io/badge/Project-Euler-6B4F2A?style=for-the-badge&logo=projecteuler&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Solved-success?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Number%20Theory%20%C2%B7%20Arithmetic%20Progressions-blue?style=for-the-badge)

</div>

---

## 📜 Problem Statement

Find the 4-digit arithmetic sequence of 3 prime numbers which are permutations of each other (other than 1487, 4817, 8147).

🔗 **Project Euler Link:** [Problem 49](https://projecteuler.net/problem=49)

---

## 💡 Key Learnings & Mathematical Insights

- **Signature Hash Bucketing**: Group 4-digit primes by sorted digits string `"".join(sorted(str(p)))`.
- **AP Search**: Search triplets in each bucket for $p_3 - p_2 == p_2 - p_1$.

---

## 💻 Code Explanation

### 📄 `better.py`
- **Role / Purpose**: Solution implementation for Problem 49 (Alternative / Optimized approach).
- **Key Logic**: Defines functions: `primes_between()`, `isItAp()`, `segregator()`, `tripletMaker()`, `result()`.
- **How It Works**:
  - Implements the mathematical formula and pruning rules described above.
  - Efficiently iterates through the search space and produces the final answer.

### 📄 `fun.py`
- **Role / Purpose**: Solution implementation for Problem 49 (Alternative / Optimized approach).
- **Key Logic**: Uses procedural script execution.
- **How It Works**:
  - Implements the mathematical formula and pruning rules described above.
  - Efficiently iterates through the search space and produces the final answer.

### 📄 `main.py`
- **Role / Purpose**: Solution implementation for Problem 49.
- **Key Logic**: Defines functions: `primes_between()`, `isItAp()`, `segregator()`, `tripletMaker()`, `result()`.
- **How It Works**:
  - Implements the mathematical formula and pruning rules described above.
  - Efficiently iterates through the search space and produces the final answer.

---

## ⏱️ Complexity Analysis

| Metric | Complexity | Description |
| :--- | :--- | :--- |
| **Time Complexity** | $O(P \log P)$ | Fast execution adhering to Project Euler's 1-minute performance rule. |
| **Space Complexity** | $O(P)$ | Efficient memory allocation. |

---

## 🚀 How to Run

```bash
python3 better.py
```

**Verified Answer / Result:**
```text
296962999629
```
