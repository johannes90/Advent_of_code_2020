import re                           # regular expressions
from AdventClasses import Passport  # passport class to create empty passports and check if fields are valid

data_string = "day_04_input.txt"
#data_string = "day_04_input_test_4valid.txt"  # 4 valid passports
#data_string = "day_04_input_test_invalid.txt" # 4 invalid passports

text_file = open(data_string, "r")
passports = text_file.read().split('\n\n') # empty line = 2 new lines in a row 
text_file.close()

# format the passports as list of dictionaires :
passports_string = list((map(lambda passport: re.split('\n| ', passport),  passports)))

passports = []
valid_passports = 0 

for passport_string in passports_string:
    
    # Init empty passport and extract key,value strings
    passport = Passport()
    for key_value_string in passport_string:

        # current key, value pair
        [key, value] = key_value_string.split(':')

        # Set field if required or optional:
        if key in passport.required_fields or key in passport.optional_fields:

            passport.validate_and_set[key](value)

        else:
            print("field not considered, not stored")
    
    # Check if the current passport has a valid entry for all required fields 
    current_fields = set(passport.fields)   

    if passport.required_fields.issubset(current_fields):
        valid_passports += 1

        # Store passport with valid fields
        passports.append(passport)


print(valid_passports) 