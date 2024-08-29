class Sudoku:
    def __init__(self):
        # Initialize a 9x9 grid filled with zeros
        self.grid = [[0 for _ in range(9)] for _ in range(9)]

    def set_number(self, x, y, number):
        # Ensure x and y are within the valid range (1 to 9)
        if 1 <= x <= 9 and 1 <= y <= 9 and 0 <= number <= 9:
            # Set the number in the grid at the specified position
            self.grid[y-1][x-1] = number
        else:
            print("Invalid position or number")

    def display(self):
        # Display the Sudoku grid with edges
        border = "+-------+-------+-------+"
        for i, row in enumerate(self.grid):
            if i % 3 == 0:
                print(border)
            
            # Prepare the row with vertical separators every 3 numbers
            row_display = "| " + " ".join(
                str(num) if num != 0 else "."
                for j, num in enumerate(row)
            )
            # Insert additional separators for 3x3 blocks
            row_display = row_display[:7] + " |" + row_display[7:13] + " |" + row_display[13:] + " |"
            print(row_display)
        
        # Print the bottom line of the grid
        print(border)

    def get_grid(self):
        # Return the current state of the grid
        return self.grid
