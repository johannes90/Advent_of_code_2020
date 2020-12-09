from AdventClasses import Handheld

data_string = "day_08_input.txt"
text_file = open(data_string, "r")
programm = text_file.read().split('\n')
text_file.close()

handheld = Handheld()

handheld.read_programm(programm)

# Run programm
while handheld.stopping_condition == False:

    # Update programm pointer 
    handheld.increment_programm_pointer()

    # Position pointer determines instruction (and checks for infinite loop)
    handheld.read_instruction()

    # Execute instruction
    handheld.execute_instruction()
    