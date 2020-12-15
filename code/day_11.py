
data_string = "day_11_input_test.txt"

text_file = open(data_string, "r")
raw_input = text_file.read()
seat_layout    = raw_input.split('\n')  
text_file.close()

# . floor
# empty L
# occupied #

seat_status = {'floor': '.', 'empty': 'L', 'occupied': '#'}


# If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
# If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
# Otherwise, the seat's state does not change.
