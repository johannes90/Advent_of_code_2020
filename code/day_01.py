# read data as txt file 
data_string = "day_01_input.txt"
text_file = open(data_string, "r")
lines = text_file.read().split('\n')
text_file.close()

# convert data into a list of strings
data = list(map(int, lines))

# brute force 
solution_A_found = False
solution_B_found = False
for int1 in data:
    for int2 in data:
        
        int_sum_A = int1 + int2  
        
        if int_sum_A == 2020 and solution_A_found == False:
            print('A: ', int1 * int2)
            solution_A_found = True
        #part b
        for int3 in data:
            int_sum_B = int1 + int2 + int3 

            if int_sum_B == 2020 and solution_B_found == False:
                print('B: ', int1 * int2 * int3)
                solution_B_found = True


# A: 876459
# B: 116168640