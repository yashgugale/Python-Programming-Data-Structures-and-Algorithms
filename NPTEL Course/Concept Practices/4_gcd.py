def gcd(m,n):
    for i in range(1,min(m,n)+1):   #any cf will be less than minimum of m and n
        if ((m%i) == 0 and (n%i) == 0):
            max_factor = i
            
    return max_factor

result = gcd(12,8)
print("The gcd of 12,8 is: ", result)

# GCD without using list

"""
def gcd(m, n):

    i = min(m,n)

    while i > 0:
        if (m%i) == 0 and (n%i) == 0:
            return(i)
        else:
            i = i-1

Here, the largest common factor will be the GCD. Hence, we start from backwards
ie by setting i = minimum of m and n and then decrementing i till we reach 1
"""
