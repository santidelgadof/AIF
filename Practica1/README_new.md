# Lab 1: Search Algorithms Implementation

**Authors:** David Carballo Rodríguez, Antonio Vila Leis, Santiago Delgado Ferreiro  
**Course:** Artificial Intelligence Fundamentals - Master in AI (2025-2026)

---

## 🚀 Quick Start

```bash
# 1. Run BFS on the example map
python main.py exampleMap.txt bfs

# 2. Run A* with detailed trace
python main.py exampleMap.txt astar --verbose

# 3. Run automated experiments (generates results and LaTeX tables)
python run_experiments.py

# 4. Visualize path comparison (generates comparison_large.png)
python visualize.py
```

---

## 📋 Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
  - [Running Search Algorithms](#running-search-algorithms)
  - [Running Experiments](#running-experiments)
  - [Visualization](#visualization)
- [Map File Format](#map-file-format)
- [Algorithms](#algorithms)
- [Output Format](#output-format)
- [Files Generated](#files-generated)
- [Report](#report)

---

## 🎯 Overview

This project implements three classic search algorithms to solve a robot navigation problem:

- **Breadth-First Search (BFS)**: Explores level by level, guarantees shortest path in terms of number of actions
- **Depth-First Search (DFS)**: Explores depth-first, may find solutions faster but not optimal
- **A* Search**: Uses heuristic (Euclidean distance + rotation cost) to find optimal cost paths

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

## 📁 Project Structure

```
AIF/
├── main.py                  # Main program (CLI interface)
├── search.py                # BFS, DFS, A* implementations
├── problem.py               # Problem definition (successors, goal test, map loader)
├── state.py                 # State representation
├── node.py                  # Search tree node
├── run_experiments.py       # Automated performance experiments
├── visualize.py             # Path visualization tool
├── exampleMap.txt           # Example map file
├── experiment_results.txt   # Generated: experiment results
├── comparison_large.png     # Generated: BFS vs A* visualization
├── report.tex               # LaTeX report (main deliverable)
├── report.pdf               # Compiled report
└── README.md                # This file
```

**Key Files:**
- **`main.py`**: Command-line interface to run individual algorithms
- **`run_experiments.py`**: Generates performance statistics for all algorithms
- **`visualize.py`**: Creates visual comparison of BFS vs A* paths
- **`report.tex`**: Complete LaTeX report with methods, results, and discussion

---

## ⚙️ Requirements

- **Python 3.10+** (uses type hints with `|` operator)
- **Standard Library Only** (no external dependencies required for core algorithms)
- **Optional:** `matplotlib` and `numpy` for visualization (only needed for `visualize.py`)

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

3. **No additional installation needed!** All core functionality uses Python's standard library.

4. **(Optional) Install visualization dependencies:**
   ```bash
   pip install matplotlib numpy
   ```

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

# Run A* with verbose output (shows step-by-step execution)
python main.py exampleMap.txt astar --verbose

# Run DFS
python main.py exampleMap.txt dfs
```

**Expected output:**
```
Node 0 (starting node)
  (0, 0, START, (0, 3, 0))

Operator 1
  rotate_left
Node 1
  (1, 1, rotate_left, (0, 3, 7))

Operator 2
  rotate_left
Node 2
  (2, 2, rotate_left, (0, 3, 6))

...

Total number of items in explored list: 8
Total number of items in frontier: 5
```

### Running Experiments

To run automated performance tests and generate statistics:

```bash
python run_experiments.py
```

**What it does:**
1. Generates random maps of sizes 3×3, 5×5, 7×7, 9×9
2. Runs all three algorithms (BFS, DFS, A*) on each map
3. Averages results over 5 trials per size
4. Displays statistics: depth (d), cost (g), nodes explored (#E), frontier size (#F)
5. Generates LaTeX tables ready for the report
6. Saves all results to `experiment_results.txt`

**Expected output:**
```
============================================================
Search Algorithms Performance Experiment
============================================================

Running experiments for 3x3 maps...

Trial 1/5:
  Map: Start=(0, 0, 0), Goal=(2, 2, 8)
  Running BFS... ✓ (d=5.0, g=12.0, E=10.0, F=6.0)
  Running DFS... ✓ (d=21.0, g=34.4, E=24.0, F=9.0)
  Running ASTAR... ✓ (d=5.4, g=11.8, E=29.4, F=8.2)

...

3x3 Maps (averaged over 5 trials):
Algorithm                      d        g       #E       #F
------------------------------------------------------------
Breadth-First Search         5.0     12.0     10.0      6.0
Depth-First Search          21.0     34.4     24.0      9.0
A*                           5.4     11.8     29.4      8.2
```

The script also generates LaTeX tables that can be directly copied into the report.

### Visualization

To generate a visual comparison of BFS vs A* paths:

```bash
python visualize.py
```

**Requirements:** `matplotlib` and `numpy` must be installed.

**What it does:**
1. Creates a challenging map with high-cost cells along the direct path
2. Runs both BFS and A* on the map
3. Generates `comparison_large.png` showing:
   - Left: BFS path (shortest in actions, but crosses expensive terrain)
   - Right: A* path (longer in actions, but cheaper in total cost)
4. Color-coded terrain (darker = higher hardness)

This visualization is included in the report to demonstrate the key difference between depth-optimal (BFS) and cost-optimal (A*) search.

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
3 4
1 2 3 4
2 1 2 3
3 2 1 2
0 3 0
1 2 8
```

**Explanation:**
- Line 1: `3 4` → Map is 3 rows × 4 columns
- Lines 2-4: Terrain hardness values (1-9 typically)
  - 1 = easy terrain, 9 = very hard terrain
  - Movement cost = hardness value of destination cell
- Line 5: `0 3 0` → Start at row 0, column 3, facing North (orientation 0)
- Line 6: `1 2 8` → Goal is row 1, column 2, any orientation (8 = wildcard)

**Orientation codes:**
```
     0 (N)
7 (NW) ↑ 1 (NE)
6 (W) ← · → 2 (E)
5 (SW) ↓ 3 (SE)
     4 (S)

0 = North        1 = Northeast    2 = East         3 = Southeast
4 = South        5 = Southwest    6 = West         7 = Northwest
8 = Any (goal only - wildcard for any final orientation)
```

---

## 🧮 Algorithms

### Breadth-First Search (BFS)
- **Data Structure:** Queue (FIFO using `collections.deque`)
- **Strategy:** Explores all nodes at depth `d` before depth `d+1`
- **Completeness:** Yes (in finite graphs)
- **Optimality:** Finds minimum **depth** (number of actions), NOT minimum **cost**
- **Space Complexity:** O(b^d) where b = branching factor, d = depth
- **Best for:** Finding shortest paths when all actions have equal cost

**Implementation details:**
- Uses `explored` set to avoid revisiting states
- Uses `frontier_set` for O(1) duplicate checking
- Goal test on generation for early termination

### Depth-First Search (DFS)
- **Data Structure:** Stack (LIFO using Python list)
- **Strategy:** Explores as deep as possible before backtracking
- **Completeness:** Yes (with cycle detection in finite graphs)
- **Optimality:** NO - first solution found may be far from optimal
- **Space Complexity:** O(b*m) where m = maximum depth
- **Best for:** Memory-constrained scenarios (but not recommended for this problem)

**Implementation details:**
- Reverses successor order on stack to maintain R→M→L expansion order
- May find very long, suboptimal paths
- In our problem, exhibits rotational bias (excessive rotations before moving)

### A* Search
- **Data Structure:** Priority queue (min-heap using `heapq`)
- **Strategy:** Expands nodes with lowest f(n) = g(n) + h(n)
  - g(n) = actual cost from start to node n
  - h(n) = heuristic estimate of cost from n to goal
- **Heuristic:** h(n) = Euclidean distance + minimum rotation cost
  ```
  h(n) = sqrt((x_goal - x)^2 + (y_goal - y)^2) + min_rotation_cost
  ```
- **Completeness:** Yes
- **Optimality:** YES - guaranteed optimal solution (heuristic is admissible)
- **Best for:** Finding minimum **cost** paths in weighted graphs

**Implementation details:**
- Uses tie-breaking with insertion counter for FIFO behavior when f-values equal
- Tracks best g-value per state to handle duplicate paths
- Lazy deletion of stale entries in priority queue

**Heuristic properties:**
- **Admissible:** Generally does not overestimate (with minor exceptions on diagonal moves)
- **Consistent:** Mostly monotonic, allows efficient search without reopening nodes
- **Informative:** Provides good guidance toward goal, though underestimates due to ignoring terrain variation

---

## 📊 Output Format

### Standard Output (all algorithms)

```
Node(depth, cost, operator, state)
Node 0 (starting node)
  (0, 0, START, (0, 3, 0))

Operator 1
  rotate_left
Node 1
  (1, 1, rotate_left, (0, 3, 7))

Operator 2
  rotate_left
Node 2
  (2, 2, rotate_left, (0, 3, 6))

...

Total number of items in explored list: 8
Total number of items in frontier: 5
```

**Key metrics:**
- **depth**: Number of actions from start (d)
- **cost**: Cumulative cost from start (g)
- **explored**: Total nodes expanded
- **frontier**: Nodes in queue when solution found

### A* Output (includes heuristic)

```
Node(depth, cost, operator, h, state)
Node 0 (starting node)
  (0, 0, START, 1.41, (0, 3, 0))

Operator 1
  rotate_left
Node 1
  (1, 1, rotate_left, 1.41, (0, 3, 7))
...
```

The additional `h` value shows the heuristic estimate at each node.

### Verbose Output (with `-v` flag)

Provides step-by-step execution trace showing:
- Current node being expanded
- Generated successors
- Current frontier state
- Goal detection

---

## 📁 Files Generated

### By `run_experiments.py`

**`experiment_results.txt`**
- Performance statistics for all algorithms
- Averaged over multiple trials per map size
- Includes LaTeX table code ready for the report

Example content:
```
3x3 Maps:
Algorithm                           d        g       #E       #F
------------------------------------------------------------
Breadth-First Search              5.0     12.0     10.0      6.0
Depth-First Search               21.0     34.4     24.0      9.0
A*                                5.4     11.8     29.4      8.2

\begin{table}[H]
\caption{Performance comparison for $3\times3$ maps}
...
```

### By `visualize.py`

**`comparison_large.png`**
- Side-by-side comparison of BFS and A* paths
- Left: BFS solution (minimum depth)
- Right: A* solution (minimum cost)
- Color-coded terrain showing hardness values
- Demonstrates cost-awareness of A* vs depth-optimality of BFS

---

## 📝 Report

The main deliverable is **`report.tex`**, which contains:

1. **Methods Section:**
   - Formal problem characterization (state space, operators, transition model)
   - Analysis of blind search methods (BFS, DFS)
   - Heuristic definition and justification for A*
   - Admissibility and monotonicity analysis

2. **Results Section:**
   - Execution traces on example map
   - Performance comparison tables (generated by `run_experiments.py`)
   - Visual comparison figure (generated by `visualize.py`)

3. **Discussion Section:**
   - Comparative analysis of all three algorithms
   - Advantages and disadvantages observed
   - Heuristic performance analysis
   - Extension discussion (impassable rocks)

4. **Appendix:**
   - Source code documentation
   - Implementation details for each module

**To compile the report:**
```bash
pdflatex report.tex
# Run twice for proper references
pdflatex report.tex
```

---

## 🧪 Testing & Validation

**Verify algorithm correctness:**

```bash
# BFS should find minimum depth solution
python main.py exampleMap.txt bfs

# A* should find minimum cost solution (may have slightly longer depth)
python main.py exampleMap.txt astar

# DFS will find A solution (not necessarily optimal)
python main.py exampleMap.txt dfs
```

**Compare algorithms:**
- BFS: shortest in actions, but may cross expensive terrain
- A*: optimal cost, slightly longer paths if needed to avoid expensive cells
- DFS: typically finds very long, expensive paths

**Expected behavior on `exampleMap.txt`:**
- BFS: depth ≈ 4, cost ≈ 4
- A*: depth ≈ 4, cost ≈ 4 (similar to BFS on this simple map)
- DFS: depth ≈ 6, cost ≈ 6 (longer due to exploration strategy)

---

## 🤝 Authors

This is an academic project for the Master in Artificial Intelligence at UDC.

**Team members:**
- **David Carballo Rodríguez**
- **Antonio Vila Leis**
- **Santiago Delgado Ferreiro**

**Supervisor:** Prof. [Instructor Name]  
**Institution:** Universidade da Coruña (UDC)  
**Academic Year:** 2025-2026

---

## 📚 References

- Lab assignment: `AIF.pdf`
- Russell, S., & Norvig, P. (2020). *Artificial Intelligence: A Modern Approach* (4th ed.)
- Full implementation details: See `report.tex`

---

## 🔗 Repository

GitHub: [https://github.com/santidelgadof/AIF](https://github.com/santidelgadof/AIF)

---

## 📧 Contact

For questions about this implementation, please contact the authors or open an issue on GitHub.

---

**Last Updated:** October 9, 2025
