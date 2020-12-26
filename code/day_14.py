data_string = "day_14_input.txt"
text_file = open(data_string, "r")
raw_input = text_file.read()
programm    = raw_input.split('\n') 

def apply_mask_part_1(value, mask):
    # convert to 36 bit binary number with zero padding
    bin_val = format(value, '036b')
    new_val= ''
    for idx in range(len(mask)):
        v = bin_val[idx]
        m = mask[idx]
        if m != 'X':
            new_val = new_val + m
        else: 
            new_val = new_val + v 
    new_val_int = int('0b' + new_val, 2)
    return new_val_int

def store_value(memory, value, adress):
    for adr in adress:      
        memory[adr] = value
    
    return memory

def run_programm_part_1(programm):
    MEM = {} #'adress': value 
    for line in programm:
        if line[:4] == 'mask':
            mask = line.split(' = ')[-1]
        else:
            adress, value = line.split(' = ')
            adress = int(adress[4:-1])
            value  = int(value)
            altered_value = apply_mask_part_1(value, mask)
            MEM = store_value(MEM, altered_value, [adress])
    return MEM

""" 
    Part 1: Read programm to memory and apply mask to values before
"""

MEM = run_programm_part_1(programm)

sum_all_values = 0
for adress in MEM:
    sum_all_values += MEM[adress]
print('Sum of all memory values (Solution Part 1): {}'.format(sum_all_values))

""" 
    Part 2: Read programm to memory and apply mask to adresses before
"""
def run_programm_part_2(programm):
    MEM = {} #'adress': value 
    for line in programm:
        if line[:4] == 'mask':
            mask = line.split(' = ')[-1]
        else:
            adress, value = line.split(' = ')
            adress = int(adress[4:-1])
            value  = int(value)

            # Returns multiple adresses
            altered_adresses = apply_mask_part_2(adress, mask)
            #print('altered adresses = ', altered_adresses)

            MEM = store_value(MEM, value, altered_adresses)

    return MEM

def apply_mask_part_2(adress, mask):
    # convert to 36 bit binary number with zero padding
    bin_adr = format(adress, '036b')
    new_adr= ''

    num_X = 0
    for idx in range(len(mask)):
        a = bin_adr[idx]
        m = mask[idx]

        if m == 'X':
            new_adr = new_adr + 'X' # floating
            num_X += 1

        elif m == '1':
            new_adr = new_adr + '1' # overwritten
        else:
            new_adr = new_adr + a # unchanged

    num_adresses = 2**num_X
    
    new_adresses = ['']*num_adresses
    new_adresses_int = [None]*num_adresses
    # build all floatings (binaries) and put in the X positions of adresses
    for i_adress in range(num_adresses):

        floating = format(i_adress, '0' + str(num_X) + 'b')

        i_float_bit = 0
        for i_bit , bit in enumerate(new_adr):
            
            if bit == 'X':
                # Set current floating bit in adress
                new_adresses[i_adress] = new_adresses[i_adress] + floating[i_float_bit]
                i_float_bit += 1
            else: 
                # Set adress bit
                new_adresses[i_adress] = new_adresses[i_adress] + bit


        #print('{}th: new BIN adress= {}'.format(i_adress,new_adresses[i_adress]))

        # convert adress back to integer 
        new_adresses_int[i_adress] = int('0b' + new_adresses[i_adress], 2)
        #print('{}th: new INT adress= {}'.format(i_adress,new_adresses_int[i_adress]))
    
        #print()

    return new_adresses_int


MEM = run_programm_part_2(programm)

# sum all values in memory
value_sum = 0
for _, value in MEM.items():
    value_sum += value

print('Sum of all memory values (Solution Part 2): {}'.format(value_sum))