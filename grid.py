class Grid:
    """
    Represents a 2D grid for robot navigation.
    0 = free space, 1 = obstacle
    """
    def __init__(self, width, height, obstacles=None):
        self.width = width
        self.height = height
        self.grid = [[0 for _ in range(width)] for _ in range(height)]
        
        if obstacles:
            for x, y in obstacles:
                if 0 <= x < width and 0 <= y < height:
                    self.grid[y][x] = 1
    
    def is_obstacle(self, x, y):
        """Check if position contains an obstacle"""
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return True
        return self.grid[y][x] == 1
    
    def is_valid(self, x, y):
        """Check if position is valid and not an obstacle"""
        return not self.is_obstacle(x, y)
    
    def display(self, path=None, start=None, end=None):
        """Display the grid with optional path visualization"""
        display_grid = [row[:] for row in self.grid]
        
        # Mark path
        if path:
            for x, y in path[1:-1]:  # Exclude start and end
                if display_grid[y][x] == 0:
                    display_grid[y][x] = 2  # 2 = path
        
        # Mark start and end
        if start:
            display_grid[start[1]][start[0]] = 3  # 3 = start
        if end:
            display_grid[end[1]][end[0]] = 4  # 4 = end
        
        # Print
        symbols = {0: '.', 1: '#', 2: '*', 3: 'S', 4: 'E'}
        for row in display_grid:
            print(' '.join(symbols.get(cell, str(cell)) for cell in row))
        print()
    
    def get_neighbors(self, x, y):
        """Get valid neighboring positions (4-directional)"""
        neighbors = []
        # Up, Down, Left, Right
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if self.is_valid(nx, ny):
                neighbors.append((nx, ny))
        return neighbors
