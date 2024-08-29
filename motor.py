class Motor:

    def __init__(self):
        self.pos = 1

    def start_position(self):
        if self.pos == 1:
            return True
        else:
            self.move_position(1)
            self.start_position()


    def get_position(self):
        return self.pos

    def move_position(self, pos):
        while(self.pos != pos):
            if(self.pos > pos):
                self.pos = self.pos - 1
            else:
                self.pos = self.pos + 1
            
