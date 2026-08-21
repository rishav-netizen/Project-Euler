# 🧮 Project Euler Problem 8: Largest Product in a Series

<div align="center">

![Project Euler](https://img.shields.io/badge/Project-Euler-6B4F2A?style=for-the-badge&logo=projecteuler&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Solved-success?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Algorithms%20%C2%B7%20Sliding%20Window-blue?style=for-the-badge)

</div>

---

## 📜 Problem Statement

Find the thirteen adjacent digits in the 1000-digit number that have the greatest product.

🔗 **Project Euler Link:** [Problem 8](https://projecteuler.net/problem=8)

---

## 💡 Key Learnings & Mathematical Insights

- **Sliding Window**: Slide a window of length 13 across the 1000-character string.
- **Zero Skipping**: If the window contains '0', the product is immediately 0 and computation can quickly advance.

---

## 💻 Code Explanation

### 📄 `main.py`
- **Role / Purpose**: Solution implementation for Problem 8.
- **Key Logic**: Defines functions: `greatestProd()`.
- **How It Works**:
  - Implements the mathematical formula and pruning rules described above.
  - Efficiently iterates through the search space and produces the final answer.

---

## ⏱️ Complexity Analysis

| Metric | Complexity | Description |
| :--- | :--- | :--- |
| **Time Complexity** | $O(L \cdot K) \text{ where } L=1000, K=13$ | Fast execution adhering to Project Euler's 1-minute performance rule. |
| **Space Complexity** | $O(1)$ | Efficient memory allocation. |

---

## 🚀 How to Run

```bash
python3 main.py
```

**Verified Answer / Result:**
```text
23514624000
```
