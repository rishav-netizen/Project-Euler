# 🧮 Project Euler Problem 25: 1000-digit Fibonacci Number

<div align="center">

![Project Euler](https://img.shields.io/badge/Project-Euler-6B4F2A?style=for-the-badge&logo=projecteuler&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Solved-success?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Math%20%C2%B7%20Binet's%20Formula%20&%20Logarithms-blue?style=for-the-badge)

</div>

---

## 📜 Problem Statement

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

🔗 **Project Euler Link:** [Problem 25](https://projecteuler.net/problem=25)

---

## 💡 Key Learnings & Mathematical Insights

- **Binet Logarithmic Formula**: $F_n \approx \frac{\phi^n}{\sqrt{5}} \implies n \log_{10}(\phi) - \frac{1}{2}\log_{10}(5) \ge 999$. Solving gives $n = \lceil \frac{999 + 0.5\log_{10}(5)}{\log_{10}(\phi)} \rceil = 4782$.
- **Iterative BigInt Simulation**: Loop until `len(str(fn)) == 1000`.

---

## 💻 Code Explanation

### 📄 `main.py`
- **Role / Purpose**: Solution implementation for Problem 25.
- **Key Logic**: Defines functions: `F()`.
- **How It Works**:
  - Implements the mathematical formula and pruning rules described above.
  - Efficiently iterates through the search space and produces the final answer.

---

## ⏱️ Complexity Analysis

| Metric | Complexity | Description |
| :--- | :--- | :--- |
| **Time Complexity** | $O(N) / O(1)$ | Fast execution adhering to Project Euler's 1-minute performance rule. |
| **Space Complexity** | $O(1)$ | Efficient memory allocation. |

---

## 🚀 How to Run

```bash
python3 main.py
```

**Verified Answer / Result:**
```text
4782
```
