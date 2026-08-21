# 🧮 Project Euler Problem 4: Largest Palindrome Product

<div align="center">

![Project Euler](https://img.shields.io/badge/Project-Euler-6B4F2A?style=for-the-badge&logo=projecteuler&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Solved-success?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Math%20%C2%B7%20Palindromes%20&%20Search-blue?style=for-the-badge)

</div>

---

## 📜 Problem Statement

Find the largest palindrome made from the product of two 3-digit numbers.

🔗 **Project Euler Link:** [Problem 4](https://projecteuler.net/problem=4)

---

## 💡 Key Learnings & Mathematical Insights

- **Reverse Nested Search with Pruning**: Iterate $i, j$ downwards from 999 to 100. If $i \times j \le \text{max\_palindrome}$, break the inner loop early because subsequent products will be even smaller.
- **Divisibility by 11**: Any 6-digit palindrome $abccba = 11(9091a + 910b + 100c)$, so at least one factor must be a multiple of 11.

---

## 💻 Code Explanation

### 📄 `main.py`
- **Role / Purpose**: Solution implementation for Problem 4.
- **Key Logic**: Uses procedural script execution.
- **How It Works**:
  - Implements the mathematical formula and pruning rules described above.
  - Efficiently iterates through the search space and produces the final answer.

---

## ⏱️ Complexity Analysis

| Metric | Complexity | Description |
| :--- | :--- | :--- |
| **Time Complexity** | $O(N^2)$ | Fast execution adhering to Project Euler's 1-minute performance rule. |
| **Space Complexity** | $O(1)$ | Efficient memory allocation. |

---

## 🚀 How to Run

```bash
python3 main.py
```

**Verified Answer / Result:**
```text
906609
```
