data_string = "day_12_input.txt"
import copy

text_file = open(data_string, "r")
raw_input = text_file.read()
INSTRUCTIONS    = raw_input.split('\n') 

NORTH   = 'N'
SOUTH   = 'S' 
EAST    = 'E'
WEST    = 'W'
FORWARD = 'F'
TRANS = {NORTH, SOUTH, EAST, WEST, FORWARD}
LEFT  = 'L'
RIGHT = 'R'
ROT = {LEFT: 1j, RIGHT: -1j}
DIRECTION = {NORTH: 1j, EAST: 1, SOUTH: -1j, WEST: -1}
ORIGIN = 0+0j
MANHATTEN = 'manhattan'

def parse_instructions(instr):
    instructions = []
    for instruction in instr:
        action = instruction[0]
        value  = int(instruction[1:])

        action_value = {'action': action,  'value': value}
        instructions.append(action_value)
    return instructions

instructions = parse_instructions(INSTRUCTIONS)

class Ship:

    def __init__(self, instructions):

        self.instructions = instructions

        NUM_INSTR = len(self.instructions)

        self.position    = ORIGIN
        self.orientation = DIRECTION[EAST] 

    def execute_instructions(self):

        for idx, instr in enumerate(self.instructions):

            action = instr['action']
            value  = instr['value']

            if action in ROT:
                self.rotate_ship(action, value)
            elif action in TRANS:
                self.translate_ship(action, value)

         
            print('instructions in step{}= {}, {} -> Position={}, Orientation ={}'.format(idx, action, value, self.position, self.orientation))
            print()

    def rotate_ship(self, action, value):

        if value%90 == 0:
            value = value/90
        else:
            raise(ValueError)

        self.orientation = self.orientation*ROT[action]**value
    
    def translate_ship(self, action, value):
        if action == FORWARD:

            # Move in direction of current orientation on complex plane
            self.position = self.position + self.orientation*value

        elif action in {NORTH, EAST, SOUTH, WEST}:
            # Move in current direction of current direction
            self.position = self.position + DIRECTION[action]*value
        else:
            raise(ValueError) 

    def compute_dist(self, pos_A, pos_B, type):

        if type == MANHATTEN:
            dist = pos_B - pos_A 
            return abs(dist.real) + abs(dist.imag)
        
# Part A: abs(distance) after all instruction were applied
ship = Ship(instructions)

ship.execute_instructions()   

print(ship.compute_dist(ORIGIN, ship.position, MANHATTEN))

# Inherite Ship class
class Ship_B():
    
    def __init__(self, instructions):
    
        self.instructions = instructions

        NUM_INSTR = len(self.instructions)

        self.position    = ORIGIN

    # defined relative to ship position
        self.waypoint = 10 + 1j

    def execute_instructions(self):

        for idx, instr in enumerate(self.instructions):

            action = instr['action']
            value  = instr['value']

            if action in ROT:
                self.rotate_waypoint(action, value)

            elif action in TRANS and action != FORWARD:
                self.translate_waypoint(action, value)

            elif action == FORWARD:
                self.translate_ship(value)

            else: 
                raise(ValueError)

            print('instructions in step {} = {},{} -> pos=={}, wp ={}'.format(idx, action, value, self.position, self.waypoint))
            print()

    def rotate_waypoint(self, action, value):

        if value%90 == 0:
            value = value/90
        else:
            raise(ValueError)

        self.waypoint = self.waypoint*ROT[action]**value
    
    def translate_waypoint(self, action, value):

        if action in {NORTH, EAST, SOUTH, WEST}:
            # Move in current direction of current direction
            self.waypoint = self.waypoint + DIRECTION[action]*value
        else:
            raise(ValueError) 

    def translate_ship(self, value):

        # move ship value times in direction of waypoint
        self.position = self.position + value*self.waypoint

        # NOTE: not update the waypoint relative to ship
        

    def compute_dist(self, pos_A, pos_B, type):

        if type == MANHATTEN:
            dist = pos_B - pos_A 
            return abs(dist.real) + abs(dist.imag)

ship = Ship_B(instructions)

ship.execute_instructions()   

print(ship.compute_dist(ORIGIN, ship.position, MANHATTEN))
