import math
def factorial(k):
    """
    Return the factorial of the integer k
    Example: factorial(3) = 1 * 2 * 3 = 6
    :param k: int
    :return: int
    """
    if k < 0:
        raise TypeError
    elif k == 0 or k == 1:
        return 1
    else:
        return math.factorial(k)