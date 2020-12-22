data_string = "day_10_input_test.txt"

text_file = open(data_string, "r")
raw_input = text_file.read()
adapters    = raw_input.split('\n') 

adapters = [int(adapter) for adapter in adapters]
adapters = sorted(adapters)

from math import comb
comb(10,3) # 10 over 3; n over k

built_in_adapter = max(adapters) + 3 # 22

chargin_outlet = 0

chain = [chargin_outlet] + adapters + [built_in_adapter]



def find_diffs(chain):    
    return [chain[idx+1] - chain[idx] for idx in range(len(chain)-1)]

diffs = find_diffs(chain)

diff_1 = diffs.count(1)
diff_2 = diffs.count(2)
diff_3 = diffs.count(3)

print('solution to Part 1: diff_1*diff_3 = {}'.format(diff_1*diff_3)) # test: 35
# Part B:
# Count number of different feasible arangements such that chain[x] - chain[x-1] \in {1,2,3}

# 1: zählen wieviele Adapter entfernt werden können


#  3 4 5 6 7  10 11 12
#  3 4 5 6 7  10    12
#  3 4 5   7  10 11 12
#  3 4 5   7  10    12
#  3 4   6 7  10 11 12
#  3 4   6 7  10    12
#  3 4     7  10 11 12
#  3 4     7  10    12

# -> 2^3 = 8

def count_paths(chain):
    
    output = chain[-1]

    # num_ways[i] is the numbers of ways to get to i
    num_ways = [0] * (output + 1)

    num_ways[0] = 1

    if 1 in chain:
        num_ways[1] = 1

    if 2 in chain and 1 in chain:
        num_ways[2] = 2

    elif 2 in chain:
        num_ways[2] = 1

    for n in range(3, output + 1):
        if n not in chain:
            continue

        num_ways[n] = num_ways[n-3] + num_ways[n-2] + num_ways[n-1]

    return num_ways[output]


print(count_paths(chain))
# def create_chunks(chain, diffs):

#     CHUNKS = []
