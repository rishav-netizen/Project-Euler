# 🧮 Project Euler Problem 99: Largest Exponential

<div align="center">

![Project Euler](https://img.shields.io/badge/Project-Euler-6B4F2A?style=for-the-badge&logo=projecteuler&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Solved-success?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Math%20%C2%B7%20Logarithms%20&%20Order%20Comparison-blue?style=for-the-badge)

</div>

---

## 📜 Problem Statement

Using a 1000-line file of base-exponent pairs $(b, e)$, determine which line number has the greatest numerical value.

🔗 **Project Euler Link:** [Problem 99](https://projecteuler.net/problem=99)

---

## 💡 Key Learnings & Mathematical Insights

- **Logarithmic Transformation**: Comparing $b^e$ is equivalent to comparing $e \cdot \ln(b)$ since $\ln(x)$ is strictly monotonically increasing.
- **Overflow Avoidance**: Operates in fast floating point arithmetic without generating huge numbers.

---

## 💻 Code Explanation

### 📄 `main.py`
- **Role / Purpose**: Solution implementation for Problem 99.
- **Key Logic**: Uses procedural script execution (imports: `math`).
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
709
```
