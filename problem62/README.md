# 🧮 Project Euler Problem 62: Cubic Permutations

<div align="center">

![Project Euler](https://img.shields.io/badge/Project-Euler-6B4F2A?style=for-the-badge&logo=projecteuler&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Solved-success?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Algorithms%20%C2%B7%20Hash%20Map%20Grouping-blue?style=for-the-badge)

</div>

---

## 📜 Problem Statement

Find the smallest cube for which exactly five permutations of its digits are cube.

🔗 **Project Euler Link:** [Problem 62](https://projecteuler.net/problem=62)

---

## 💡 Key Learnings & Mathematical Insights

- **Sorted Digit Key**: For each $n^3$, compute `key = "".join(sorted(str(n**3)))` and append $n$ to `table[key]`.
- **First Match**: The first key to accumulate 5 cubes provides the minimum cube $n_{\text{min}}^3$.

---

## 💻 Code Explanation

### 📄 `main.py`
- **Role / Purpose**: Solution implementation for Problem 62.
- **Key Logic**: Uses procedural script execution (imports: `itertools`).
- **How It Works**:
  - Implements the mathematical formula and pruning rules described above.
  - Efficiently iterates through the search space and produces the final answer.

---

## ⏱️ Complexity Analysis

| Metric | Complexity | Description |
| :--- | :--- | :--- |
| **Time Complexity** | $O(N \cdot D \log D)$ | Fast execution adhering to Project Euler's 1-minute performance rule. |
| **Space Complexity** | $O(N)$ | Efficient memory allocation. |

---

## 🚀 How to Run

```bash
python3 main.py
```

**Verified Answer / Result:**
```text
127035954683
```
