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