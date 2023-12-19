import math
def factorial(k):
    if k < 0:
        raise TypeError
    elif k == 0 or k == 1:
        return 1
    else:
        return math.factorial(k)