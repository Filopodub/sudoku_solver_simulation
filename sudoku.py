class Sudoku:
    def __init__(self) -> None:
        # Initialize a 9x9 grid filled with zeros
        self.grid: list[list[int]] = [[0 for _ in range(9)] for _ in range(9)]

    def set_number(self, x: int, y: int, number: int) -> None:
        # Set a number in the Sudoku grid at the specified (x, y) position
        if 1 <= x <= 9 and 1 <= y <= 9 and 0 <= number <= 9:
            self.grid[y-1][x-1] = number
        else:
            raise ValueError("Invalid position or number")

    def display(self, grid: list[list[int]] = None) -> None:
        # Display the Sudoku grid with borders
        grid = grid if grid else self.grid
        border = "+-------+-------+-------+"
        for i, row in enumerate(grid):
            if i % 3 == 0:
                print(border)
            row_display = "| " + " ".join(
                str(num) if num != 0 else "." for num in row[:3]
            ) + " | " + " ".join(
                str(num) if num != 0 else "." for num in row[3:6]
            ) + " | " + " ".join(
                str(num) if num != 0 else "." for num in row[6:]
            ) + " |"
            print(row_display)
        print(border)

    def get_grid(self) -> list[list[int]]:
        # Return the current state of the grid
        return self.grid

    def reset(self) -> None:
        # Reset the grid to its initial state
        self.grid = [[0 for _ in range(9)] for _ in range(9)]
        
    def is_valid(self, grid: list[list[int]], row: int, col: int, num: int) -> bool:
        # Check if it's valid to place 'num' at position (row, col)
        # Check the row
        for x in range(9):
            if grid[row][x] == num:
                return False
        # Check the column
        for x in range(9):
            if grid[x][col] == num:
                return False
        # Check the 3x3 subgrid
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if grid[i + start_row][j + start_col] == num:
                    return False
        return True

    def solve_sudoku(self, grid: list[list[int]]) -> bool:
        # Solve the Sudoku using backtracking
        for row in range(9):
            for col in range(9):
                if grid[row][col] == 0:  # Find an empty cell
                    for num in range(1, 10):
                        if self.is_valid(grid, row, col, num):
                            grid[row][col] = num  # Place the number
                            if self.solve_sudoku(grid):
                                return True  # Return if successful
                            grid[row][col] = 0  # Backtrack if needed
                    return False  # Trigger backtracking
        return True

    def solve(self) -> list[list[int]]:
        # Create a copy of the grid to solve
        solved_grid = [row[:] for row in self.grid]
        if self.solve_sudoku(solved_grid):
            print("Sudoku solved successfully!")
        else:
            print("No solution exists.")
        return solved_grid
