# 🧮 Project Euler Problem 60: Prime Pair Sets

<div align="center">

![Project Euler](https://img.shields.io/badge/Project-Euler-6B4F2A?style=for-the-badge&logo=projecteuler&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Solved-success?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Graph%20Theory%20%C2%B7%20Cliques%20&%20Prime%20Concatenation-blue?style=for-the-badge)

</div>

---

## 📜 Problem Statement

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime in both orders.

🔗 **Project Euler Link:** [Problem 60](https://projecteuler.net/problem=60)

---

## 💡 Key Learnings & Mathematical Insights

- **Compatibility Graph**: Edge between $p_1, p_2$ if $\text{isPrime}(p_1 \circ p_2)$ and $\text{isPrime}(p_2 \circ p_1)$.
- **5-Clique Finding**: Find a 5-clique with minimum sum via recursive set intersections.

---

## 💻 Code Explanation

### 📄 `main.py`
- **Role / Purpose**: Solution implementation for Problem 60.
- **Key Logic**: Defines functions: `primes_till()`, `isPrime()`, `is_valid_pair()`, `main()`.
- **How It Works**:
  - Implements the mathematical formula and pruning rules described above.
  - Efficiently iterates through the search space and produces the final answer.

---

## ⏱️ Complexity Analysis

| Metric | Complexity | Description |
| :--- | :--- | :--- |
| **Time Complexity** | $O(V^5) \text{ heavily pruned}$ | Fast execution adhering to Project Euler's 1-minute performance rule. |
| **Space Complexity** | $O(V^2)$ | Efficient memory allocation. |

---

## 🚀 How to Run

```bash
python3 main.py
```

**Verified Answer / Result:**
```text
26033
```
