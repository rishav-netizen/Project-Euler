# 🧮 Project Euler Problem 69: Totient Maximum

<div align="center">

![Project Euler](https://img.shields.io/badge/Project-Euler-6B4F2A?style=for-the-badge&logo=projecteuler&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Solved-success?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Number%20Theory%20%C2%B7%20Euler's%20Totient%20Function-blue?style=for-the-badge)

</div>

---

## 📜 Problem Statement

Find the value of $n \le 1,000,000$ for which $n / \phi(n)$ is a maximum.

🔗 **Project Euler Link:** [Problem 69](https://projecteuler.net/problem=69)

---

## 💡 Key Learnings & Mathematical Insights

- **Totient Ratio Maximization**: $\frac{n}{\phi(n)} = \prod_{p | n} \frac{p}{p-1}$. The ratio grows with more distinct small prime factors.
- **Primorial**: The product of consecutive smallest primes: $2 \times 3 \times 5 \times 7 \times 11 \times 13 \times 17 = 510,510 \le 10^6$.

---

## 💻 Code Explanation

### 📄 `main.py`
- **Role / Purpose**: Solution implementation for Problem 69.
- **Key Logic**: Defines functions: `gcd()`, `relativePrime()`, `primesTill()`, `isPrime()`, `phi()`, `test()`, `bruteForce()`, `main()`.
- **How It Works**:
  - Implements the mathematical formula and pruning rules described above.
  - Efficiently iterates through the search space and produces the final answer.

---

## ⏱️ Complexity Analysis

| Metric | Complexity | Description |
| :--- | :--- | :--- |
| **Time Complexity** | $O(1)$ | Fast execution adhering to Project Euler's 1-minute performance rule. |
| **Space Complexity** | $O(1)$ | Efficient memory allocation. |

---

## 🚀 How to Run

```bash
python3 main.py
```

**Verified Answer / Result:**
```text
510510
```
