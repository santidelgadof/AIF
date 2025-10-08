**Authors:** David Carballo Rodríguez, Antonio Vila Leis, Santiago Delgado Ferreiro  
**Course:** Artificial Intelligence Fundamentals - Master in AI (2025-2026)

---

## 📋 Table of Contents

- [Overview](#overview)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
  - [Running Search Algorithms](#running-search-algorithms)
  - [Running Experiments](#running-experiments)
- [Map File Format](#map-file-format)
- [Algorithms](#algorithms)
- [Output Format](#output-format)
- [Contributing](#contributing)

---

## 🎯 Overview

This project implements three classic search algorithms to solve a robot navigation problem:

- **Breadth-First Search (BFS)**: Explores level by level, guarantees shortest path in terms of number of actions
- **Depth-First Search (DFS)**: Explores depth-first, may find solutions faster but not optimal
- **A Star Search**: Uses heuristic (Euclidean distance + rotation cost) to find optimal paths efficiently

### Problem Definition

**State Space:** `(x, y, o)` where:
- `x, y`: Robot position on grid (row, column)
- `o`: Orientation (0=N, 1=NE, 2=E, 3=SE, 4=S, 5=SW, 6=W, 7=NW)

**Actions:**
- `rotate_right`: Turn 45° clockwise (cost = 1)
- `rotate_left`: Turn 45° counter-clockwise (cost = 1)
- `move`: Move forward in current orientation (cost = terrain hardness)

**Goal:** Navigate from start position to goal position, optionally matching orientation.

---

## ⚙️ Requirements

- **Python 3.10+** (uses type hints with `|` operator)
- **Standard Library Only** (no external dependencies)

Required modules (all built-in):
- `dataclasses`
- `collections`
- `heapq`
- `itertools`
- `math`
- `sys`
- `random`

---

## 🚀 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/santidelgadof/AIF.git
   cd AIF
   ```

2. **Verify Python version:**
   ```bash
   python --version  # Should be 3.10 or higher
   ```

3. **No additional installation needed!** All dependencies are part of Python's standard library.

---

## 💻 Usage

### Running Search Algorithms

**Basic syntax:**
```bash
python main.py <map_file> <algorithm> [--verbose|-v]
```

**Parameters:**
- `<map_file>`: Path to map file (e.g., `exampleMap.txt`)
- `<algorithm>`: Algorithm to use (`bfs`, `dfs`, or `astar`)
- `--verbose` or `-v`: (Optional) Enable detailed execution trace

**Examples:**

```bash
# Run BFS on example map
python main.py exampleMap.txt bfs

# Run A* with verbose output
python main.py exampleMap.txt astar --verbose

# Run DFS
python main.py exampleMap.txt dfs
```

### Running Experiments

To run automated performance tests on randomly generated maps:

```bash
python run_experiments.py
```

This will:
1. Generate random maps of sizes 3×3, 5×5, 7×7, 9×9
2. Run all three algorithms (BFS, DFS, A*) on each map
3. Average results over 5 trials per size
4. Output statistics and formatted LaTeX tables
5. Save results to `experiment_results.txt`

**Expected output:**
```
===========================================================
Search Algorithms Performance Experiment
===========================================================

Starting experiments...

===========================================================
Running experiments for 3x3 maps...
===========================================================

Trial 1/5:
  Running BFS... ✓ (d=4, g=8, E=12, F=3)
  Running DFS... ✓ (d=6, g=10, E=8, F=2)
  Running ASTAR... ✓ (d=4, g=8, E=9, F=2)
...
```

---

## 📄 Map File Format

Map files are plain text with the following structure:

```
<rows> <cols>
<hardness_matrix>
...
<start_x> <start_y> <start_orientation>
<goal_x> <goal_y> <goal_orientation>
```

**Example (`exampleMap.txt`):**
```
3 3
1 2 3
2 1 2
3 2 1
0 0 0
2 2 8
```

**Explanation:**
- Line 1: `3 3` → Map is 3×3
- Lines 2-4: Terrain hardness values (1-5 typically)
- Line 5: `0 0 0` → Start at position (0,0) facing North (orientation 0)
- Line 6: `2 2 8` → Goal is position (2,2) with any orientation (8 = wildcard)

**Orientation codes:**
```
0 = North        1 = Northeast    2 = East         3 = Southeast
4 = South        5 = Southwest    6 = West         7 = Northwest
8 = Any (goal only)
```

---

## 🧮 Algorithms

### Breadth-First Search (BFS)
- **Data Structure:** Queue (FIFO)
- **Strategy:** Explores all nodes at depth `d` before depth `d+1`
- **Guarantees:** Shortest path in terms of number of actions

### Depth-First Search (DFS)
- **Data Structure:** Stack (LIFO)
- **Strategy:** Explores as deep as possible before backtracking
- **Guarantees:** None (may find non-optimal solutions)

### A* Search
- **Data Structure:** Priority queue (min-heap)
- **Strategy:** Expands nodes with lowest f(n) = g(n) + h(n)
- **Heuristic:** Euclidean distance + minimum rotation cost
- **Guarantees:** Optimal solution (heuristic is admissible)

---

## 📊 Output Format

### Standard Output

```
Node 0 (starting node)
  (0, 0, START, (0, 0, 0))

Operator 1
  rotate_right
Node 1
  (1, 1, rotate_right, (0, 0, 1))

Operator 2
  move
Node 2
  (2, 3, move, (0, 1, 1))

...

Total number of items in explored list: 15
Total number of items in frontier: 4
```

### Verbose Output (with `-v` flag)

```
[Step 0] Expand: (0, 0, 0) (g=0, d=0)
  Generated -> rotate_right:(0, 0, 1), move:(1, 0, 0), rotate_left:(0, 0, 7)
  Frontier: ['(0, 0, 1)', '(1, 0, 0)', '(0, 0, 7)']

[Step 1] Expand: (0, 0, 1) (g=1, d=1)
  Generated -> rotate_right:(0, 0, 2), move:(0, 1, 1)
  Goal found -> (0, 1, 1) (g=3, d=2)
```

### A* Output (includes heuristic)

```
Node 0 (starting node)
  (0, 0, START, 2.83, (0, 0, 0))

Operator 1
  move
Node 1
  (1, 1, move, 1.41, (1, 0, 0))
...
```

Format: `(depth, cost, operator, heuristic, state)`

---

## 🧪 Testing

To verify correctness, compare algorithm outputs:

```bash
# BFS should find solution with minimum depth
python main.py exampleMap.txt bfs

# A* should find solution with minimum cost
python main.py exampleMap.txt astar

# DFS may find different (potentially longer) solution
python main.py exampleMap.txt dfs
```

---

## 🤝 Contributing

This is an academic project for the Master in Artificial Intelligence. 

**Team members:**
- David Carballo Rodríguez
- Antonio Vila Leis
- Santiago Delgado Ferreiro

For questions or suggestions, please contact the authors.

---

## 📚 References

- Lab assignment: `lab1-AIF-2025.pdf`
- Full implementation details: See `report.tex` (LaTeX report)

---

## 🔗 Repository

GitHub: [https://github.com/santidelgadof/AIF](https://github.com/santidelgadof/AIF)

---