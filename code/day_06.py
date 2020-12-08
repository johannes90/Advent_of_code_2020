
data_string = "day_06_input.txt"
#data_string = "day_04_input_test_4valid.txt"  # 4 valid passports
#data_string = "day_04_input_test_invalid.txt" # 4 invalid passports

text_file = open(data_string, "r")
raw_input = text_file.read()
groups    = raw_input.split('\n\n') # empty line = 2 new lines in a row 
text_file.close()

all_groups = list((map( lambda group: group.split("\n"),  groups))) 
# list of lists 
# number of lists = number of groups
# elemts in a list = number of poeple in that group   

# Task: count number of questions to which anyone answered yes and take the sum of all groups 
# Per Group (list) -> count different questions -> put every question in a set and count elements in the set = solution

all_groups_answers = 0
all_groups_answers_B = 0
for group in all_groups:

    group_answers = set()
    answers_current_person = 0
    count = 0
    for person in group:

        count += 1
        person_answers = set(person) 
        group_answers = group_answers.union(person_answers) # anyone 
        
        #TODO: I could use the whole alphabet as "empty set" for intersection for a nicer solution 
        if count == 1:
            group_answers_B = person_answers
        else:   
            group_answers_B = group_answers_B.intersection(person_answers) # everyone

    num_group_answers = len(group_answers) 
    all_groups_answers += num_group_answers

    num_group_answers_B = len(group_answers_B) 
    #print(num_group_answers_B)
    all_groups_answers_B += num_group_answers_B

# Test case : 

print("solution task A (anyone): ",all_groups_answers) 


print("solution task B (everyone): ",all_groups_answers_B) 

