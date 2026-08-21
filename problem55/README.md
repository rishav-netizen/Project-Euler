# 🧮 Project Euler Problem 55: Lychrel Numbers

<div align="center">

![Project Euler](https://img.shields.io/badge/Project-Euler-6B4F2A?style=for-the-badge&logo=projecteuler&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Solved-success?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Math%20%C2%B7%20Palindromic%20Iteration-blue?style=for-the-badge)

</div>

---

## 📜 Problem Statement

How many Lychrel numbers are there below ten-thousand (numbers that do not produce a palindrome within 50 reverse-and-add iterations)?

🔗 **Project Euler Link:** [Problem 55](https://projecteuler.net/problem=55)

---

## 💡 Key Learnings & Mathematical Insights

- **Reverse and Add**: $n \to n + \text{int}(\text{str}(n)[::-1])$.
- **Cap at 50 Iterations**: Test up to 50 iterations; if no palindrome appears, increment count.

---

## 💻 Code Explanation

### 📄 `main.py`
- **Role / Purpose**: Solution implementation for Problem 55.
- **Key Logic**: Defines functions: `reverse_add()`, `isPalindrome()`, `main()`.
- **How It Works**:
  - Implements the mathematical formula and pruning rules described above.
  - Efficiently iterates through the search space and produces the final answer.

### 📄 `optimized.py`
- **Role / Purpose**: Solution implementation for Problem 55 (Alternative / Optimized approach).
- **Key Logic**: Defines functions: `isPalindrome()`, `main()`.
- **How It Works**:
  - Implements the mathematical formula and pruning rules described above.
  - Efficiently iterates through the search space and produces the final answer.

---

## ⏱️ Complexity Analysis

| Metric | Complexity | Description |
| :--- | :--- | :--- |
| **Time Complexity** | $O(N \cdot 50)$ | Fast execution adhering to Project Euler's 1-minute performance rule. |
| **Space Complexity** | $O(1)$ | Efficient memory allocation. |

---

## 🚀 How to Run

```bash
python3 main.py
```

**Verified Answer / Result:**
```text
249
```
