class Robot:
    def __init__(self, grid):
        self.grid = grid  # 2D list representing the grid
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0

    def bfs(self, start, goal):
        from collections import deque
        queue = deque([start])
        visited = set()
        visited.add(start)
        came_from = {start: None}

        while queue:
            current = queue.popleft()
            if current == goal:
                return self.reconstruct_path(came_from, current)
            for neighbor in self.get_neighbors(current):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    came_from[neighbor] = current
        return None  # Path not found

    def dfs(self, start, goal):
        stack = [start]
        visited = set()
        came_from = {start: None}

        while stack:
            current = stack.pop()
            if current == goal:
                return self.reconstruct_path(came_from, current)
            if current not in visited:
                visited.add(current)
                for neighbor in self.get_neighbors(current):
                    if neighbor not in visited:
                        stack.append(neighbor)
                        came_from[neighbor] = current
        return None  # Path not found

    def a_star(self, start, goal):
        from queue import PriorityQueue
        open_set = PriorityQueue()
        open_set.put((0, start))
        came_from = {start: None}
        g_score = {start: 0}
        f_score = {start: self.heuristic(start, goal)}

        while not open_set.empty():
            current = open_set.get()[1]
            if current == goal:
                return self.reconstruct_path(came_from, current)
            for neighbor in self.get_neighbors(current):
                tentative_g_score = g_score[current] + 1  # Assuming all edges have weight 1
                if tentative_g_score < g_score.get(neighbor, float('inf')):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + self.heuristic(neighbor, goal)
                    if neighbor not in [i[1] for i in open_set.queue]:
                        open_set.put((f_score[neighbor], neighbor))
        return None  # Path not found

    def heuristic(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])  # Manhattan distance

    def get_neighbors(self, node):
        x, y = node
        neighbors = []
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if 0 <= x + dx < self.rows and 0 <= y + dy < self.cols:
                neighbors.append((x + dx, y + dy))
        return neighbors

    def reconstruct_path(self, came_from, current):
        total_path = [current]
        while current in came_from:
            current = came_from[current]
            if current is not None:
                total_path.append(current)
        return total_path[::-1]  # Return reversed path
