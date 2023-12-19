
def fibonacci_sequence(n):
    """
    Return the value in the fibonacci sequence at point n.
    Example fibonacci_sequence(8) = 34
    :param n: int
    :return: int
    """
    first_val = 1
    second_val = 1
    total = 0
    for n in range(1, n):
        total = first_val + second_val
        third_val = first_val + second_val
        first_val = second_val
        second_val = third_val
    return total

#     if n < 0:
#         return "Fibonacci is not defined for negative numbers"
#     elif n == 0:
#         return 1
#     elif n == 1:
#         return 1
#
#     fib_seq = [0, 1]
#     for i in range(2, n + 1):
#         fib_seq.append(fib_seq[i - 1] + fib_seq[i - 2])
#
#     return fib_seq[n]
# print(fibonacci_sequence(160))
# def fibonacci(k):
#     if k in [0, 1]:
#         return k
#     return False
# def Fibonacci(n):
#     if n < 0:
#         print("Incorrect input")
#     elif n == 0:
#         return 0
#     elif n == 1 or n == 2:
#         return 1
#     else:
#         return Fibonacci(n-1) + Fibonacci(n-2)
#
# print(Fibonacci(8))


#     l = k+2
#     if l < 0:
#         raise ValueError
#     elif l == 0:
#         return "0"
#     elif l == 1:
#         return "1"
#     else:
#         l = l*(l - 1) + l*(l - 2)
#         return l
# print(fibonacci(8))
