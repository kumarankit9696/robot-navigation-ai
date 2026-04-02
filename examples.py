from robot import Robot
from grid import Grid

def visualize_path(grid, path, start, goal):
    """Visualize the path on the grid"""
    visual_grid = [['.' for _ in range(grid.width)] for _ in range(grid.height)]
    
    # Mark obstacles
    for (x, y) in grid.obstacles:
        visual_grid[y][x] = 'X'
    
    # Mark path
    if path:
        for (x, y) in path:
            if (x, y) != start and (x, y) != goal:
                visual_grid[y][x] = '*'
    
    # Mark start and goal
    start_x, start_y = start
    goal_x, goal_y = goal
    visual_grid[start_y][start_x] = 'S'
    visual_grid[goal_y][goal_x] = 'G'
    
    # Print grid
    for row in visual_grid:
        print(' '.join(row))

def example_1_simple_pathfinding():
    """Example 1: Simple pathfinding without obstacles"""
    print("=" * 50)
    print("Example 1: Simple Pathfinding (No Obstacles)")
    print("=" * 50)
    
    # Create a 5x5 grid
    grid_data = [[0 for _ in range(5)] for _ in range(5)]
    robot = Robot(grid_data)
    
    start = (0, 0)
    goal = (4, 4)
    
    print(f"\nStart: {start}, Goal: {goal}\n")
    
    # BFS
    print("BFS Path:")
    bfs_path = robot.bfs(start, goal)
    print(bfs_path)
    print(f"Path length: {len(bfs_path) if bfs_path else 'No path found'}\n")
    
    # DFS
    print("DFS Path:")
    dfs_path = robot.dfs(start, goal)
    print(dfs_path)
    print(f"Path length: {len(dfs_path) if dfs_path else 'No path found'}\n")
    
    # A*
    print("A* Path:")
    astar_path = robot.a_star(start, goal)
    print(astar_path)
    print(f"Path length: {len(astar_path) if astar_path else 'No path found'}\n")

def example_2_pathfinding_with_obstacles():
    """Example 2: Pathfinding with obstacles"""
    print("=" * 50)
    print("Example 2: Pathfinding With Obstacles")
    print("=" * 50)
    
    # Create a 10x10 grid
    grid_data = [[0 for _ in range(10)] for _ in range(10)]
    robot = Robot(grid_data)
    
    start = (0, 0)
    goal = (9, 9)
    
    # Add obstacles (create a wall)
    for i in range(1, 8):
        grid_data[5][i] = 1  # Create a horizontal wall
    grid_data[5][7] = 0  # Create a gap in the wall
    
    print(f"\nStart: {start}, Goal: {goal}\n")
    print("Grid with obstacles (1 = obstacle):")
    for row in grid_data:
        print(row)
    print() 
    
    # BFS with obstacles
    print("BFS Path (with obstacles):")
    bfs_path = robot.bfs(start, goal)
    print(bfs_path)
    print(f"Path length: {len(bfs_path) if bfs_path else 'No path found'}\n")
    
    # A* with obstacles
    print("A* Path (with obstacles):")
    astar_path = robot.a_star(start, goal)
    print(astar_path)
    print(f"Path length: {len(astar_path) if astar_path else 'No path found'}\n")

def example_3_performance_comparison():
    """Example 3: Compare performance of different algorithms"""
    print("=" * 50)
    print("Example 3: Algorithm Performance Comparison")
    print("=" * 50)
    
    import time
    
    grid_data = [[0 for _ in range(20)] for _ in range(20)]
    robot = Robot(grid_data)
    
    start = (0, 0)
    goal = (19, 19)
    
    # BFS Performance
    start_time = time.time()
    bfs_path = robot.bfs(start, goal)
    bfs_time = time.time() - start_time
    
    # DFS Performance
    start_time = time.time()
    dfs_path = robot.dfs(start, goal)
    dfs_time = time.time() - start_time
    
    # A* Performance
    start_time = time.time()
    astar_path = robot.a_star(start, goal)
    astar_time = time.time() - start_time
    
    print(f"\nGrid Size: 20x20")
    print(f"Start: {start}, Goal: {goal}\n")
    print(f"{'Algorithm':<10} {'Path Length':<15} {'Time (ms)':<15}")
    print("-" * 40)
    print(f"{'BFS':<10} {len(bfs_path) if bfs_path else 'N/A':<15} {bfs_time*1000:<15.4f}")
    print(f"{'DFS':<10} {len(dfs_path) if dfs_path else 'N/A':<15} {dfs_time*1000:<15.4f}")
    print(f"{'A*':<10} {len(astar_path) if astar_path else 'N/A':<15} {astar_time*1000:<15.4f}")

if __name__ == '__main__':
    example_1_simple_pathfinding()
    print("\n")
    example_2_pathfinding_with_obstacles()
    print("\n")
    example_3_performance_comparison()