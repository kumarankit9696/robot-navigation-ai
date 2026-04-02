# Robot Navigation Algorithms Example Demonstrations

## Example 1: Basic Movement
### Description:
This example demonstrates basic movement of a robot in a 2D grid.

```python
class Robot:
    def __init__(self):
        self.position = (0, 0)  # Starting position at origin

    def move(self, direction):
        if direction == 'up':
            self.position = (self.position[0], self.position[1] + 1)
        elif direction == 'down':
            self.position = (self.position[0], self.position[1] - 1)
        elif direction == 'left':
            self.position = (self.position[0] - 1, self.position[1])
        elif direction == 'right':
            self.position = (self.position[0] + 1, self.position[1])

# Testing the robot movement
robot = Robot()
robot.move('up')  # Move up
print(robot.position)  # Should print (0, 1)
robot.move('right')  # Move right
print(robot.position)  # Should print (1, 1)
```

## Example 2: Obstacle Avoidance
### Description:
This example demonstrates obstacle avoidance using a simple algorithm.

```python
class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.obstacles = set()  # Set of obstacle positions

    def add_obstacle(self, position):
        self.obstacles.add(position)

    def is_obstacle(self, position):
        return position in self.obstacles

class RobotWithObstacles:
    def __init__(self, grid):
        self.grid = grid
        self.position = (0, 0)

    def move(self, direction):
        new_position = self.position
        if direction == 'up':
            new_position = (self.position[0], self.position[1] + 1)
        elif direction == 'down':
            new_position = (self.position[0], self.position[1] - 1)
        elif direction == 'left':
            new_position = (self.position[0] - 1, self.position[1])
        elif direction == 'right':
            new_position = (self.position[0] + 1, self.position[1])
        
        if not self.grid.is_obstacle(new_position):
            self.position = new_position

# Testing the obstacle avoidance
grid = Grid(5, 5)
grid.add_obstacle((1, 1))  # Add obstacle at (1, 1)
robot = RobotWithObstacles(grid)
robot.move('up')  # Move up to (0, 1)
robot.move('right')  # Move right to (1, 1) - should encounter obstacle
print(robot.position)  # Should still print (0, 1)
```

## Test Cases

def test_robot_movements():
    robot = Robot()
    robot.move('up')
    assert robot.position == (0, 1), "Test failed: Expected position (0, 1)"
    robot.move('down')
    assert robot.position == (0, 0), "Test failed: Expected position (0, 0)"
    robot.move('left')
    assert robot.position == (-1, 0), "Test failed: Expected position (-1, 0)"
    robot.move('right')
    assert robot.position == (0, 0), "Test failed: Expected position (0, 0)"


def test_obstacle_avoidance():
    grid = Grid(5, 5)
    grid.add_obstacle((1, 1))
    robot = RobotWithObstacles(grid)
    robot.move('up')  # Move to (0, 1)
    robot.move('right')  # Attempt to move to (1, 1)
    assert robot.position == (0, 1), "Test failed: Expected position (0, 1)"

# Run test cases

test_robot_movements()
test_obstacle_avoidance()
print("All tests passed!")