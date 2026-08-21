# 🧮 Project Euler Problem 9: Special Pythagorean Triplet

<div align="center">

![Project Euler](https://img.shields.io/badge/Project-Euler-6B4F2A?style=for-the-badge&logo=projecteuler&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Solved-success?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Math%20%C2%B7%20Pythagorean%20Triples-blue?style=for-the-badge)

</div>

---

## 📜 Problem Statement

A Pythagorean triplet is a set of three natural numbers, $a < b < c$, for which $a^2 + b^2 = c^2$. There exists exactly one Pythagorean triplet for which $a + b + c = 1000$. Find the product $abc$.

🔗 **Project Euler Link:** [Problem 9](https://projecteuler.net/problem=9)

---

## 💡 Key Learnings & Mathematical Insights

- **Variable Substitution**: Since $a + b + c = 1000$, we have $c = 1000 - a - b$. Testing $a^2 + b^2 = (1000 - a - b)^2$ eliminates the third loop for $c$.
- **Bound Analysis**: $a < 1000/3 \approx 333$ and $a < b < (1000 - a)/2$.

---

## 💻 Code Explanation

### 📄 `bruteForce.py`
- **Role / Purpose**: Solution implementation for Problem 9 (Alternative / Optimized approach).
- **Key Logic**: Uses procedural script execution.
- **How It Works**:
  - Implements the mathematical formula and pruning rules described above.
  - Efficiently iterates through the search space and produces the final answer.

### 📄 `straightForward.py`
- **Role / Purpose**: Solution implementation for Problem 9 (Alternative / Optimized approach).
- **Key Logic**: Uses procedural script execution.
- **How It Works**:
  - Implements the mathematical formula and pruning rules described above.
  - Efficiently iterates through the search space and produces the final answer.

---

## ⏱️ Complexity Analysis

| Metric | Complexity | Description |
| :--- | :--- | :--- |
| **Time Complexity** | $O(N^2) / O(N)$ | Fast execution adhering to Project Euler's 1-minute performance rule. |
| **Space Complexity** | $O(1)$ | Efficient memory allocation. |

---

## 🚀 How to Run

```bash
python3 bruteForce.py
```

**Verified Answer / Result:**
```text
31875000
```
