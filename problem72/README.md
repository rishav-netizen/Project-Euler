# 🧮 Project Euler Problem 72: Counting Fractions

<div align="center">

![Project Euler](https://img.shields.io/badge/Project-Euler-6B4F2A?style=for-the-badge&logo=projecteuler&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Solved-success?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Number%20Theory%20%C2%B7%20Farey%20Sequences%20&%20Totient%20Sieve-blue?style=for-the-badge)

</div>

---

## 📜 Problem Statement

How many elements would be contained in the set of proper reduced fractions for $d \le 1,000,000$?

🔗 **Project Euler Link:** [Problem 72](https://projecteuler.net/problem=72)

---

## 💡 Key Learnings & Mathematical Insights

- **Sum of Euler's Totient**: The number of reduced fractions with denominator $d$ is $\phi(d)$. Total $= \sum_{d=2}^{10^6} \phi(d)$.
- **Totient Sieve**: Computes all $\phi(d)$ up to $10^6$ in $O(N \log \log N)$.

---

## 💻 Code Explanation

### 📄 `main.py`
- **Role / Purpose**: Solution implementation for Problem 72.
- **Key Logic**: Defines functions: `TotientSieveSum()`, `main()`.
- **How It Works**:
  - Implements the mathematical formula and pruning rules described above.
  - Efficiently iterates through the search space and produces the final answer.

---

## ⏱️ Complexity Analysis

| Metric | Complexity | Description |
| :--- | :--- | :--- |
| **Time Complexity** | $O(N \log \log N)$ | Fast execution adhering to Project Euler's 1-minute performance rule. |
| **Space Complexity** | $O(N)$ | Efficient memory allocation. |

---

## 🚀 How to Run

```bash
python3 main.py
```

**Verified Answer / Result:**
```text
303963552391
```
