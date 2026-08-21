# 🧮 Project Euler Problem 39: Integer Right Triangles

<div align="center">

![Project Euler](https://img.shields.io/badge/Project-Euler-6B4F2A?style=for-the-badge&logo=projecteuler&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Solved-success?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Math%20%C2%B7%20Pythagorean%20Triangles-blue?style=for-the-badge)

</div>

---

## 📜 Problem Statement

For which value of $p \le 1000$ (perimeter) is the number of solutions to $a^2 + b^2 = c^2$ with $a+b+c=p$ maximised?

🔗 **Project Euler Link:** [Problem 39](https://projecteuler.net/problem=39)

---

## 💡 Key Learnings & Mathematical Insights

- **Direct Formula for $b$**: $c = p - a - b \implies b = \frac{p^2 - 2pa}{2(p - a)}$.
- **Even Perimeter Property**: $p$ must be even because $a^2+b^2=c^2$ requires either 0 or 2 odd legs.

---

## 💻 Code Explanation

### 📄 `main.py`
- **Role / Purpose**: Solution implementation for Problem 39.
- **Key Logic**: Defines functions: `generateTriplets()`.
- **How It Works**:
  - Implements the mathematical formula and pruning rules described above.
  - Efficiently iterates through the search space and produces the final answer.

---

## ⏱️ Complexity Analysis

| Metric | Complexity | Description |
| :--- | :--- | :--- |
| **Time Complexity** | $O(P^2 / 4)$ | Fast execution adhering to Project Euler's 1-minute performance rule. |
| **Space Complexity** | $O(P)$ | Efficient memory allocation. |

---

## 🚀 How to Run

```bash
python3 main.py
```

**Verified Answer / Result:**
```text
840
```
