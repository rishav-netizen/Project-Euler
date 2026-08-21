# 🧮 Project Euler Problem 38: Pandigital Multiples

<div align="center">

![Project Euler](https://img.shields.io/badge/Project-Euler-6B4F2A?style=for-the-badge&logo=projecteuler&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Solved-success?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Search%20%C2%B7%20Concatenated%20Multiples-blue?style=for-the-badge)

</div>

---

## 📜 Problem Statement

What is the largest 1 to 9 pandigital 9-digit number formed as the concatenated product of an integer with $(1, 2, \dots, n)$ where $n > 1$?

🔗 **Project Euler Link:** [Problem 38](https://projecteuler.net/problem=38)

---

## 💡 Key Learnings & Mathematical Insights

- **Leading Digit Bounds**: Known candidate starts with 9 ($9 \times (1..5) = 918273645$). Best candidate must start with 9.
- **4-digit Multiplicand**: For $n=2$, a 4-digit number $9xxx \times 1 = 4$ digits, $9xxx \times 2 = 5$ digits $\implies 9$ digits total. Search $9123 \le k \le 9876$.

---

## 💻 Code Explanation

### 📄 `main.py`
- **Role / Purpose**: Solution implementation for Problem 38.
- **Key Logic**: Defines functions: `isPandigital()`, `concatenator()`, `largestPandigital()`.
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
932718654
```
