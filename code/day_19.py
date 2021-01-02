import re 

data_string = "day_19_input_test.txt"

text_file = open(data_string, "r")
lines = text_file.read()
lines = lines.split('\n\n')

rulelines = lines[0].split('\n')


letter_pattern = re.compile(r'^(")([a-z])(")$')


rules = {}
a = 'a'
b = 'b'

# rules have either numbers or letters
for rule in rulelines:
    

    # Get rid of leading id in rule string
    ID, rule = int(rule.split(': ')[0]), rule.split(': ')[1]

    # single letters ("a"-"z")
    if match := re.search(letter_pattern, rule):
        letter = match.group()[1:-1]
        rules[ID] = letter

    # One or two possible sets of numbers
    else:
        numbers = rule.split()
        if '|' in numbers:
            subrules = rule.split(' | ')
            subrules = [list(map(int, number.split())) for number in subrules] 
        else:
            subrules = rule.split()
            subrules = [int(number) for number in subrules]

        rules[ID] = subrules


#any(isinstance(listitems, list) for listitems in list1)


messages = lines[1].split('\n')


def replaceValinTuple(oldTuple, index, values):
    newList = list(oldTuple)
    firstHalf = newList[:index]
    secondHalf = newList[index+1:]

    if type(values) != list:
        values = [values]

    newList = firstHalf + values + secondHalf
    

    return tuple(newList)

test = (1,2,3)
value = [2,3]
test = replaceValinTuple(test, 1, value)
print(test)
print()
def allMatchings(rules,  matchings):

    # macthings :set = {(a n1,...,ni, b), (...), (...)}
    for match in matchings:
        for char_idx, character in enumerate(match):
            
            # more subrules
            if type(character) == int:

                # retrieve string of rules with current ID character
                subrules = rules[character]

                # Multiple Subrules 
                if any(isinstance(listitems, list) for listitems in subrules):
                    
                    # put new rules in matching                     
                    firstrules  = subrules[0]
                    secondrules = subrules[1]

                    newmatch1 = match
                    newmatch2 = match

                    newmatch1 = replaceValinTuple(newmatch1, char_idx, firstrules)
                    newmatch2 = replaceValinTuple(newmatch2, char_idx, secondrules)

                    matchings.remove(match)
                    matchings.add(newmatch1)
                    matchings.add(newmatch2)

                # Single Subrules
                else:
                    newmatch = match
                    newmatch = replaceValinTuple(newmatch, char_idx, subrules)

                    matchings.remove(match)


                    matchings.add(newmatch)
                    
                    
                # TODO: recursive function calls
                    matchings = allMatchings(rules,  matchings)


            # letter digits are "ready"  
            else: 
                pass

    return matchings


    


# Part 1: How many messages match rule 1
numMachtesRule0 = 0
ZERO = {tuple(rules[0])}
matches = allMatchings(rules, ZERO)
for message in messages:

    if message in matches:
        numMachtesRule0 += 1
    
        



print(numMachtesRule0, 'messages match rule', ID)

