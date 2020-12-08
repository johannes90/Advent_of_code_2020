import re # regular expressions

# read data as txt file 
data_string = "day_02_input.txt"
text_file = open(data_string, "r")
lines = text_file.read().split('\n')
text_file.close()

#1-3 a: abcde

lines = list((map(lambda password: re.split('\\-|: | ',password),  lines)))

# part 1: count occurences of given letter
count = 0
for line in lines:
    lower = int(line[0]) 
    upper = int(line[1])
    character = line[2]
    password_candidate = line[3]

    # count occurences of letter in password_candidate
    occurences = password_candidate.count(character)

    # check if the candidate matches the policy
    if lower <= occurences and upper >= occurences:
        count += 1
    else: 
        continue

# part 2:
count2 = 0
for line in lines:
    index_1 = int(line[0]) - 1
    index_2 = int(line[1]) - 1 
    character = line[2]

    password_candidate = line[3]
    character_1 = password_candidate[index_1]
    character_2 = password_candidate[index_2]

    # check condition if either one OR the other character is 
    if (character == character_1) ^ (character == character_2):
        count2 += 1


print(count)
# test