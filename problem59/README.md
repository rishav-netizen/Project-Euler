# 🧮 Project Euler Problem 59: XOR Decryption

<div align="center">

![Project Euler](https://img.shields.io/badge/Project-Euler-6B4F2A?style=for-the-badge&logo=projecteuler&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Solved-success?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Cryptography%20%C2%B7%20Frequency%20Analysis-blue?style=for-the-badge)

</div>

---

## 📜 Problem Statement

Decrypt the cipher using a 3-character lowercase key and find the sum of ASCII values of the original text.

🔗 **Project Euler Link:** [Problem 59](https://projecteuler.net/problem=59)

---

## 💡 Key Learnings & Mathematical Insights

- **Key Space**: $26^3 = 17576$ possible keys.
- **Heuristic Scoring**: Valid English text contains abundant spaces (ASCII 32) and common English words like 'the'.

---

## 💻 Code Explanation

### 📄 `main.py`
- **Role / Purpose**: Solution implementation for Problem 59.
- **Key Logic**: Defines functions: `main()`, `combinations()`.
- **How It Works**:
  - Implements the mathematical formula and pruning rules described above.
  - Efficiently iterates through the search space and produces the final answer.

---

## ⏱️ Complexity Analysis

| Metric | Complexity | Description |
| :--- | :--- | :--- |
| **Time Complexity** | $O(26^3 \cdot N)$ | Fast execution adhering to Project Euler's 1-minute performance rule. |
| **Space Complexity** | $O(N)$ | Efficient memory allocation. |

---

## 🚀 How to Run

```bash
python3 main.py
```

**Verified Answer / Result:**
```text
129448
```
