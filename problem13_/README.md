# 🧮 Project Euler Problem 13: Large Sum

<div align="center">

![Project Euler](https://img.shields.io/badge/Project-Euler-6B4F2A?style=for-the-badge&logo=projecteuler&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Solved-success?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Arbitrary%20Precision%20Arithmetic-blue?style=for-the-badge)

</div>

---

## 📜 Problem Statement

Work out the first ten digits of the sum of the one-hundred 50-digit numbers.

🔗 **Project Euler Link:** [Problem 13](https://projecteuler.net/problem=13)

---

## 💡 Key Learnings & Mathematical Insights

- **BigInt Native Support**: Python handles 50-digit integers seamlessly without overflow or precision loss.
- **String Slicing**: After summing all 100 numbers, `str(total)[:10]` yields the leading ten digits.

---

## 💻 Code Explanation

### 📄 `main.py`
- **Role / Purpose**: Solution implementation for Problem 13.
- **Key Logic**: Uses procedural script execution.
- **How It Works**:
  - Implements the mathematical formula and pruning rules described above.
  - Efficiently iterates through the search space and produces the final answer.

---

## ⏱️ Complexity Analysis

| Metric | Complexity | Description |
| :--- | :--- | :--- |
| **Time Complexity** | $O(N \cdot D)$ | Fast execution adhering to Project Euler's 1-minute performance rule. |
| **Space Complexity** | $O(N)$ | Efficient memory allocation. |

---

## 🚀 How to Run

```bash
python3 main.py
```

**Verified Answer / Result:**
```text
5537376230
```
