
import time 

data_string = "day_15_input.txt"

text_file = open(data_string, "r")
numbers = text_file.read()
numbers = numbers.split(',')

#numbers = [0,3,6] # 436
# numbers = [1,3,2] # 1
# numbers = [2,1,3] # 10
# numbers = [1,2,3] # 27
# numbers = [2,3,1] # 78
# numbers = [3,2,1] # 438
# numbers = [3,1,2] # 1836
numbers = [5,1,9,18,13,8,0] # NOTE: 376 is the correct answer

NUM_STARTING_NUMBERS = len(numbers)
GAME_LEN = 30000000 # 2020

# If that was the first time the number has been spoken, the current player says 0.
# Otherwise, the number had been spoken before; 
# the current player announces how many turns apart the number is from when it was previously spoken.

spoken = {}
idx = 1
for number in numbers:
    spoken[number] = [idx]
    idx += 1

idx = 0

# Play for 2020 turns and; what is the 2020th. number spoken
last_spoken = numbers[-1]
#numbers.pop(-1) #0,3,6
time0 = time.time()
for turn in range(NUM_STARTING_NUMBERS + 1, GAME_LEN + 1):
    
    # if turn%100000 == 0:
    #     print(turn)
    #     print(time.time() - time0)
    # Last number is new (it exist precisely once) 
    indices_last_spoken = spoken[last_spoken]

    # more than 1 index -> spoken before
    times_spoken = len(indices_last_spoken)

    # First time spoken 
    if times_spoken == 1:
        last_spoken = 0
    
    # Last number is new
    elif times_spoken >= 1:
        #just update when it was last spoken to have the youngest index saved
        diff = turn-1 - spoken[last_spoken][-2]
        last_spoken = diff

    # update indices and last spoken map
    if last_spoken in spoken:
        indices_last_spoken = spoken[last_spoken]
        indices_last_spoken = [indices_last_spoken[-1],turn]
    else:
        indices_last_spoken = []
        indices_last_spoken.append(turn)

    spoken[last_spoken] = indices_last_spoken

elapsed_time = time.time() -time0

print('2020th spoken number is: {}'.format(last_spoken)) 
print('elapsed time = {}'.format(elapsed_time)) # 0.005 - 0.01