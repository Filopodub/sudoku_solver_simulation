class Pen:
    def __init__(self, motorx, motory, sudoku_grid):
        self.motorx = motorx
        self.motory = motory
        self.sudoku_grid = sudoku_grid

    def start_position(self):
        while self.motorx.get_position() != 1 or self.motory.get_position() != 1:
            self.move_position(1, 1)
        return True


    def get_position(self):
        print(self.motorx.get_position(), self.motory.get_position())

    def move_position(self, x, y):
        if not (1 <= x <= 9 and 1 <= y <= 9):
            print("Invalid position")
            return  # Exit the function if the position is invalid

        self.motorx.move_position(x)
        self.motory.move_position(y)
        self.get_position()

    def read_number(self):
        # Simulate reading a number from the Sudoku grid at the current position
        x = self.motorx.get_position()
        y = self.motory.get_position()
        return self.sudoku_grid[y-1][x-1]  # Adjust for zero-based indexing
    
    def scan_sudoku(self, sudoku):
        for y in range(1, 10):  # Loop through y positions from 1 to 9
            if y % 2 == 1:
                # For odd y values, move x from 1 to 9
                for x in range(1, 10):
                    self.move_position(x, y)
                    number = self.read_number()
                    sudoku.set_number(x, y, number)
            else:
                # For even y values, move x from 9 to 1
                for x in range(9, 0, -1):
                    self.move_position(x, y)
                    number = self.read_number()
                    sudoku.set_number(x, y, number)

        print("Scan is done!!!") 
