import sys

def isprime(n):
    factors = []
    if n == 1:
        print("1 is neither prime nor composite")
    for i in range(2,n+1):
        if n%i == 0:
            factors.append(i)
            
    if len(factors) > 2:
        print(n," is a composite number")
    else:
        print(n," is a prime number")

#isprime(5)

"""
def isprime(n):
    return(factors(n) == [1,n])

ie if the factors of n are 1 and the number itself, then return that the number
is a prime number

"""
