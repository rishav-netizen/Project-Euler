# 🧮 Project Euler Problem 17: Number Letter Counts

<div align="center">

![Project Euler](https://img.shields.io/badge/Project-Euler-6B4F2A?style=for-the-badge&logo=projecteuler&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Solved-success?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Strings%20%C2%B7%20Logic%20&%20Dictionary%20Mapping-blue?style=for-the-badge)

</div>

---

## 📜 Problem Statement

If all the numbers from 1 to 1000 (inclusive) were written out in words, how many letters would be used (ignoring spaces and hyphens)?

🔗 **Project Euler Link:** [Problem 17](https://projecteuler.net/problem=17)

---

## 💡 Key Learnings & Mathematical Insights

- **Structural Dictionary Mapping**: Predefine character lengths for ones (1-9), teens (10-19), tens (20-90), hundreds ('hundred' = 7), and 'and' (= 3).
- **British English Grammar**: Include 'and' for numbers with hundreds and non-zero tens/ones (e.g. *three hundred and forty-two*).

---

## 💻 Code Explanation

### 📄 `main.py`
- **Role / Purpose**: Solution implementation for Problem 17.
- **Key Logic**: Defines functions: `get_letter_count()`.
- **How It Works**:
  - Implements the mathematical formula and pruning rules described above.
  - Efficiently iterates through the search space and produces the final answer.

---

## ⏱️ Complexity Analysis

| Metric | Complexity | Description |
| :--- | :--- | :--- |
| **Time Complexity** | $O(N)$ | Fast execution adhering to Project Euler's 1-minute performance rule. |
| **Space Complexity** | $O(1)$ | Efficient memory allocation. |

---

## 🚀 How to Run

```bash
python3 main.py
```

**Verified Answer / Result:**
```text
21124
```
