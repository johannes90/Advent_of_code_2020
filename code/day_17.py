import time 
import re
import copy
import itertools
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

data_string = "day_17_input.txt"

text_file = open(data_string, "r")
state = text_file.read()
space = state.split('\n')

Ndim = 3 
# cube status
ACTIVE   = '#'
cubes = set()
# The initially active cubes lie in a 2D Slice of a Ndim space 
# The space is either Ndim=3  for part 1 or Ndim=4 for part 2
if Ndim == 3:
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
# Simulate 6 cycles of chaning cubes 
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

# Print function for debugging
def print_2D_slice(cubes, z0, gridsize):
    if type(cubes) == tuple:
        cs = [cubes]
    else:
        cs = cubes

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


    # convert cubes of z_0 plane to 2D List[List]
    z0_plane = []
    for row in range(gridsize):
        ROW = []
        for col in range(gridsize):
            
            if (col+min_x, row+min_y, z0) in cs:
                ROW.append('#')
            else:
                ROW.append('.')

        z0_plane.append(ROW)
        print(ROW)

    print()
    return z0_plane

# TODO: utilize fact that the cubes would change in +z/-z direction the same  
for i_cycle in range(NUM_CYCLES):

    inactive = set()
    new_activ = set()
    potentially_new = {}

    # Loop through al cubes in the map
    for cube in cubes:

        # check if neighbours exist
        neighbours = get_neighbour_coord_ND(cube)

        # Existent(active) neighbours: Those are neighbours of a cube that are a cube allready
        active_neighbours = neighbours.intersection(cubes)
        active_neighbours_count = len(active_neighbours)
        
        # Condition ACTIVE -> stay ACTIVE or get INACTIVE
        if (active_neighbours_count != 2 and active_neighbours_count != 3):
            inactive.add(cube)

        # candidates for new active cubes are those neighbours that are not allready a cube
        nn = neighbours.difference(cubes)
        for n in nn:
            if n in potentially_new:
                potentially_new[n] += 1
            else:
                potentially_new[n] = 1
        
    # Condition INACTIVE -> stay INACTIVE or get ACTIVE
    for neighbour in potentially_new:
        
        Num_active_of_inactive = potentially_new[neighbour]
        if Num_active_of_inactive == 3:
            new_activ.add(neighbour)
    
    # Remove cubes are inactive
    cubes = cubes.difference(inactive)

    # Add new active cubes 
    cubes = cubes.union(new_activ)


t_delta = time.time() - t0

print('{} cubes are active after {} cycles in {} dimensional space'.format(len(cubes), NUM_CYCLES, Ndim))
print('Computation took {} seconds \n'.format(t_delta))


# Plot point cloud
fig = plt.figure()
ax = Axes3D(fig)

ax.scatter(*zip(*cubes))
plt.show()

