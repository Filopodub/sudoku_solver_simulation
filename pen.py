from motor import Motor
from sudoku import Sudoku

class Pen:
    def __init__(self, motorx: Motor, motory: Motor, sudoku_grid: list[list[int]]) -> None:
        # Initialize the Pen with two motors and a reference to the Sudoku grid
        self.motorx = motorx
        self.motory = motory
        self.sudoku_grid = sudoku_grid

    def start_position(self) -> bool:
        # Ensure the pen is in the starting position (1,1)
        while self.motorx.get_position() != 1 or self.motory.get_position() != 1:
            self.move_position(1, 1)
        return True

    def get_position(self) -> None:
        # Print the current position of the pen
        print(f"X = {self.motorx.get_position()}, Y = {self.motory.get_position()}")

    def move_position(self, x: int, y: int) -> None:
        # Move the pen to the specified x, y position
        # Validate that the position is within the 1-9 range
        if not (1 <= x <= 9 and 1 <= y <= 9):
            print(f"Invalid position ({x}, {y})")
            return  # Exit the function if the position is invalid

        # Move the motors to the specified positions
        self.motorx.move_position(x)
        self.motory.move_position(y)
        self.get_position()  # Print the new position

    def read_number(self) -> int:
        # Simulate reading a number from the Sudoku grid at the current position
        x = self.motorx.get_position()
        y = self.motory.get_position()
        return self.sudoku_grid[y-1][x-1]  # Adjust for zero-based indexing
    
    def scan_sudoku(self, sudoku: Sudoku) -> None:
        # Scan the entire Sudoku grid and populate the Sudoku object
        print("Scan started!!!")
        for y in range(1, 10):  # Loop through y positions from 1 to 9
            # Determine the order of scanning for x based on the current y position
            x_range = range(1, 10) if y % 2 == 1 else range(9, 0, -1)
            for x in x_range:
                self.move_position(x, y)  # Move the pen to the current (x, y) position
                number = self.read_number()  # Read the number from the grid
                sudoku.set_number(x, y, number)  # Set the number in the Sudoku object
        print("Scan is done!!!")  # Indicate that the scan is complete
