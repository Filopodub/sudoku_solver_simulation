class Sudoku:
    def __init__(self) -> None:
        # Initialize a 9x9 grid filled with zeros
        self.grid: list[list[int]] = [[0 for _ in range(9)] for _ in range(9)]

    def set_number(self, x: int, y: int, number: int) -> None:
        # Set a number in the Sudoku grid at the specified (x, y) position
        # Ensure x, y are within the valid range (1 to 9) and the number is between 0 and 9
        if 1 <= x <= 9 and 1 <= y <= 9 and 0 <= number <= 9:
            self.grid[y-1][x-1] = number  # Adjust for zero-based indexing
        else:
            raise ValueError("Invalid position or number")  # Raise an error for invalid inputs

    def display(self) -> None:
        # Display the Sudoku grid with borders to indicate 3x3 subgrids
        border = "+-------+-------+-------+"
        for i, row in enumerate(self.grid):
            if i % 3 == 0:
                print(border)  # Print the border at the start and every 3 rows
            
            # Display each row with vertical separators every 3 numbers
            row_display = "| " + " ".join(
                str(num) if num != 0 else "." for num in row[:3]
            ) + " | " + " ".join(
                str(num) if num != 0 else "." for num in row[3:6]
            ) + " | " + " ".join(
                str(num) if num != 0 else "." for num in row[6:]
            ) + " |"
            print(row_display)
        
        print(border)  # Print the bottom border

    def get_grid(self) -> list[list[int]]:
        # Return the current state of the Sudoku grid
        return self.grid

    def reset(self) -> None:
        # Reset the grid to its initial empty state (all zeros)
        self.grid = [[0 for _ in range(9)] for _ in range(9)]
