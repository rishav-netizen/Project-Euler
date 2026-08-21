# 🧮 Project Euler Problem 33: Digit Cancelling Fractions

<div align="center">

![Project Euler](https://img.shields.io/badge/Project-Euler-6B4F2A?style=for-the-badge&logo=projecteuler&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Solved-success?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Math%20%C2%B7%20Fractions%20&%20Simplifying-blue?style=for-the-badge)

</div>

---

## 📜 Problem Statement

Discover all four non-trivial fractions less than one in value, containing two digits in the numerator and denominator, which cancel incorrectly to the correct value. Find the value of the denominator in lowest terms.

🔗 **Project Euler Link:** [Problem 33](https://projecteuler.net/problem=33)

---

## 💡 Key Learnings & Mathematical Insights

- **Algebraic Cancellation**: For $10 \le n < d < 100$, check if dropping common digits gives equal ratio: $\frac{10a+b}{10b+c} = \frac{a}{c} \iff (10a+b)c = (10b+c)a$.
- **Lowest Terms**: Multiply all four fractions and divide total denominator by $\gcd(\text{product\_num}, \text{product\_den})$.

---

## 💻 Code Explanation

### 📄 `main.py`
- **Role / Purpose**: Solution implementation for Problem 33.
- **Key Logic**: Uses procedural script execution.
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
100
```
