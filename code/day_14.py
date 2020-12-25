data_string = "day_10_input_test.txt"

text_file = open(data_string, "r")
raw_input = text_file.read()
adapters    = raw_input.split('\n') 

adapters = [int(adapter) for adapter in adapters]
adapters = sorted(adapters)