# 🧮 Project Euler Problem 104: Pandigital Fibonacci Ends

<div align="center">

![Project Euler](https://img.shields.io/badge/Project-Euler-6B4F2A?style=for-the-badge&logo=projecteuler&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Solved-success?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Number%20Theory%20%C2%B7%20Fibonacci%20&%20Golden%20Ratio%20Logarithms-blue?style=for-the-badge)

</div>

---

## 📜 Problem Statement

Given that $F_k$ is the first Fibonacci number for which the first nine digits AND the last nine digits are 1-9 pandigital, find $k$.

🔗 **Project Euler Link:** [Problem 104](https://projecteuler.net/problem=104)

---

## 💡 Key Learnings & Mathematical Insights

- **Last 9 Digits via Modulo**: Generate $F_k \pmod{10^9}$ sequentially. Only when the last 9 digits are pandigital do we test the first 9 digits.
- **Leading 9 Digits via Binet's Formula**: $\log_{10}(F_k) \approx k \log_{10}(\phi) - \frac{1}{2}\log_{10}(5)$. Extract fractional part $t = \{ \log_{10}(F_k) \}$ and compute $\lfloor 10^{t + 8} \rfloor$.

---

## 💻 Code Explanation

### 📄 `main.py`
- **Role / Purpose**: Solution implementation for Problem 104.
- **Key Logic**: Defines functions: `solve()`, `isPandigital()`, `main()` (imports: `math`).
- **How It Works**:
  - Implements the mathematical formula and pruning rules described above.
  - Efficiently iterates through the search space and produces the final answer.

---

## ⏱️ Complexity Analysis

| Metric | Complexity | Description |
| :--- | :--- | :--- |
| **Time Complexity** | $O(K)$ | Fast execution adhering to Project Euler's 1-minute performance rule. |
| **Space Complexity** | $O(1)$ | Efficient memory allocation. |

---

## 🚀 How to Run

```bash
python3 main.py
```

**Verified Answer / Result:**
```text
329468
```
