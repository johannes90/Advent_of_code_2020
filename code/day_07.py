import re  

data_string = "day_07_input_test.txt"

text_file = open(data_string, "r")
raw_input = text_file.read()
rules    = raw_input.split('\n')  
text_file.close()

class Bag:
    def __init__(self, color: str, cildren: dict):
        
        self.color    = color    # parent bag
        self.children = children # contained children bags



# 1,2: parsing, build graph  
BAGS = []
for line in rules:

    (parent_string, children_string) = line.split(' bags contain ')

    # store child and parent and connect
    parent = parent_string

    if children_string == 'no other bags.':
        children = {'color': 'no other bags', 'quantity': 0}

    else: 
        children_strings = children_string[:-1].split(", ")
        quantity = []
        color_c = []
        for child in children_strings:

            quantity.append(int(child[0]))
            child = re.sub(r" bags| bag", "", child) #remove "bags(s)"
            child = re.sub(r"\d ", "", child)        # remove number and whitespace
            color_c.append(child)

        children = {'color': color_c, 'quantity': quantity}

    BAGS.append(Bag(parent, children))

#  Test: Parsing 
for idx, bag in enumerate(BAGS): 
    print('{} {} {} {}'.format(idx, bag.color, bag.children['color'], bag.children['quantity']) ) 
print()
def find_parents(bags: list, children: str):

    if type(children) == str:
        children = [children] 
    parents = set()

    for c in children: 
        for bag in bags:
            if c in bag.children['color']:
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
    children = {'colors': [], 'quantities': []} #TODO: this could be a "children" class

    for p in parents: 
        for bag in bags:
            if p in bag.color:
                children['colors'].extend(bag.children['color'])
                children['quantities'].extend(bag.children['quantity'])
                #TODO: deal with "no other bags -> "
    return children

#  Test: vibrant plum
#  ground truth: 5 faded blue bags and 6 dotted black bags
vibrant_plum_children = find_children(BAGS, 'vibrant plum') # NOTE: works
shiny_gold_children = find_children(BAGS, 'shiny gold') # NOTE: works

print("Test: vibrant plum contains {}".format(vibrant_plum_children) )

def find_all_children(bags, parents, all_children):


    current_new_children = find_children(bags, parents)

    if current_new_children == False: 
        return all_children 

    else:
        # TODO: write "add" function in a new children class
        all_children['colors'].extend(current_new_children['colors'])
        all_children['quantities'].extend(current_new_children['quantities'])
        return find_all_children(bags, current_new_children, all_children) 



print()