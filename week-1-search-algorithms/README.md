# Search Algorithms for Week 1 - COMP9414

This project includes the week-1 tutorial and additional programming exercises.

## Algorithms
- Depth-first Search (DFS): Expand one node at the deepest level reached so far
- Breadth-First Search (BFS): All nodes are expanded at a same depth in the tree before any nodes at the next level are expanded
- Uniform Cost Search (UCS): Expands nodes with the lowest cumulative cost g(n) using a priority queue.
- Greedy Best-First Search: Always select node closest to goal according to heuristic function.
- A* search: f(n) = g(n) + h(n) Combine UCS and Greedy Best-First Search

### Uniform-Cost Search 
Reduces to breadth-first search when all actions have same cost

### Uniformed vs Informed Search
- Uninformed: Keeps searching until it stumbles on goal (no domain knowledge)
- Informed: Searches (**a.k.a heuristics**) in direction of best guess to goal (uses domain knowledge)