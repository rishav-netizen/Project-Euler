# 🧮 Project Euler Problem 87: Prime Power Triples

<div align="center">

![Project Euler](https://img.shields.io/badge/Project-Euler-6B4F2A?style=for-the-badge&logo=projecteuler&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Solved-success?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Number%20Theory%20%C2%B7%20Primes%20&%20Combinations-blue?style=for-the-badge)

</div>

---

## 📜 Problem Statement

How many numbers below fifty million can be expressed as the sum of a prime square, prime cube, and prime fourth power ($p_1^2 + p_2^3 + p_3^4 < 50,000,000$)?

🔗 **Project Euler Link:** [Problem 87](https://projecteuler.net/problem=87)

---

## 💡 Key Learnings & Mathematical Insights

- **Bound Derivations**: $p_1 < \sqrt{50M} \approx 7071$, $p_2 < \sqrt[3]{50M} \approx 368$, $p_3 < \sqrt[4]{50M} \approx 84$.
- **Bitset / Set Accumulation**: Iterate nested loops over small prime lists and record unique valid sums.

---

## 💻 Code Explanation

### 📄 `main.py`
- **Role / Purpose**: Solution implementation for Problem 87.
- **Key Logic**: Defines functions: `primesTill()`, `main()`.
- **How It Works**:
  - Implements the mathematical formula and pruning rules described above.
  - Efficiently iterates through the search space and produces the final answer.

---

## ⏱️ Complexity Analysis

| Metric | Complexity | Description |
| :--- | :--- | :--- |
| **Time Complexity** | $O(|P_1| \cdot |P_2| \cdot |P_3|)$ | Fast execution adhering to Project Euler's 1-minute performance rule. |
| **Space Complexity** | $O(N)$ | Efficient memory allocation. |

---

## 🚀 How to Run

```bash
python3 main.py
```

**Verified Answer / Result:**
```text
1097343
```
