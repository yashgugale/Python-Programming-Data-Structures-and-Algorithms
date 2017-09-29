def gcd(m,n):
    fm = []
    fn = []
    cf = []
    if m > n:
        max_no = m
    else:
        max_no = n

    for i in range(1,max_no+1):
        if ((m%i) == 0 and (n%i) == 0): #ie i divides both m and n, then add it to cf list
            cf.append(i)
            
    return (cf[-1])

result = gcd(12,12)
print("The gcd of 23,23 is: ", result)
        
# actually, we can write:
# for i in range(1,min(m,n)+1):
#     if (m%i) == 0 and (n%i) == 0:
#         cf.append(i)

# Note: min is a keyword, that will return the smallest of the two numbers
