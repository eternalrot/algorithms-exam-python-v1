# 📐 Algorithms & Data Structures — Exam Tasks (v2)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![No Dependencies](https://img.shields.io/badge/Dependencies-None-lightgrey)
![Tasks](https://img.shields.io/badge/Tasks-3-orange)

Three algorithm and data structure problems solved in pure Python as part of an **Algorithms & Complexity** exam.

---

## 📋 Table of Contents

- [Tasks Overview](#-tasks-overview)
- [Task 1 — Singly Linked List](#task-1--singly-linked-list)
- [Task 2 — Longest Zero-Sum Subsequence](#task-2--longest-zero-sum-subsequence)
- [Task 3 — Microwave Network Power Calculator](#task-3--microwave-network-power-calculator)
- [Getting Started](#-getting-started)
- [Time Complexity Summary](#-time-complexity-summary)

---

## 📦 Tasks Overview

| File | Topic | Key Algorithm |
|---|---|---|
| `task_1.py` | Singly Linked List | Head-based operations, file loading |
| `task_2.py` | Longest Zero-Sum Subarray | Prefix sums + hash map |
| `task_3.py` | Microwave Network Output Power | Topological BFS on DAG |

---

## Task 1 — Singly Linked List

A from-scratch singly linked list supporting stack-style operations and file-based initialization.

**Supported operations:** `push`, `pop`, `top`, `len`, `is_empty`, `find`, `remove`, `from_file`

```python
from task_1 import SinglyLinkedList

lst = SinglyLinkedList()
lst.push(10)
lst.push(20)
lst.push(30)

print(lst)         # HEAD -> 30 -> 20 -> 10 -> None
print(lst.pop())   # 30
print(lst.find(10))  # True
lst.remove(10)
print(lst)         # HEAD -> 20 -> None
```

| Operation | Time Complexity |
|---|---|
| `push`, `pop`, `top`, `len`, `is_empty` | O(1) |
| `find`, `remove` | O(n) |
| `from_file` | O(n) |

---

## Task 2 — Longest Zero-Sum Subsequence

Finds the length of the longest contiguous subarray whose elements sum to zero.

**Algorithm:** prefix sums + dictionary — first occurrence of each prefix sum is stored; if the same prefix sum appears again at index `j`, the subarray between the two indices sums to zero.

```python
from task_2 import longest_subsequence

s = [100, 5, 0, -5, 1, 1, 1, 1, 1, -5, -5, 5, 5, 5, -3, -7, 7, 25, -15, -7, -3, -5, -21, 38]
print(longest_subsequence(s))  # 16
```

| Complexity | Value |
|---|---|
| Time | O(n) |
| Space | O(n) |

---

## Task 3 — Microwave Network Power Calculator

Calculates output power of a microwave network described as a DAG (directed acyclic graph).

**Network rules:**
- **Divider** (1 input → N outputs): power split equally among outputs
- **Combiner** (N inputs → 1 output): powers summed
- **Device** (1 → 1): `P_out = Γ × P_in`, where `Γ ∈ [0, 1]`

Network is read from a `.txt` file — each line: `input_node, output_node, gamma`

```
# network.txt
0, 1, 0.75
```

```python
from task_3 import output_power

result = output_power("network.txt", input_power=200.0)
print(result)  # 150.0
```

| Complexity | Value |
|---|---|
| Time | O(n) |
| Space | O(n) |

---

## 🚀 Getting Started

**Requirements:** Python 3.8+ — no external libraries needed.

```bash
git clone https://github.com/your-username/algorithms-exam-python.git
cd algorithms-exam-python

python task_1.py
python task_2.py
python task_3.py
```

---

## ⏱ Time Complexity Summary

| Task | Time | Space |
|---|---|---|
| Singly Linked List (per operation) | O(1) – O(n) | O(n) |
| Longest Zero-Sum Subsequence | O(n) | O(n) |
| Microwave Network Power | O(n) | O(n) |

---

## 📄 License

This project is licensed under the MIT License.
