
# def fibonacci_sequence(n):
#     """
#     Return the value in the fibonacci sequence at point n.
#     Example fibonacci_sequence(8) = 34
#     :param n: int
#     :return: int
#     """
#     first_val = 1
#     second_val = 1
#     total = 0
#     for n in range(1, n):
#         total = first_val + second_val
#         third_val = first_val + second_val
#         first_val = second_val
#         second_val = third_val
#     return total


#
from tkinter import *
def fibonacci_sequence(n):
    """
#     Return the value in the fibonacci sequence at point n.
#     Example fibonacci_sequence(8) = 34
#     :param n: int
#     :return: int
#     """
    first_val = 1
    second_val = 1
    total = 0
    for n in range(1, n):
        total = first_val + second_val
        third_val = first_val + second_val
        first_val = second_val
        second_val = third_val

    label = Label(root, text=total)
    label.pack



