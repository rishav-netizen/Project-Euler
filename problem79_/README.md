# 🧮 Project Euler Problem 79: Passcode Derivation

<div align="center">

![Project Euler](https://img.shields.io/badge/Project-Euler-6B4F2A?style=for-the-badge&logo=projecteuler&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Solved-success?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Graph%20Theory%20%C2%B7%20Topological%20Sort-blue?style=for-the-badge)

</div>

---

## 📜 Problem Statement

Given fifty successful login attempts of 3-character sub-sequences, determine the shortest possible secret passcode.

🔗 **Project Euler Link:** [Problem 79](https://projecteuler.net/problem=79)

---

## 💡 Key Learnings & Mathematical Insights

- **Directed Graph / Partial Ordering**: Each entry $abc$ defines directed edges $a \to b$ and $b \to c$.
- **Topological Sort**: Ordering vertices by in-degree reconstructs the unique secret sequence.

---

## 💻 Code Explanation

### 📄 `main.py`
- **Role / Purpose**: Solution implementation for Problem 79.
- **Key Logic**: Defines functions: `usedNumbers()`, `itemWithNoneBefore()`, `main()`.
- **How It Works**:
  - Implements the mathematical formula and pruning rules described above.
  - Efficiently iterates through the search space and produces the final answer.

---

## ⏱️ Complexity Analysis

| Metric | Complexity | Description |
| :--- | :--- | :--- |
| **Time Complexity** | $O(V + E)$ | Fast execution adhering to Project Euler's 1-minute performance rule. |
| **Space Complexity** | $O(V + E)$ | Efficient memory allocation. |

---

## 🚀 How to Run

```bash
python3 main.py
```

**Verified Answer / Result:**
```text
73162890
```
