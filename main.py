from motor import Motor
from pen import Pen
from sudoku import Sudoku

# Define a sample 9x9 Sudoku grid with some predefined numbers
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

# Initialize the motors for the x and y axes
motor1 = Motor()
motor2 = Motor()

# Create the Pen object with the predefined Sudoku grid
pen = Pen(motor1, motor2, sudoku_grid)

# Initialize an empty Sudoku object to hold the scanned grid
sudoku = Sudoku()

# Check if the pen is in the start position (1, 1)
if pen.start_position():
    print("Scan is ready")  # Notify that the scan is ready to start
    pen.get_position()  # Display the current position of the pen

# Start scanning the Sudoku grid
pen.scan_sudoku(sudoku)

# Display the scanned Sudoku grid
print("Original Sudoku grid:")
sudoku.display()

# Solve the Sudoku and display the solution
solved_grid = sudoku.solve()
print("\nSolved Sudoku grid:")
sudoku.display(solved_grid)


