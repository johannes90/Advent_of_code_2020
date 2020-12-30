import time 
import re
import copy
import itertools
data_string = "day_17_input_test.txt"

text_file = open(data_string, "r")
state = text_file.read()
space = state.split('\n')

Ndim = 4
# cube status
ACTIVE   = '#'

# The initially active cubes lie in a 2D Slice of a Ndim space 
# The space is either Ndim=3  for part 1 or Ndim=4 for part 2
if Ndim == 3:
    cubes = set()
    X0_width = len(space[0])
    Y0_width = len(space)
    Z0_width = 1
    W0_width = 1
    for y in range(Y0_width):
        for x in range(X0_width):
            for z in range(Z0_width):
                if space[y][x] == ACTIVE:
                    
                    cubes.add((x,y,z))
elif Ndim == 4:
    cubes = set()
    X0_width = len(space[0])
    Y0_width = len(space)
    Z0_width = 1
    W0_width = 1
    for y in range(Y0_width):
        for x in range(X0_width):
            for z in range(Z0_width):
                for w in range(W0_width):
                    if space[y][x] == ACTIVE:
                        
                        cubes.add((x,y,z,w))

# Simulate 6 Cycles of cubes changing its status
NUM_CYCLES = 6

t0 = time.time()
# Simulate 6 cycles of chaning cubes TODO: add NDim as input for higher dim data to omit certain dimensions
def get_neighbour_coord_ND(coordinates):
    # coordinates x1, x2, x3, ... xi i = N DIM
    Ndim = len(coordinates)
    
    neighbours = set()
    Deltas = {-1, 0, 1}
    for dx in itertools.product(Deltas, repeat=Ndim):
        n = [] # empty tuple for a new neighbours
        for d_i, dx_i in enumerate(dx):
            xn_i = coordinates[d_i] + dx_i
            n.append(xn_i)

        neighbours.add(tuple(n))
    
    # Remove coordinate itsel
    neighbours.remove(coordinates)

    return neighbours  

def print_2D_slice(cubes, z0, gridsize):
    if type(cubes) == tuple:
        cs = [cubes]
    else:
        cs = cubes#.copy() 

    # Find cubes in z0-plane and max x,y coordinates of cubes in that plane
    max_x = 0 
    max_y = 0
    min_x = 10000000
    min_y = 10000000
    for cube in cs:
        if z0 == cube[2]:
            if cube[0] > max_x:
                max_x = cube[0]
            if cube[0] < min_x:
                min_x = cube[0]

            if cube[1] > max_y:
                max_y = cube[1]
            if cube[1] < min_y:
                min_y = cube[1]
            
        else: 
            pass
            #cs.remove(cube)

    # convert cubes of z_0 plane to 2D List[List]
    z0_plane = []
    for row in range(gridsize):
        ROW = []
        for col in range(gridsize):
            
            if (col+min_x, row+min_y, z0) in cs:
                ROW.append('#')
                #print('in cubes', col+min_x, row+min_y, z0)
            else:
                ROW.append('.')
                #print('not in cubes: ', col+min_x, row+min_y, z0)

        z0_plane.append(ROW)
        print(ROW)

    print()
    return z0_plane

# TODO: utilize fact that the cubes would change in +z/-z direction the same  
for i_cycle in range(NUM_CYCLES):

    inactive = set()
    new_activ = set()
    potentially_new = set()

    # Loop through al cubes in the map
    for cube in cubes:
        # check if neighbours exist
        neighbours = get_neighbour_coord_ND(cube)

        # Existent(active) neighbours: Those are neighbours of a cube that are a cube allready
        active_neighbours = neighbours.intersection(cubes)
        active_neighbours_count = len(active_neighbours)
        
        if (active_neighbours_count != 2 and active_neighbours_count != 3):
            #cubes.remove(cube)
            inactive.add(cube)

        # candidates for new active cubes are those neighbours that are not allready a cube
        potentially_new = potentially_new.union(neighbours.difference(cubes))
        
    # If a cube is inactive but exactly 3 of its neighbors are active, the cube becomes active. 
    # Otherwise, the cube remains inactive.  (inactive = new cube)
    for neighbour in potentially_new:
        
        neighbours_neighbour = get_neighbour_coord_ND(neighbour)
        Num_active_of_inactive = len(neighbours_neighbour.intersection(cubes))

        if Num_active_of_inactive == 3:
            #cubes.add(neighbour)
            new_activ.add(neighbour)
            #print('new cube: ',neighbour)
    
    # Remove cubes are inactive
    cubes = cubes.difference(inactive)

    # Add new active cubes 
    cubes = cubes.union(new_activ)

t_delta = time.time() - t0

print('Time passed: ', t_delta)
print(len(cubes))