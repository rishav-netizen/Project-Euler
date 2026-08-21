# 🧮 Project Euler Problem 31: Coin Sums

<div align="center">

![Project Euler](https://img.shields.io/badge/Project-Euler-6B4F2A?style=for-the-badge&logo=projecteuler&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Solved-success?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Dynamic%20Programming%20%C2%B7%20Unbounded%20Knapsack-blue?style=for-the-badge)

</div>

---

## 📜 Problem Statement

How many different ways can £2 (200p) be made using any number of English coins (1p, 2p, 5p, 10p, 20p, 50p, 100p, 200p)?

🔗 **Project Euler Link:** [Problem 31](https://projecteuler.net/problem=31)

---

## 💡 Key Learnings & Mathematical Insights

- **Coin Change DP**: `dp[i]` represents ways to make target amount `i`. Base case `dp[0] = 1`.
- **Outer Coin Loop**: Outer iteration over coin denominations ensures unordered combinations: `dp[i] += dp[i - coin]`.

---

## 💻 Code Explanation

### 📄 `main.py`
- **Role / Purpose**: Solution implementation for Problem 31.
- **Key Logic**: Uses procedural script execution.
- **How It Works**:
  - Implements the mathematical formula and pruning rules described above.
  - Efficiently iterates through the search space and produces the final answer.

---

## ⏱️ Complexity Analysis

| Metric | Complexity | Description |
| :--- | :--- | :--- |
| **Time Complexity** | $O(C \cdot T) = O(8 \times 200)$ | Fast execution adhering to Project Euler's 1-minute performance rule. |
| **Space Complexity** | $O(T) = O(200)$ | Efficient memory allocation. |

---

## 🚀 How to Run

```bash
python3 main.py
```

**Verified Answer / Result:**
```text
73682
```
