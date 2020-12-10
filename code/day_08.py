from AdventClasses import Handheld

data_string = "day_08_input.txt"
text_file = open(data_string, "r")
clean_programm = text_file.read().split('\n')
text_file.close()

#clean_programm = programm

#TODO: clean up messy approach
len_programm = len(clean_programm)

for i in range(len(clean_programm)):
    print(i)
    programm = clean_programm[:]
    instruction = programm[i]
    [op, arg] = instruction.split(' ')
    
    # flip jmp and and nop operation
    if op == 'jmp':
        op = 'nop'
    elif op == 'nop':
        op = 'jmp'
    else: continue
    programm[i] = op + ' ' + arg

    handheld = Handheld()

    handheld.read_programm(programm)


    # Run programm
    while handheld.stopping_condition == False :

        # Update programm pointer 
        handheld.increment_programm_pointer()

        if handheld.programm_pointer > len_programm:
            print("programm finished successfully")
            break

        # Position pointer determines instruction (and checks for infinite loop)
        handheld.read_instruction()

        # Execute instruction
        handheld.execute_instruction()
      
print("Solution = ", handheld.accumulator) # 571 not correct, 277 to low