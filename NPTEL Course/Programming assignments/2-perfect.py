"""
PROBLEM STATEMENT:

1. A positive integer n is said to be perfect if the sum of the factors of n,
other than n itself, add up to n. For instance 6 is perfect since the factors
of 6 are {1,2,3,6} and 1+2+3=6. Likewise, 28 is perfect because the factors of
28 are {1,2,4,7,14,28} and 1+2+4+7+14=28.

Write a Python function perfect(n) that takes a positive integer argument and
returns True if the integer is perfect, and False otherwise.

Here are some examples to show how your function should work.

>>> perfect(6)
True
>>> perfect(12)
False
>>> perfect(28)
True
"""

def perfect(number):
    factors = []
    for no in range(1,number):
        if number % no == 0:
            factors = factors + [no]
    #print(factors)

    summation = 0
    for value in factors:
        summation = summation + value

    if summation == number:
        return(True)
    else:
        return(False)
    

result = perfect(9)
print(result)
