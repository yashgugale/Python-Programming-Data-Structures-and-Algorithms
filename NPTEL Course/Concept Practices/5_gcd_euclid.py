def gcd(m,n):
    if m < n:
        (m,n) = (n,m)

    while (m%n) != 0:   # if n divides m, then break and return n eg(8,4)
        r = m%n
        (m,n) = (n,r)

    return(n)

result = gcd(36,24)
print("The GCD is : ", result)

# Final optimization of euclid
# We see that, as we are taking % values, if m is 1 billion ie 10^9, then the basic
#algorithm takes billions of steps, whereas, the above algorithm takes only tens of
#steps
"""
Using recursion:

def gcd(m,n):
    if m < n:
        (m,n) = (n,m)

    if (m%n) == 0:
        return(n)
    else:
        return(gcd(n,m%n))

result = gcd(23,69)
print("The GCD is : ", result)

# Final optimization of euclid

"""
