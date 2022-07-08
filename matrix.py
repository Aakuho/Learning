# Homework

from pprint import pprint

def func(number):
    return [[max(abs(row - (2 * number - 1)//2), abs(col - (2 * number - 1) // 2)) + 1 for col in range((2 * number - 1))] for row in range((2 * number - 1))]
    #The value at each index is given by the maximum of (distance from the row index to the center, distance from the column index to the center).


pprint(func(3))

#?      3   3   3   3   3
#?      3   2   2   2   3
#?      3   2   1   2   3
#?      3   2   2   2   3
#?      3   3   3   3   3

