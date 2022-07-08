import sys

def myGenerator(n):
    for x in range(n + 1):
        yield x ** 3

values = myGenerator(1000)      # Can be any number, and the following will still be true  
print(sys.getsizeof(values))    # Generators don't change size in bytes, doesn't matter how big the input is

def infiniteSequence():
    result = 1
    while True:
        yield result
        result *= 5

values = infiniteSequence()     # <- Doesn't waste memory, we still have an infinite sequence and get next value, unless limitied by memory itself

print(next(values))             # 1
print(next(values))             # 5
print(next(values))             # 25
print(next(values))             # 125
print(next(values))             # 625
print(next(values))             # 3125