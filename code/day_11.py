
data_string = "day_11_input_test.txt"

text_file = open(data_string, "r")
raw_input = text_file.read()
seat_layout    = raw_input.split('\n')  
text_file.close()

# . floor
# empty L
# occupied #
class SeatStatus:
    
    def __init__(self, status):
    
        self.status = status

    def set_status(self, status):
        self.status = status

    def get_status(self):
        return self.status

class Seat:

    def __init__(self, layout):

        self.layout = layout 
        self.NUM_ROWS    = len(layout)
        self.NUM_COLS    = len(layout[0])

        self.seat_status = {'floor': '.', 'empty': 'L', 'occupied': '#'}
        # neighbours
        self.upLeft    = None
        self.up        = None
        self.upRight   = None 
        self.left      = None
        self.right     = None
        self.downLeft  = None
        self.down      = None
        self.downRight = None 

    def update_neighbours(self, row, col):

        if row > 0 and col > 0:
            self.upLeft = self.layout[row - 1][col - 1]
        else: 
            self.upLeft = None 

        if row > 0:
            self.up = self.layout[row - 1][col]
        else: 
            self.up = None

        if row > 0 and col <self.NUM_COLS - 1:
            self.upRight = self.layout[row-1][col+1]
        else: 
            self.upRight = None

        if col > 0:
            self.left = self.layout[row][col-1]
        else:
            self.left = None

        if col < self.NUM_COLS:
            self.right = self.layout[row][col + 1]
        else: 
            self.right = None

        if row < self.NUM_ROWS-1 and col > 0:
            self.downLeft = self.layout[row + 1][col - 1]
        else: 
            self.downLeft = None

        if row < self.NUM_ROWS - 1:
            self.down = self.layout[row + 1]
        else:
            self.down = None
        
        if row < self.NUM_ROWS - 1 and col < self.NUM_COLS -1:
            self.downRight = self.layout[row + 1][col + 1]
     
    def count_empty_neighbours
# If a seat is empty (L) and there are no occupied seats adjacent to it(benachbart), the seat becomes occupied.
# If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
# Otherwise, the seat's state does not change.

seat = Seat(seat_layout)

for row in seat_layout:
    for col in row:
        
        seat.update_neighbours(row, col)



