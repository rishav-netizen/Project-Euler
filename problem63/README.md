# 🧮 Project Euler Problem 63: Powerful Digit Counts

<div align="center">

![Project Euler](https://img.shields.io/badge/Project-Euler-6B4F2A?style=for-the-badge&logo=projecteuler&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Solved-success?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Math%20%C2%B7%20Logarithms%20&%20Digit%20Length%20Bounds-blue?style=for-the-badge)

</div>

---

## 📜 Problem Statement

How many $n$-digit positive integers exist which are also an $n$-th power?

🔗 **Project Euler Link:** [Problem 63](https://projecteuler.net/problem=63)

---

## 💡 Key Learnings & Mathematical Insights

- **Base Bound**: Base $x$ must satisfy $1 \le x \le 9$ (since $10^n$ has $n+1$ digits).
- **Exponent Bound**: $10^{n-1} \le x^n \implies n(1 - \log_{10}(x)) \le 1 \implies n \le \lfloor \frac{1}{1 - \log_{10}(x)} \rfloor$.

---

## 💻 Code Explanation

### 📄 `main.py`
- **Role / Purpose**: Solution implementation for Problem 63.
- **Key Logic**: Uses procedural script execution (imports: `math`).
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
49
```
