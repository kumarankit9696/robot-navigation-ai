# Robot Navigation AI

## Introduction
This project implements various pathfinding algorithms for robot navigation in a 2D space. The primary algorithms included are Breadth-First Search (BFS), Depth-First Search (DFS), and A* search algorithms.

## Algorithms

### 1. Breadth-First Search (BFS)
BFS is a graph traversal algorithm that explores nodes layer by layer. It starts at the root node and explores all its neighbors at the present depth prior to moving on to nodes at the next depth level.

#### Characteristics:
- Complete: BFS will always find a solution if one exists.
- Optimal: BFS finds the shortest path in terms of the number of edges.
- Time Complexity: O(b^d)
- Space Complexity: O(b^d)

### 2. Depth-First Search (DFS)
DFS is another graph traversal algorithm that starts at the root node and explores as far as possible along each branch before backtracking.

#### Characteristics:
- Complete: DFS is not guaranteed to find a solution even if one exists.
- Optimal: Does not guarantee the shortest path.
- Time Complexity: O(b^d)
- Space Complexity: O(bd)

### 3. A* Search Algorithm
The A* search algorithm is an extension of Dijkstra's algorithm that incorporates heuristics to improve performance. It finds the shortest path from a start node to a goal node while minimizing the total cost.

#### Characteristics:
- Complete: A* is guaranteed to find a solution if one exists.
- Optimal: A* is optimal if the heuristic used is admissible (it does not overestimate the cost to reach the goal).
- Time Complexity: O(b^d) in the worst case.
- Space Complexity: O(b^d)

## Project Structure
```
robot-navigation-ai/
│
├── algorithms/
│   ├── bfs.py
│   ├── dfs.py
│   └── a_star.py
│
├── main.py
├── README.md
└── requirements.txt
```

### Explanation of Project Structure:
- `algorithms/`: This directory contains the implementations of the BFS, DFS, and A* search algorithms.
- `main.py`: This script serves as the entry point for the project, running the navigation algorithms.
- `requirements.txt`: This file lists the necessary dependencies for the project.

## Usage Examples
To run the project, you can execute the `main.py` file which will demonstrate the functionality of the algorithms.

```bash
python main.py
```

You can also import the algorithms into your own scripts:
```python
from algorithms.bfs import bfs
from algorithms.dfs import dfs
from algorithms.a_star import a_star
```

Feel free to extend or modify the algorithms to fit your needs!