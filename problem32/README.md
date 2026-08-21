# 🧮 Project Euler Problem 32: Pandigital Products

<div align="center">

![Project Euler](https://img.shields.io/badge/Project-Euler-6B4F2A?style=for-the-badge&logo=projecteuler&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Solved-success?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Search%20%C2%B7%20Pandigital%20Numbers-blue?style=for-the-badge)

</div>

---

## 📜 Problem Statement

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

🔗 **Project Euler Link:** [Problem 32](https://projecteuler.net/problem=32)

---

## 💡 Key Learnings & Mathematical Insights

- **Digit Partitioning**: $A \times B = C$ where $\text{len}(A) + \text{len}(B) + \text{len}(C) = 9$. Only partitions are $1 \times 4 = 4$ digits and $2 \times 3 = 4$ digits.
- **Set Collection**: Products can be produced by multiple valid multiplier pairs; collect products in a set to avoid double-counting.

---

## 💻 Code Explanation

### 📄 `main.py`
- **Role / Purpose**: Solution implementation for Problem 32.
- **Key Logic**: Defines functions: `isPandigitalProduct()`, `main()`.
- **How It Works**:
  - Implements the mathematical formula and pruning rules described above.
  - Efficiently iterates through the search space and produces the final answer.

---

## ⏱️ Complexity Analysis

| Metric | Complexity | Description |
| :--- | :--- | :--- |
| **Time Complexity** | $O(\text{search})$ | Fast execution adhering to Project Euler's 1-minute performance rule. |
| **Space Complexity** | $O(\text{products})$ | Efficient memory allocation. |

---

## 🚀 How to Run

```bash
python3 main.py
```

**Verified Answer / Result:**
```text
45228
```
