class Motor:
    def __init__(self) -> None:
        # Initialize the motor's position to 1
        self.pos: int = 1

    def start_position(self) -> bool:
        # Move the motor to position 1 if it's not already there
        while self.pos != 1:
            self.move_position(1)
        return True

    def get_position(self) -> int:
        # Return the current position of the motor
        return self.pos

    def move_position(self, pos: int) -> None:
        # Move the motor to the specified position
        # If the current position is less than the target, move forward
        # If the current position is greater than the target, move backward
        step = 1 if self.pos < pos else -1
        while self.pos != pos:
            self.pos += step
