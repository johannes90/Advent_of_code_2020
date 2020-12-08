data_string = "day_05_input.txt"
text_file = open(data_string, "r")
all_flight_passes = text_file.read().split('\n')
text_file.close()

max_ID = 0
IDs = []
for flight_pass in all_flight_passes:

    # convert both to binary 
    row = flight_pass[:7]
    row = int(row.replace("F", "0").replace("B", "1"), 2)
    col = flight_pass[7:]
    col = int(col.replace("L", "0").replace("R", "1"), 2)

    ID = 8*row + col
    IDs.append(ID)

    if ID > max_ID:
        max_ID = ID

# to find to missing number we utilize the fact that the IDs are a range of numbers, where my ID is the only missing 
IDs.sort()
my_ID = sum(range(IDs[0], IDs[-1]+1)) - sum(IDs)

print("row: ", row,  "col: ",  col, "max ID (solution part A): ", max_ID)
print("my ID (solution part B): ", my_ID)

