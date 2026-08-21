# 🧮 Project Euler Problem 10: Summation of Primes

<div align="center">

![Project Euler](https://img.shields.io/badge/Project-Euler-6B4F2A?style=for-the-badge&logo=projecteuler&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Solved-success?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Number%20Theory%20%C2%B7%20Sieve%20of%20Eratosthenes-blue?style=for-the-badge)

</div>

---

## 📜 Problem Statement

Find the sum of all the primes below two million.

🔗 **Project Euler Link:** [Problem 10](https://projecteuler.net/problem=10)

---

## 💡 Key Learnings & Mathematical Insights

- **Sieve of Eratosthenes**: Creates a boolean array up to $N = 2,000,000$ and crosses off composite multiples, operating in $O(N \log \log N)$ time.
- **Trial Division**: Testing odds up to $\sqrt{n}$ also terminates within seconds.

---

## 💻 Code Explanation

### 📄 `main.py`
- **Role / Purpose**: Solution implementation for Problem 10.
- **Key Logic**: Defines functions: `isPrime()`.
- **How It Works**:
  - Implements the mathematical formula and pruning rules described above.
  - Efficiently iterates through the search space and produces the final answer.

---

## ⏱️ Complexity Analysis

| Metric | Complexity | Description |
| :--- | :--- | :--- |
| **Time Complexity** | $O(N \sqrt{N}) \text{ trial division } / O(N \log \log N) \text{ sieve}$ | Fast execution adhering to Project Euler's 1-minute performance rule. |
| **Space Complexity** | $O(1) / O(N)$ | Efficient memory allocation. |

---

## 🚀 How to Run

```bash
python3 main.py
```

**Verified Answer / Result:**
```text
142913828922
```
