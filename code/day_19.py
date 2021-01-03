import re 
import itertools

data_string = "day_19_input.txt"

text_file = open(data_string, "r")
lines = text_file.read()

def parseInput(lines):

    lines = lines.split('\n\n')
    rulelines = lines[0].split('\n')

    letter_pattern = re.compile(r'^(")([a-z])(")$')
    rules = {}

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
                subrules = [[int(number) for number in subrules]]

            rules[ID] = subrules

    messages = lines[1].split('\n')

    return rules, messages


# Recursive search for all valid messages, memorizing IDs that we have seen before
def resolve_rules(rules, mem={}, ID=0):

    # ID seen before
    if ID in mem:
        return mem[ID]
    
    # Current rule
    rule = rules[ID]

    # Basecase: single letter
    if isinstance(rule, str):
        mem[ID] = rule
        return rule

    out = []
    # Go through all subrules; subrule = [[ID1, ID2, ID3]] or [[ID11, ID21, ID31],[ID12, ID22, ID32]] 
    for subrule in rule:
        
        #next_rules = [resolve_rules(rules, mem, next_i) for next_i in subrule] # NOTE: this does the same, but shorter
        next_rules= []
        for next_ID in subrule:
            next_rule = resolve_rules(rules, mem, next_ID)
            next_rules.append(next_rule)

        #print('next_rules', next_rules)
        #out.extend("".join(x) for x in itertools.product(*next_rules)) # NOTE: this does the same, but shorter
        for x in itertools.product(*next_rules): # itertool can produce all permutations in *temp
            
            #print(xx)
            X = ["".join(x)]
            out.extend(X)
    
    print('ID={} -> mem{}'.format(ID, out))
    mem[ID] = out
    return out

# Parse Input data
# rules: List[List[Int], str] 
# messages: List[str]
rules, messages = parseInput(lines)

# Part 1: How many messages match rule 1
validMessages = set(resolve_rules(rules))

numMachtesRule0 = 0

for message in messages:
    if message in validMessages:
        numMachtesRule0 += 1

print(numMachtesRule0, 'messages match rule', 0)

