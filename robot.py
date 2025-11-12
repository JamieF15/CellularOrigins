from table import table

class robot:
    DIRECTIONS = ["NORTH", "EAST", "SOUTH", "WEST"]
    TABLE = table()
    
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.is_on_table = True

    def report(self):
        print(f"{self.x}, {self.y}, {self.direction}")

    def set_robot_on_table(self, is_on_table):
        self.is_on_table = is_on_table
    
    def get_is_on_table(self):
        return self.is_on_table
    
    def set_direction(self, direction):
        self.direction = direction

    def get_direction(self):
        return self.direction   

    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y   

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y  

    def invoke_movement_commands(self, commands):

        if not self.get_is_on_table():
            print("Robot is not on the table. Cannot execute movement commands.")
            return

        for command in commands:
            if command == "MOVE":
                new_x = self.x
                new_y = self.y
                
                if self.direction == "NORTH":
                    new_y = self.get_y() + 1

                elif self.direction == "EAST":
                    new_x = self.get_x() + 1

                elif self.direction == "SOUTH":
                    new_y = self.get_y() - 1

                elif self.direction == "WEST":
                    new_x = self.get_x() - 1
                
                # Check if the new position is within the table bounds
                if self.TABLE.position_is_valid(new_x, new_y):
                    self.set_x(new_x)
                    self.set_y(new_y)
                else:
                    print(f"Warning: Movement blocked. Would move to ({new_x}, {new_y}) which is off the table.")

            elif command == "LEFT":
                current_index = self.DIRECTIONS.index(self.direction)              
                
                # current_index - The index of the current direction in the DIRECTIONS list

                # NORTH = 0, EAST = 1, SOUTH = 2, WEST = 3
                # current_index - 1 - Subtract 1 to get the previous direction (left rotation)

                # If facing NORTH (0): 0 - 1 = -1
                # If facing EAST (1): 1 - 1 = 0
                # If facing SOUTH (2): 2 - 1 = 1
                # If facing WEST (3): 3 - 1 = 2
                # % 4 - The modulo operator wraps around when we go below 0

                # -1 % 4 = 3 (wraps to WEST)
                # 0 % 4 = 0 (stays at NORTH)
                # 1 % 4 = 1 (stays at EAST)
                # 2 % 4 = 2 (stays at SOUTH)
                
                self.set_direction(self.DIRECTIONS[(current_index - 1) % 4])

            elif command == "RIGHT":
                current_index = self.DIRECTIONS.index(self.direction)
                self.set_direction(self.DIRECTIONS[(current_index + 1) % 4])

            elif command == "REPORT":
                self.report()

