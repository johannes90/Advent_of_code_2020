import re 

data_string = "day_18_input.txt"

text_file = open(data_string, "r")
lines = text_file.read()
lines = lines.split('\n')

ADD = '+'
MUL = '*'

innerParanthesisPattern =  re.compile(r"\([^()]+\)")

# Evaluate an expression without paranthesis
def evalParanthesisExpression(ParanthesisExpression):
    
    # Replace all paranthesises with its solution if any 
    while (re.search(innerParanthesisPattern, ParanthesisExpression)):

        # 1: Find all paranthesis, 
        match = re.search(innerParanthesisPattern, ParanthesisExpression)

        # 2: Extract inside of first paranthesis = linear expression
        linearExpression = match.group()[1:-1].split()

        # 3: solve resulting linear expression
        linearSolution = evalLinearExpression(linearExpression)

        # 4: replace paranthesis with solution
        ParanthesisExpression = ParanthesisExpression[:match.start()] + str(linearSolution) + ParanthesisExpression[match.end():]
        
        
    else:

        linearExpression = ParanthesisExpression.split()

        linearSolution = evalLinearExpression(linearExpression)

        return linearSolution

def evalLinearExpression(LinearExpression):
    # We assume the expression to be of the following form:
    # [INT_1, OPERATOR_1, INT_2, OPERATOR_2, INT_3 , ... OPERATOR_N-1, INT_N],
    # where OPERATOR_i \in {ADD, MUL}

    # Evaluate iteratively from left to right
    solution = int(LinearExpression.pop(0))
    for idx in range(0, len(LinearExpression)-1, 2):
        
        operator = LinearExpression[idx]

        if operator == ADD: 

            solution += int(LinearExpression[idx + 1])

        elif operator == MUL: 

            solution  *= int(LinearExpression[idx + 1])
        else: 
            raise ValueError('Wrong operator! Allowed are: \'+\' or \'*\', but got: ', operator)

    return solution

test ="1 + 2 * 3 + 4 * 5 + 6"

test_sol = evalParanthesisExpression(test)


solutionSum = 0 
for line in lines:
    print(line)
    solutionSum += evalParanthesisExpression(line)

print(solutionSum)