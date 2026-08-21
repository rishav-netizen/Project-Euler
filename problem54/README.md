# 🧮 Project Euler Problem 54: Poker Hands

<div align="center">

![Project Euler](https://img.shields.io/badge/Project-Euler-6B4F2A?style=for-the-badge&logo=projecteuler&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Solved-success?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Game%20Logic%20%C2%B7%20Rank%20Evaluation%20&%20Sorting-blue?style=for-the-badge)

</div>

---

## 📜 Problem Statement

How many hands did Player 1 win in the file of 1,000 poker hands?

🔗 **Project Euler Link:** [Problem 54](https://projecteuler.net/problem=54)

---

## 💡 Key Learnings & Mathematical Insights

- **Tuple Ranking Strategy**: Map poker hands to comparable tuples `(category_rank, tie_breaker_card_ranks)`. Python's natural tuple comparison handles tie-breaking effortlessly.
- **Hand Evaluator**: Evaluates High Card, One Pair, Two Pair, Three of a Kind, Straight, Flush, Full House, Four of a Kind, Straight Flush, Royal Flush.

---

## 💻 Code Explanation

### 📄 `better.py`
- **Role / Purpose**: Solution implementation for Problem 54 (Alternative / Optimized approach).
- **Key Logic**: Defines functions: `__init__()`, `__str__()`, `__repr__()`, `__gt__()`, `__eq__()`, `main()`.
- **How It Works**:
  - Implements the mathematical formula and pruning rules described above.
  - Efficiently iterates through the search space and produces the final answer.

### 📄 `main.py`
- **Role / Purpose**: Solution implementation for Problem 54.
- **Key Logic**: Uses procedural script execution.
- **How It Works**:
  - Implements the mathematical formula and pruning rules described above.
  - Efficiently iterates through the search space and produces the final answer.

---

## ⏱️ Complexity Analysis

| Metric | Complexity | Description |
| :--- | :--- | :--- |
| **Time Complexity** | $O(N) \text{ where } N=1000$ | Fast execution adhering to Project Euler's 1-minute performance rule. |
| **Space Complexity** | $O(1)$ | Efficient memory allocation. |

---

## 🚀 How to Run

```bash
python3 better.py
```

**Verified Answer / Result:**
```text
376
```
