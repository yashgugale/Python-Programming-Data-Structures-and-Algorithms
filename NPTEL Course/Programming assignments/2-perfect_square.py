"""
3. PROBLEM STATEMENT:
Write a function sumsquares(l) that takes as input a list of integers and retuns the sum of all the perfect squares in l.

Here are some examples to show how your function should work.

>>> sumsquares([1,4,9])
14
>>> sumsquares([10,11,12,15])
0
>>> sumsquares([16,20,25,30,625])
666

"""

def sumsquares(l):
    result = 0
    for number in l:
        sqrt = number ** 0.5
        if number % sqrt == 0:
            result = result + number

    return(result)

solution = sumsquares([1,4,9])
#print(solution)
