import re 

data_string = "day_18_input.txt"

text_file = open(data_string, "r")
lines = text_file.read()
lines = lines.split('\n')

ADD = '+'
MUL = '*'

innerParanthesisPattern =  re.compile(r"\([^()]+\)")

# Evaluate an expression without paranthesis
def evalParanthesisExpression(ParanthesisExpression, Plus):
    
    # Replace all paranthesises with its solution if any 
    while (re.search(innerParanthesisPattern, ParanthesisExpression)):

        # 1: Find all paranthesis, 
        match = re.search(innerParanthesisPattern, ParanthesisExpression)

        # 2: Extract inside of first paranthesis = linear expression
        linearExpression = match.group()[1:-1].split()

        # 3: solve resulting linear expression
        if Plus == True:
            linearSolution = evalLinearExpressionPlus(linearExpression)
        else:
            linearSolution = evalLinearExpression(linearExpression)

        # 4: replace paranthesis with solution
        ParanthesisExpression = ParanthesisExpression[:match.start()] + str(linearSolution) + ParanthesisExpression[match.end():]
        
    else:
        linearExpression = ParanthesisExpression.split()

        if Plus == True:
            linearSolution = evalLinearExpressionPlus(linearExpression)
        else:
            linearSolution = evalLinearExpression(linearExpression)

        return linearSolution

def evalLinearExpression(linearExpression):
    # We assume the expression to be of the following form:
    # [INT_1, OPERATOR_1, INT_2, OPERATOR_2, INT_3 , ... OPERATOR_N-1, INT_N],
    # where OPERATOR_i \in {ADD, MUL}

    # Evaluate iteratively from left to right
    solution = int(linearExpression.pop(0))
    for idx in range(0, len(linearExpression)-1, 2):
        
        operator = linearExpression[idx]

        if operator == ADD: 

            solution += int(linearExpression[idx + 1])

        elif operator == MUL: 

            solution  *= int(linearExpression[idx + 1])
        else: 
            raise ValueError('Wrong operator! Allowed are: \'+\' or \'*\', but got: ', operator)

    return solution


def evalLinearExpressionPlus(linearExpression):
    
    if type(linearExpression) == str:
        linearExpression = linearExpression.split()
    # Iteratively remove all Parts of (INT_i + INT_i+1) -> Solution
    while ADD in linearExpression:
        
        # Find index of addition and retrieve both operands left and right
        addInd = linearExpression.index(ADD)
        operand1 = linearExpression[addInd - 1]
        operand2 = linearExpression[addInd + 1]

        # Compute the sum
        solution = [str(int(operand1) + int(operand2))]

        # Insert solution in string
        linearExpression = linearExpression[:addInd - 1] + solution + linearExpression[addInd + 2:]
        #print(*linearExpression)
    else: 
        solution = evalLinearExpression(linearExpression)

        return solution

test ="1 + 2 * 3 + 4 * 5 + 6"

test_sol = evalParanthesisExpression(test, False)


solutionSum = 0 
for line in lines:
    print(line)
    solutionSum += evalParanthesisExpression(line, False)

print('Solution part 1: ',solutionSum)


# Part 2: addition is evaluated before multiplication
test ="1 + 2 * 3 + 4 * 5 + 6"

test_sol = evalLinearExpressionPlus(test)


solutionSum = 0 
for line in lines:
    sol = evalParanthesisExpression(line, True)
    solutionSum += sol
    print(line, '=', sol)

print('Solution part 2: ',solutionSum)
