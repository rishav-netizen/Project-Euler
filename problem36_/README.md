# 🧮 Project Euler Problem 36: Double-Base Palindromes

<div align="center">

![Project Euler](https://img.shields.io/badge/Project-Euler-6B4F2A?style=for-the-badge&logo=projecteuler&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Solved-success?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Math%20%C2%B7%20Base%20Conversion%20&%20Palindromes-blue?style=for-the-badge)

</div>

---

## 📜 Problem Statement

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

🔗 **Project Euler Link:** [Problem 36](https://projecteuler.net/problem=36)

---

## 💡 Key Learnings & Mathematical Insights

- **Odd Base-2 Restriction**: Even numbers in binary end in '0' and cannot be palindromes (no leading zeros allowed). Thus, only test odd numbers.
- **Palindromic Verification**: `str(n) == str(n)[::-1]` and `bin(n)[2:] == bin(n)[2:][::-1]`.

---

## 💻 Code Explanation

### 📄 `main.py`
- **Role / Purpose**: Solution implementation for Problem 36.
- **Key Logic**: Defines functions: `decimal_to_binary()`, `isPalindrome()`.
- **How It Works**:
  - Implements the mathematical formula and pruning rules described above.
  - Efficiently iterates through the search space and produces the final answer.

### 📄 `more_optimized.py`
- **Role / Purpose**: Solution implementation for Problem 36 (Alternative / Optimized approach).
- **Key Logic**: Defines functions: `isPalindrome()`, `generatePalindrome()`.
- **How It Works**:
  - Implements the mathematical formula and pruning rules described above.
  - Efficiently iterates through the search space and produces the final answer.

### 📄 `optimized.py`
- **Role / Purpose**: Solution implementation for Problem 36 (Alternative / Optimized approach).
- **Key Logic**: Defines functions: `isPalindrome()`.
- **How It Works**:
  - Implements the mathematical formula and pruning rules described above.
  - Efficiently iterates through the search space and produces the final answer.

---

## ⏱️ Complexity Analysis

| Metric | Complexity | Description |
| :--- | :--- | :--- |
| **Time Complexity** | $O(N) / O(\sqrt{N}) \text{ palindrome generation}$ | Fast execution adhering to Project Euler's 1-minute performance rule. |
| **Space Complexity** | $O(1)$ | Efficient memory allocation. |

---

## 🚀 How to Run

```bash
python3 main.py
```

**Verified Answer / Result:**
```text
872187
```
