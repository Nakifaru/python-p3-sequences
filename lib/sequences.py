#!/usr/bin/env python3

def print_fibonacci(length):
    series = [0, 1]

    if length == 0:
        print([])
    
    elif length == 1:
        print([0])
    
    elif length == 2:
        print (series)
    
    else:
        last_num = series[-1]
        second_last = series[-2]
        i = 3
        while i <= length:
            series.append(last_num + second_last)
            last_num = series[-1]
            second_last = series[-2]
            i += 1
        print(series)
    pass