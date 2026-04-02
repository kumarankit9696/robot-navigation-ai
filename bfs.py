from collections import deque
from typing import List, Tuple, Optional

class BFS:
    """
    Breadth-First Search (BFS) Algorithm for Robot Navigation
    
    BFS explores the graph level by level, visiting all neighbors at the current depth
    before moving to nodes at the next depth level. This guarantees the shortest path
    in an unweighted graph.
    
    Time Complexity: O(V + E) where V is vertices and E is edges
    Space Complexity: O(V)
    """
    
    def __init__(self, grid: List[List[int]]):
        """
        Initialize BFS with a grid.
        
        Args:
            grid: 2D list where 0 = walkable, 1 = obstacle
        """
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0]) if grid else 0
        self.visited = set()
        self.path = []
        self.explored_nodes = []
    
    def is_valid(self, row: int, col: int) -> bool:
        """Check if a position is valid and walkable."""
        return (0 <= row < self.rows and 
                0 <= col < self.cols and 
                self.grid[row][col] == 0 and 
                (row, col) not in self.visited)
    
    def find_path(self, start: Tuple[int, int], goal: Tuple[int, int]) -> Optional[List[Tuple[int, int]]]:
        """
        Find the shortest path from start to goal using BFS.
        
        Args:
            start: Starting position (row, col)
            goal: Goal position (row, col)
        
        Returns:
            List of coordinates representing the path, or None if no path exists
        """
        if not self.is_valid(start[0], start[1]) or not self.is_valid(goal[0], goal[1]):
            return None
        
        self.visited.clear()
        self.path = []
        self.explored_nodes = []
        
        queue = deque([(start, [start])])
        self.visited.add(start)
        
        # Directions: up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while queue:
            (row, col), path = queue.popleft()
            self.explored_nodes.append((row, col))
            
            if (row, col) == goal:
                self.path = path
                return path
            
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                
                if self.is_valid(new_row, new_col):
                    self.visited.add((new_row, new_col))
                    new_path = path + [(new_row, new_col)]
                    queue.append(((new_row, new_col), new_path))
        
        return None
    
    def get_explored_nodes(self) -> List[Tuple[int, int]]:
        """Return list of explored nodes during search."""
        return self.explored_nodes
    
    def get_path_length(self) -> int:
        """Return the length of the found path."""
        return len(self.path) if self.path else 0