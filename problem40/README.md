# 🧮 Project Euler Problem 40: Champernowne's Constant

<div align="center">

![Project Euler](https://img.shields.io/badge/Project-Euler-6B4F2A?style=for-the-badge&logo=projecteuler&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Solved-success?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Sequences%20%C2%B7%20Fractional%20Part%20Digit%20Concatenation-blue?style=for-the-badge)

</div>

---

## 📜 Problem Statement

An irrational decimal fraction is created by concatenating the positive integers. Find the product $d_1 \times d_{10} \times d_{100} \times d_{1000} \times d_{10000} \times d_{100000} \times d_{1000000}$.

🔗 **Project Euler Link:** [Problem 40](https://projecteuler.net/problem=40)

---

## 💡 Key Learnings & Mathematical Insights

- **Concatenation Buffer**: Append numbers until string length exceeds $1,000,000$.
- **Direct Offset Indexing**: Extract characters at indices $10^0, 10^1, \dots, 10^6$ and multiply.

---

## 💻 Code Explanation

### 📄 `main.py`
- **Role / Purpose**: Solution implementation for Problem 40.
- **Key Logic**: Uses procedural script execution.
- **How It Works**:
  - Implements the mathematical formula and pruning rules described above.
  - Efficiently iterates through the search space and produces the final answer.

---

## ⏱️ Complexity Analysis

| Metric | Complexity | Description |
| :--- | :--- | :--- |
| **Time Complexity** | $O(L) \text{ where } L=10^6$ | Fast execution adhering to Project Euler's 1-minute performance rule. |
| **Space Complexity** | $O(L)$ | Efficient memory allocation. |

---

## 🚀 How to Run

```bash
python3 main.py
```

**Verified Answer / Result:**
```text
210
```
