# 🧮 Project Euler Problem 16: Power Digit Sum

<div align="center">

![Project Euler](https://img.shields.io/badge/Project-Euler-6B4F2A?style=for-the-badge&logo=projecteuler&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Solved-success?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Math%20%C2%B7%20Big%20Integers-blue?style=for-the-badge)

</div>

---

## 📜 Problem Statement

What is the sum of the digits of the number $2^{1000}$?

🔗 **Project Euler Link:** [Problem 16](https://projecteuler.net/problem=16)

---

## 💡 Key Learnings & Mathematical Insights

- **Arbitrary Precision Exponentiation**: $2^{1000}$ is computed efficiently using fast binary exponentiation.
- **Digit Sum Reduction**: Convert the resulting 302-digit integer to string and sum each digit: `sum(int(c) for c in str(2**1000))`.

---

## 💻 Code Explanation

### 📄 `main.py`
- **Role / Purpose**: Solution implementation for Problem 16.
- **Key Logic**: Uses procedural script execution.
- **How It Works**:
  - Implements the mathematical formula and pruning rules described above.
  - Efficiently iterates through the search space and produces the final answer.

---

## ⏱️ Complexity Analysis

| Metric | Complexity | Description |
| :--- | :--- | :--- |
| **Time Complexity** | $O(\log(\text{exp}))$ | Fast execution adhering to Project Euler's 1-minute performance rule. |
| **Space Complexity** | $O(D) \text{ where } D \approx 302$ | Efficient memory allocation. |

---

## 🚀 How to Run

```bash
python3 main.py
```

**Verified Answer / Result:**
```text
1366
```
