data_string = "day_07_input.txt"

text_file = open(data_string, "r")
raw_input = text_file.read()
rules    = raw_input.split('\n')  
text_file.close()

# (color)outer bag contains -> shiny gold bag, ... 

#
# idea: 
# 1: parse sentences to bag a -> N bag b format (named tuple?)   
# 2: build tree/graph for every rule (tuple)
# 3: start at shiny gold bag at a child node 
#   -> 3a:find every parent nodes in the set of rules (tree/graphs tuples)
#   -> 3b: for every parent node repeat 3 -> new parents nodes 
#       -> repeat again and again until we don't have any more parent nodes (-> maybe recursion is smart ?)

print(1)