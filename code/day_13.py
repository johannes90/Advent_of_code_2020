data_string = "day_13_input.txt"

text_file = open(data_string, "r")
raw_input = text_file.read()
NOTES    = raw_input.split('\n') 

earliest_timestamp = int(NOTES[0])
busses = NOTES[1].split(',') 
# at timestamp 0 all busses depart and repeat forever
# ID = time for one loop
# 

print('earliest timestamps: {} \nBusses: {}'.format(earliest_timestamp, busses))


min_wait = 100000
min_bus  = -1
for bus in busses:
    if bus == 'x':
        pass
    else: 
        bus = int(bus)

        waiting_time = bus - earliest_timestamp % bus
        print('{} wait {}'.format(bus, waiting_time))

        if waiting_time < min_wait:
            min_wait = waiting_time
            min_bus  = bus

print('minimum waiting time: {}'.format(min_bus*min_wait))