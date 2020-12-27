
import time 

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
print()

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
invalid = []
invalid_sum = 0
for nearby_ticket in NEARBY_TICKETS:
    print(nearby_ticket)
    
    for value in nearby_ticket:
        value = int(value)
        print(value)

        # check if the value is inside ANY range
        valid_flag = False
        for rule in rules:
            if ((value >= rule.lower[0] and value <= rule.upper[0]) or ( value >= rule.lower[1] and value <= rule.upper[1])):
                valid_flag = True
                break
            else:
                pass # value still invalid 
        
        # save invalid value, build sum
        if valid_flag == False:
            invalid.append(value)
            invalid_sum += value


print('invalid numbers: ', invalid)# 4, 55, 12
print('invalid sum(Solution Part 1): ', invalid_sum)# 4, 55, 12