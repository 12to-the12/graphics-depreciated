from time import time

class Stop_Watch(): # allows you to check how long things take to run
    timing_flag = True # this 
    epoch = time() # this gets the # seconds since 1970
    breakpoints = {} #key is message, value is sum instances list
    frequency = 100# actually inverse of frequency
    loops = 1
    def take_time(message):
        time_taken = (time()-Stop_Watch.epoch) # in seconds
        if Stop_Watch.timing_flag: # if timing is enabled, periodically print out the running averages of each breakpoint
            if not message in Stop_Watch.breakpoints.keys():# if first loop through
                Stop_Watch.breakpoints[message] = time_taken
            else: # if the entry already exists
                Stop_Watch.breakpoints[message] += time_taken
                if Stop_Watch.loops % Stop_Watch.frequency == 0:
                    print(message,': ',Stop_Watch.breakpoints[message]
                                      /Stop_Watch.loops
                                      *1000)
            
            Stop_Watch.epoch = time()

