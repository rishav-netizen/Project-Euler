# 🧮 Project Euler Problem 78: Coin Partitions

<div align="center">

![Project Euler](https://img.shields.io/badge/Project-Euler-6B4F2A?style=for-the-badge&logo=projecteuler&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Solved-success?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Number%20Theory%20%C2%B7%20Euler's%20Pentagonal%20Number%20Theorem-blue?style=for-the-badge)

</div>

---

## 📜 Problem Statement

Find the least value of $n$ for which $p(n)$ is divisible by one million.

🔗 **Project Euler Link:** [Problem 78](https://projecteuler.net/problem=78)

---

## 💡 Key Learnings & Mathematical Insights

- **Pentagonal Number Theorem**: $p(n) = \sum_{k \ne 0} (-1)^{k-1} p(n - g_k)$ where $g_k = \frac{k(3k-1)}{2}$.
- **Modulo 1,000,000**: Retain values modulo $10^6$ to keep operations ultra-fast in $O(N \sqrt{N})$.

---

## 💻 Code Explanation

### 📄 `main.py`
- **Role / Purpose**: Solution implementation for Problem 78.
- **Key Logic**: Defines functions: `main()`.
- **How It Works**:
  - Implements the mathematical formula and pruning rules described above.
  - Efficiently iterates through the search space and produces the final answer.

---

## ⏱️ Complexity Analysis

| Metric | Complexity | Description |
| :--- | :--- | :--- |
| **Time Complexity** | $O(N \sqrt{N})$ | Fast execution adhering to Project Euler's 1-minute performance rule. |
| **Space Complexity** | $O(N)$ | Efficient memory allocation. |

---

## 🚀 How to Run

```bash
python3 main.py
```

**Verified Answer / Result:**
```text
55374
```
