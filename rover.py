class Rover:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

    def move(self):
        if self.direction == 'N':
            self.y += 1
        elif self.direction == 'S':
            self.y -= 1
        elif self.direction == 'E':
            self.x += 1
        elif self.direction == 'W':
            self.x -= 1

    def turn_left(self):
        if self.direction == 'N':
            self.direction = 'W'
        elif self.direction == 'S':
            self.direction = 'E'
        elif self.direction == 'E':
            self.direction = 'N'
        elif self.direction == 'W':
            self.direction = 'S'

    def turn_right(self):
        if self.direction == 'N':
            self.direction = 'E'
        elif self.direction == 'S':
            self.direction = 'W'
        elif self.direction == 'E':
            self.direction = 'S'
        elif self.direction == 'W':
            self.direction = 'N'

    def execute_commands(self, commands):
        for command in commands:
            if command == 'M':
                new_x, new_y = self.x, self.y

                if self.direction == 'N':
                    new_y += 1
                elif self.direction == 'S':
                    new_y -= 1
                elif self.direction == 'E':
                    new_x += 1
                elif self.direction == 'W':
                    new_x -= 1

                if (new_x, new_y) not in obstacles and 0 <= new_x < 10 and 0 <= new_y < 10:
                    self.x, self.y = new_x, new_y
            elif command == 'L':
                self.turn_left()
            elif command == 'R':
                self.turn_right()

    def get_status_report(self):
        return f"Rover is at ({self.x}, {self.y}) facing {self.direction}. No Obstacles detected."


class ObstacleGrid:
    def __init__(self, size, obstacles):
        self.size = size
        self.obstacles = obstacles

    def has_obstacle(self, x, y):
        return (x, y) in self.obstacles


# Initialize the Rover
rover = Rover(0, 0, 'N')

# Define the grid and obstacles
obstacles = [(2, 2), (3, 5)]
grid = ObstacleGrid((10, 10), obstacles)

# Execute commands
commands = ['M', 'M', 'R', 'M', 'L', 'M']
rover.execute_commands(commands)

# Check for obstacles and generate status report
if grid.has_obstacle(rover.x, rover.y):
    print("Rover detected an obstacle and cannot move.")
else:
    status_report = rover.get_status_report()
    print("Final Position:", (rover.x, rover.y, rover.direction))
    print("Status Report:", status_report)
