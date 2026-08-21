# 🧮 Project Euler Problem 97: Large Non-Mersenne Prime

<div align="center">

![Project Euler](https://img.shields.io/badge/Project-Euler-6B4F2A?style=for-the-badge&logo=projecteuler&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Solved-success?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Math%20%C2%B7%20Modular%20Exponentiation-blue?style=for-the-badge)

</div>

---

## 📜 Problem Statement

Find the last ten digits of the massive prime $28433 \times 2^{7830457} + 1$.

🔗 **Project Euler Link:** [Problem 97](https://projecteuler.net/problem=97)

---

## 💡 Key Learnings & Mathematical Insights

- **Modular Arithmetic**: $(28433 \times (2^{7830457} \pmod{10^{10}}) + 1) \pmod{10^{10}}$.
- **`pow(2, 7830457, 10**10)`**: Computes in $O(\log(\text{exp})) \approx 23$ multiplications.

---

## 💻 Code Explanation

### 📄 `main.py`
- **Role / Purpose**: Solution implementation for Problem 97.
- **Key Logic**: Uses procedural script execution.
- **How It Works**:
  - Implements the mathematical formula and pruning rules described above.
  - Efficiently iterates through the search space and produces the final answer.

---

## ⏱️ Complexity Analysis

| Metric | Complexity | Description |
| :--- | :--- | :--- |
| **Time Complexity** | $O(\log(\text{exponent}))$ | Fast execution adhering to Project Euler's 1-minute performance rule. |
| **Space Complexity** | $O(1)$ | Efficient memory allocation. |

---

## 🚀 How to Run

```bash
python3 main.py
```

**Verified Answer / Result:**
```text
8739992577
```
