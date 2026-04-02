def dfs(graph, start, goal):
    stack = [start]
    visited = set()

    while stack:
        node = stack.pop()
        if node == goal:
            return True
        if node not in visited:
            visited.add(node)
            stack.extend(neighbor for neighbor in graph[node] if neighbor not in visited)

    return False

# Example usage:
if __name__ == '__main__':
    # Define a sample graph as a dictionary
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    start = 'A'
    goal = 'F'
    if dfs(graph, start, goal):
        print(f'Path found from {start} to {goal}!')
    else:
        print(f'No path found from {start} to {goal.')
