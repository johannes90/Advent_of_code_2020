
data_string = "day_11_input.txt"
import copy

text_file = open(data_string, "r")
raw_input = text_file.read()
seat_layout    = raw_input.split('\n') 
rows = [] 
for row in seat_layout:
    rows.append(list(row)) 

text_file.close()
seat_layout = rows

FLOOR = '.'
EMPTY = 'L'
OCCUPIED = '#'

NUM_ROWS = len(seat_layout)
NUM_COLS = len(seat_layout[0])

def count_adj_neighbours(layout, row, col):

    occupied_neighbours = 0

    if row > 0 and col > 0:
        upLeft = layout[row - 1][col - 1]
        if upLeft == OCCUPIED:
            occupied_neighbours += 1   

    if row > 0:
        up = layout[row - 1][col]
        if up == OCCUPIED:
            occupied_neighbours += 1  
    
    if row > 0 and col <NUM_COLS - 1:
        upRight = layout[row-1][col+1]
        if upRight == OCCUPIED:
            occupied_neighbours += 1  

    if col > 0:
        left = layout[row][col-1]
        if left == OCCUPIED:
            occupied_neighbours += 1

    if col < NUM_COLS-1:
        right = layout[row][col + 1]
        if right == OCCUPIED:
            occupied_neighbours += 1

    if row < NUM_ROWS-1 and col > 0:
        downLeft = layout[row + 1][col - 1]
        if downLeft == OCCUPIED:
            occupied_neighbours += 1

    if row < NUM_ROWS - 1:
        down = layout[row + 1][col]
        if down == OCCUPIED:
            occupied_neighbours += 1
    
    if row < NUM_ROWS - 1 and col < NUM_COLS -1:
        downRight = layout[row + 1][col + 1]
        if downRight == OCCUPIED:
            occupied_neighbours += 1

    return occupied_neighbours

def update_seat(seat, occupied_neighbours):
    # If a seat is empty (L) and there are no occupied seats adjacent to it(benachbart), the seat becomes occupied.
    # If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
    # Otherwise, the seat's state does not change.
    if seat == EMPTY and occupied_neighbours == 0:
        return OCCUPIED

    elif seat == OCCUPIED and occupied_neighbours >= 4:
        return EMPTY

    elif seat == FLOOR:
        return FLOOR

    else: 
        return seat

has_changed = True

for s in seat_layout:
    print(''.join(s))

print('\n\n')

# rules are applied to every seat simultaneously:
new_layout = copy.deepcopy(seat_layout)

while has_changed:
    has_changed = False
    for row_ind, row in enumerate(seat_layout):
        for col_ind, seat in enumerate(row):
            
            occupied_neighbours = count_adj_neighbours(seat_layout, row_ind, col_ind) 
            
            new_seat = update_seat(seat, occupied_neighbours)

            new_layout[row_ind][col_ind] = new_seat

            if new_seat != seat:
                has_changed = True


    # Update layout 
    seat_layout = copy.deepcopy(new_layout)

    # Display after one cycle
    for s in seat_layout:
        print(''.join(s))

    print('\n\n\n')

# Count occupied seats after stabilization
occupied = 0
for row in seat_layout:
    for seat in row:
        if seat == OCCUPIED:
            occupied += 1

print('Process stabilized {} seats are occupied'.format(occupied))
