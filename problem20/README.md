# 🧮 Project Euler Problem 20: Factorial Digit Sum

<div align="center">

![Project Euler](https://img.shields.io/badge/Project-Euler-6B4F2A?style=for-the-badge&logo=projecteuler&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Solved-success?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Math%20%C2%B7%20Big%20Integers-blue?style=for-the-badge)

</div>

---

## 📜 Problem Statement

Find the sum of the digits in the number $100!$.

🔗 **Project Euler Link:** [Problem 20](https://projecteuler.net/problem=20)

---

## 💡 Key Learnings & Mathematical Insights

- **Exact BigInt Factorial**: $100!$ produces a 158-digit number.
- **Digit Sum**: `sum(int(d) for d in str(math.factorial(100)))`.

---

## 💻 Code Explanation

### 📄 `main.py`
- **Role / Purpose**: Solution implementation for Problem 20.
- **Key Logic**: Defines functions: `factDigitSum()` (imports: `math`).
- **How It Works**:
  - Implements the mathematical formula and pruning rules described above.
  - Efficiently iterates through the search space and produces the final answer.

---

## ⏱️ Complexity Analysis

| Metric | Complexity | Description |
| :--- | :--- | :--- |
| **Time Complexity** | $O(N \log N)$ | Fast execution adhering to Project Euler's 1-minute performance rule. |
| **Space Complexity** | $O(D) \text{ where } D \approx 158$ | Efficient memory allocation. |

---

## 🚀 How to Run

```bash
python3 main.py
```

**Verified Answer / Result:**
```text
648
```
