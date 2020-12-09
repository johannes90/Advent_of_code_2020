import re

# This class is used in days: {4}
class Passport: 

    def __init__(self):

        # Set of required fields
        self.required_fields = {
        'byr',
        'iyr',
        'eyr',
        'hgt',
        'hcl',
        'ecl',
        'pid'}

        self.optional_fields = {
        'cid'}  # (Country ID) - ignored, missing or not. 

        self.fields = {} 

        # functions to set values if valid
        self.validate_and_set = {'byr':  self.validate_and_set_byr,       
                                 'iyr':  self.validate_and_set_iyr, 
                                 'eyr':  self.validate_and_set_eyr,
                                 'hgt':  self.validate_and_set_hgt,
                                 'hcl':  self.validate_and_set_hcl,
                                 'ecl':  self.validate_and_set_ecl,
                                 'pid':  self.validate_and_set_pid,
                                 'cid':  self.validate_and_set_cid} # optional value

    """ validation functions for required passport fields"""
    def validate_and_set_byr(self, byr):

        #byr (Birth Year) - four digits; at least 1920 and at most 2002
        byr = int(byr)
        if (byr >= 1920 and byr <= 2002):
            self.fields['byr'] = byr
                                 
    def validate_and_set_iyr(self, iyr):

        # iyr (Issue Year) - four digits; at least 2010 and at most 2020
        iyr = int(iyr)
        if (iyr >= 2010 and iyr <= 2020):
            self.fields['iyr'] = iyr
    
    def validate_and_set_eyr(self, eyr):

        #eyr (Expiration Year) - four digits; at least 2020 and at most 2030
        eyr = int(eyr)
        if (eyr >= 2020 and eyr <= 2030):
            self.fields['eyr'] = eyr
                                 
    def validate_and_set_hgt(self, hgt):
        #hgt (Height) - a number followed by either cm or in:
        #If cm, the number must be at least 150 and at most 193.
        #If in, the number must be at least 59 and at most 76.

        hgt_pattern = re.compile(r'^(\d+)(cm|in)$')
        if hgt_pattern.match(hgt):
            hgt_unit = hgt[-2:]
            hgt_val  = int(hgt[:-2])

            if hgt_unit == 'cm':
                if hgt_val >= 150 and hgt_val <= 193:
                    self.fields['hgt'] = hgt_val

            elif hgt_unit == 'in':
                if hgt_val >= 59 and hgt_val <= 76:
                    self.fields['hgt'] = hgt_val
            
            else: 
                print('hgt not a valid unit') # TODO: ingore this case and just not update the value? 
                raise(ValueError)


    def validate_and_set_hcl(self, hcl):

        #hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
        # raw string with r in front of string -> 
        hcl_pattern = re.compile(r'^#[0-9a-f]{6}')
        if hcl_pattern.match(hcl):

            self.fields['hcl'] = hcl
       

    def validate_and_set_ecl(self, ecl):

        #ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
        ecl_pattern = re.compile(r'^(amb|blu|brn|gry|grn|hzl|oth)$') 
        if ecl_pattern.match(ecl):
            self.fields['ecl'] = ecl
        

    def validate_and_set_pid(self, pid):
        
        #pid (Passport ID) - a nine-digit number, including leading zeroes.
        #pid = int(pid)
        pid_pattern = re.compile(r'^[0-9]{9}$')
        if pid_pattern.match(pid):
            self.fields['pid'] = pid
        

    def validate_and_set_cid(self, cid):

        self.fields['cid'] = cid



# This class is used in days: {8} 
class Handheld:

    def __init__(self):

        self.programm = None # puzzle input
        self.instruction = None
        self.operation = None
        self.argument = None
        self.accumulator = 0
        self.programm_pointer = -1
        self.infinite_loop_detected = False
        self.stopping_condition = False
        
        self.executed_lines = set() 
        
        self.operation_fct = {'acc': self.acc,
                            'jmp': self.jmp,
                            'nop': self.nop}

    def read_programm(self, programm):
        self.programm = programm

    # increment pointer unless we came from a jump instruction (we allready jumped to a new line)
    def increment_programm_pointer(self):
        if self.operation != 'jmp':
            self.programm_pointer += 1
        else: 
            # The programm pointer was changed inside "jmp" function thus allready updated
            pass 
        

    # reads the instruction from the current line of the programm
    def read_instruction(self):
        
        if self.check_infinite_loop() == False:
            
            # read the current instruction of the programm
            self.instruction = self.programm[self.programm_pointer]

            [op, arg] = self.instruction.split(' ')
            self.operation = op
            self.argument  = int(arg)

            # to detect infinite loops safe the programm lines in a set
            self.executed_lines.add(str(self.programm_pointer))
            
        else: 
            print('Programm ran into infinite loop, Accumlator value: ', self.accumulator)
            self.infinite_loop_detected = True

        # the pointer, instructions and acc valid for the current loop is displayes
        print('pointer: ', self.programm_pointer, 'acc: ', self.accumulator, 'instruction: ', self.instruction)



    def execute_instruction(self):

        if self.infinite_loop_detected == True:
            # the programm loop will be stopped with the condition below, 
            # that way we can chose to use other criteria to stop the loop other than infinite loop
            self.stopping_condition = True
            pass
        else:
            self.operation_fct[self.operation]() 

    def check_infinite_loop(self):
        
        set_current_line = {str(self.programm_pointer)} # NOTE: conversion with set() does not work for strings with multiple characters somehow..

        # check if we have seen the line of instruction before
        if set_current_line.intersection(self.executed_lines):
            return True 
        else: 
            return False 

    # increase or decrease the accumulator by the current argument
    def acc(self):
        self.accumulator += self.argument

    # jumps to a new instruction relative to itself. 
    # The next instruction to execute is found using the argument as an offset
    def jmp(self):

        self.programm_pointer += self.argument    

    # Do not do anythin, continue with next line
    def nop(self):
        pass