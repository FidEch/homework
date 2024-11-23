import math

def divide_fake (first, second):
    if second == 0:
        print(float('inf'))
    elif first / second > 0:
        print(first / second)
