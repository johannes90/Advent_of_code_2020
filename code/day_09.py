
data_string = "day_09_input.txt"

text_file = open(data_string, "r")
raw_input = text_file.read()
all_numbers    = raw_input.split('\n')  
text_file.close()

all_numbers = list(map(lambda number: int(number), all_numbers))

NUM_PREAMBLE = 25
NUM_PREAMBLE_TEST = 5

def is_sum(numbers, sum_candidate):
    for idx, summand_1 in enumerate(numbers): # TODO: can we use code of day 1?
        for summand_2 in numbers[idx + 1:]:
            
            if summand_1 + summand_2 == sum_candidate:
                return (summand_1, summand_2)

    return False

def find_first_invalid(all_numbers, num_preamble):
    for idx, number in enumerate(all_numbers):

        if idx >= num_preamble: # skip preambel
            numbers = all_numbers[idx-num_preamble:idx]
            
            if is_sum(numbers, number) == False:
                return number

first_invalid = find_first_invalid(all_numbers, NUM_PREAMBLE)

print("Solution Part A: {}".format(first_invalid))

# contiguous = zusammenhängend

def find_contigous_set(all_numbers, num_preamble, first_invalid):


    for start in range(len(all_numbers)):
        
        for end in range(start + 1,len(all_numbers)):

            window = all_numbers[start:end+1]

            if sum(window) == first_invalid:
                return (min(window), max(window))
            
            elif sum(window) > first_invalid:
                break
            
            else:
                pass

        
#(first, last) = find_contigous_set(all_numbers, NUM_PREAMBLE_TEST, first_invalid)
(first, last) = find_contigous_set(all_numbers, NUM_PREAMBLE, first_invalid)


print("Solution part B: {}".format(first + last))
