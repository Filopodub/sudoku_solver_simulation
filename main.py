# Define a sample 9x9 Sudoku grid
sudoku_grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

              

from motor import Motor
from pen import Pen
from sudoku import Sudoku

# Initialize motors
motor1 = Motor()
motor2 = Motor()

# Create the Pen with the predefined Sudoku grid
pen = Pen(motor1, motor2, sudoku_grid)

# Initialize an empty Sudoku object
sudoku = Sudoku()

# Check if the pen is in the start position
if pen.start_position():
    print("Scan is ready")
    pen.get_position()

# Scan the Sudoku grid
pen.scan_sudoku(sudoku)

# Display the scanned Sudoku grid
sudoku.display()

