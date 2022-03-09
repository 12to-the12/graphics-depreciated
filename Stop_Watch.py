from time import time

class Stop_Watch(): # allows you to check how long things take to run
    timing_flag = True # this 
    epoch = time() # this gets the # seconds since 1970

    def take_time(message):
        if Stop_Watch.timing_flag: # if timing is enabled
            print(message,': ',(time()-Stop_Watch.epoch )*1000)
            Stop_Watch.epoch = time()

