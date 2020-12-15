import re  

data_string = "day_07_input.txt"

text_file = open(data_string, "r")
raw_input = text_file.read()
rules    = raw_input.split('\n')  
text_file.close()

class Children:
    def __init__(self, colors, quantities):

        if type(colors) == str:
            colors = [colors]
            quantities = [quantities]

        self.colors     = colors
        self.quantities = quantities

    def extend(self, children):
        for idx in range(len(children.colors)):

            c = children.colors[idx]
            q = children.quantities[idx]

            # update quantity of color if color exists
            if c in self.colors:
                i = self.colors.index(c)
                self.quantities[i] = self.quantities[i] + q
            else:
                self.colors.append(c)
                self.quantities.append(q)

class Bag:
    def __init__(self, color: str, cildren: Children):
        
        self.color    = color    # parent bag
        self.children = children # contained children bags

child1 = Children('blue', 1)
child2 = Children(['blue', 'green'], [2, 3])


child3 = Children([], [])
child3.extend(child1)
child3.extend(child2)
print()

# 1,2: parsing, build graph  
BAGS = []
for line in rules:

    (parent_string, children_string) = line.split(' bags contain ')

    # store child and parent and connect
    parent = parent_string

    if children_string == 'no other bags.':
        children = Children('no other bags', 0)

    else: 
        children_strings = children_string[:-1].split(", ")
        quantity = []
        color_c = []
        for child in children_strings:

            quantity.append(int(child[0]))
            child = re.sub(r" bags| bag", "", child) #remove "bags(s)"
            child = re.sub(r"\d ", "", child)        # remove number and whitespace
            color_c.append(child)

        children  = Children(color_c, quantity)


    BAGS.append(Bag(parent, children))

#  Test: Parsing 
for idx, bag in enumerate(BAGS): 
    print('{} {} {} {}'.format(idx, bag.color, bag.children.colors, bag.children.quantities) ) 
print()
def find_parents(bags: list, children: str):

    if type(children) == str:
        children = [children] 
    parents = set()

    for c in children: 
        for bag in bags:
            if c in bag.children.colors:#bag.children['color']:
                parents.add(bag.color)
        
    return parents

# Test: find parents for 
parents_of_muted_yellow = find_parents(BAGS, 'muted yellow')

# bags = all bags we search the parents
# child = shiny gold at beginning, then next parent of shiny gold and so on
# all parents = empty set at start, then set of found parents
def find_all_parents(bags, child, all_parents): 
    
    if len(find_parents(bags, child)) == 0: #Rekursion stoppen bei "child" hat keinen parent TODO:oder parent is geschwister von shiny gold -> könnte ich dafür einfach alle Geschwister von shiny gold löschen ganz zu Beginn? 
        return all_parents 
    else:
        current_new_parents = find_parents(bags, child) 
        all_parents = all_parents.union(current_new_parents)
        return find_all_parents(bags, current_new_parents, all_parents) 

ALL_PARRENTS = find_all_parents(BAGS, 'shiny gold', set())

"""
    Solution Part A
"""
print("{} bags can eventually contain a shiny gold bag".format(len(ALL_PARRENTS)))

""" 
    Part: B
"""
def find_children(bags, parents):

    # parents: list[Bag]
    
    if type(parents) == str:
        parents = [parents] 
        quantity = [1]
    else: 
        quantity = parents.quantities
        parents = parents.colors

    children = Children([], [])

    for idx, p in enumerate(parents): 
        q = quantity[idx]
        for bag in bags:
            if p in bag.color and bag.children.colors != 'no other bags':

                
                children.colors.extend(bag.children.colors)

                new_quantities = [i * q for i in bag.children.quantities]
                children.quantities.extend(new_quantities)
                #children.quantities.extend(bag.children.quantities*q)
                #TODO: can we break out here because every parent bag exists only once?
    return children

#  Test: vibrant plum
#  ground truth: 5 faded blue bags and 6 dotted black bags
vibrant_plum_children = find_children(BAGS, 'vibrant plum') # NOTE: works
shiny_gold_children = find_children(BAGS, 'shiny gold') # NOTE: works
dotted_black_children = find_children(BAGS, 'dotted black') # NOTE: works

print("Test: vibrant plum contains {}".format(vibrant_plum_children) )

def find_all_children(bags, parents, all_children):

    current_new_children = find_children(bags, parents)

    if current_new_children.colors == []: 
        return all_children 

    else:
        all_children.extend(current_new_children)
        return find_all_children(bags, current_new_children, all_children) 


all_children = Children([], [])
shiny_gold_all_children = find_all_children(BAGS, 'shiny gold', all_children)

#count numer of children bags
number_of_children = shiny_gold_all_children.quantities

sol = 0
for number in number_of_children:
    sol += number
print('Solution: {}'.format(sol)) #465 to low 1469 