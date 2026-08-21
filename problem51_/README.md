# 🧮 Project Euler Problem 51: Prime Digit Replacements

<div align="center">

![Project Euler](https://img.shields.io/badge/Project-Euler-6B4F2A?style=for-the-badge&logo=projecteuler&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Solved-success?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Number%20Theory%20%C2%B7%20Pattern%20Matching%20&%20Primes-blue?style=for-the-badge)

</div>

---

## 📜 Problem Statement

Find the smallest prime which, by replacing part of the number with the same digit, is part of an eight prime value family.

🔗 **Project Euler Link:** [Problem 51](https://projecteuler.net/problem=51)

---

## 💡 Key Learnings & Mathematical Insights

- **Modulo 3 Divisibility Invariance**: Replacing 1 or 2 digits creates numbers whose sum mod 3 cycles through all residues, ensuring at least 3 composite multiples of 3. Therefore, exactly 3 digits must be replaced.
- **Candidate Generation**: Search primes containing three 0's, three 1's, or three 2's.

---

## 💻 Code Explanation

### 📄 `main.py`
- **Role / Purpose**: Solution implementation for Problem 51.
- **Key Logic**: Defines functions: `primes_till()`, `is_eligible()`, `main()`.
- **How It Works**:
  - Implements the mathematical formula and pruning rules described above.
  - Efficiently iterates through the search space and produces the final answer.

---

## ⏱️ Complexity Analysis

| Metric | Complexity | Description |
| :--- | :--- | :--- |
| **Time Complexity** | $O(N)$ | Fast execution adhering to Project Euler's 1-minute performance rule. |
| **Space Complexity** | $O(N)$ | Efficient memory allocation. |

---

## 🚀 How to Run

```bash
python3 main.py
```

**Verified Answer / Result:**
```text
121313
```
