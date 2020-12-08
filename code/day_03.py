data_string = "day_03_input.txt"
text_file = open(data_string, "r")
lines = text_file.read().split('\n')
text_file.close()

# slopes
DX = [1, 3, 5, 7, 1]
DY = [1, 1, 1, 1, 2]

list_hit_trees = []
score = 1
# check all slopes 
for i in range(len(DX)):

    # init position and slope
    x = 0 
    y = 0

    dx = DX[i]
    dy = DY[i]

    hit_trees = 0

    # go through map
    while y + dy < len(lines):
        
        # move one step
        x = (x + dx) % len(lines[0])
        y += dy
        ground = lines[y][x] 

        # count if you hit a tree 
        if ground == "#":
            hit_trees += 1

    score = score*hit_trees

print(score)