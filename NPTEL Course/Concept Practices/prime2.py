import sys
from prime import isprime #Use the isprime function that we have already written
                        #that returns True if the number is a prime number

def prime_upto(n):
    prime_list = []

    for i in range(1,n+1):
        if isprime(i):
            prime_list.append(i)
            
    return(prime_list)

#Return prime numbers upto a given number

"""
Returns the first n prime numbers:

def nprimes(n):
    (count, i, plist) = (0,1,[])
    while(count < n):
        if isprime(n):
            (count, plist) = (count + 1, plist + [i])

        i = i + 1
    return(plist)

"""
