
#! -- Practical Use Program #1 --

def logged(func):
    def wrapper(*args, **kwargs):
        value = func(*args, **kwargs)
        with open('./decorators_log/logfile.txt', 'a', encoding='utf-8') as a:
            function_name = func.__name__
            print(f"{function_name} returned value {value}")
            a.write(f"{function_name} returned value {value}\n")
        return value

    return wrapper
    
@logged
def add(x, y):
    return x + y

#add(10, 20)

#! -- Practical Use Program #2 --

import time

def timed(func):
    def wrapper(*args, **kwargs):
        before = time.time()
        value = func(*args, **kwargs)
        after = time.time()
        
        fname = func.__name__
        print(f"{fname} took {round(after-before, 3)} seconds to execute")
        return value
    return wrapper

@timed
def myFunc(x):
    result = 1
    for i in range(1, x):
        result *= i
    return result

#myFunc(100000)