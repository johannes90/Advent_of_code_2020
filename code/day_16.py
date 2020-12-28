
import time 
import re
import copy
data_string = "day_16_input.txt"

text_file = open(data_string, "r")
ticket_info = text_file.read()
ticket_info = ticket_info.split('\n\n')

# messy formating of information
ticket_info[0]  = ticket_info[0].split('\n')
ticket_info[1]  = ticket_info[1].split('your ticket:\n')[-1].split(',')
ticket_info[2]  = ticket_info[2].split('nearby tickets:\n')[-1].split('\n')

RULES   = ticket_info[0]
YOUR_TICKET   = ticket_info[1]
NEARBY_TICKETS = [t.split(',') for t in ticket_info[2]]

class Rule:

    def __init__(self, rule_type, lower, upper):
        self.rule_type = rule_type
        self.lower = lower
        self.upper = upper
        self.range = {'lower': lower, 'upper': upper}

# format rules
rules = []
super_low = 1000000
super_up = 0
for rule in RULES:
    rule_type, ranges = rule.split(': ')
    ranges = ranges.split(' or ')
    lower = [int(r.split('-')[0]) for r in ranges]
    upper = [int(r.split('-')[1]) for r in ranges]

    rules.append(Rule(rule_type, lower, upper))


# eliminate invalid nearby tickets
invalid_indices = set()
invalid_values = []
invalid_sum = 0
for idx, nearby_ticket in enumerate(NEARBY_TICKETS):
    
    for value in nearby_ticket:
        value = int(value)

        # check if the value is inside ANY range
        valid_flag = False
        for rule in rules:
            if rule.lower[0] <= value <= rule.upper[0] or rule.lower[1] <= value <= rule.upper[1]:
                valid_flag = True
                break
            else:
                pass # value still invalid 
        
        # save invalid value, build sum
        if valid_flag == False:
            invalid_values.append(value)
            invalid_indices.add(idx)
            invalid_sum += value


print('invalid sum(Solution Part 1): ', invalid_sum)# 4, 55, 12max()

for index in sorted(invalid_indices, reverse=True):
    del NEARBY_TICKETS[index]

# Find the correct index for each range

# 1: All rules as a set of strings: r
positions = []

r = []
for rule in rules: 
    r.append(rule.rule_type)

# 2: build positions vector with 20 rule positions
for i in range(20):
    positions.append({'pos': i, 'rules': r.copy()}) 


# 3: loop thruogh all nearby tickets in the order that you only look at the first positions for all tickets, 
# than the second and so on
for i_position in range(len(positions)):

    # Loop through all tickets
    for i_ticket in range(len(NEARBY_TICKETS)):

        val = int(NEARBY_TICKETS[i_ticket][i_position])

        # Check for which rules the current value is valid
        for rule in rules: 
            
            if ((rule.lower[0]<= val <= rule.upper[0]) or (rule.lower[1] <= val <= rule.upper[1])):
                pass
            
            else:
                # remove rule from positions list and go to next rule
                positions[i_position]['rules'].remove(rule.rule_type)

# 5: 
# sort by num rules: sorted(positions, key=lambda x: len(x['rules']))
# sort by positions: sorted(positions, key=lambda x: (x['pos']))
positions = sorted(positions, key=lambda x: len(x['rules']))

for i_position in range(len(positions)):

    NUM_RULES = len(positions[i_position]['rules'])
            
    for i_other_positions in range(i_position+1,len(positions)):#[x for x in range(len(positions)) if x != i_position]:
        
        if positions[i_position]['rules'][0] in positions[i_other_positions]['rules']:                      
            positions[i_other_positions]['rules'].remove(positions[i_position]['rules'][0])


positions = sorted(positions, key=lambda x: (x['pos']))

departure_pattern = re.compile(r'')


departure_positions = []
for idx, position in enumerate(positions):

    if re.match(r"departure", position['rules'][0]):
        departure_positions.append(idx)

mul = 1
for _ in departure_positions:
    
    mul = mul*int(YOUR_TICKET[_])

print('Solution Part 2: ', mul)