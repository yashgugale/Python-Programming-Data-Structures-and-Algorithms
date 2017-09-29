def gcd(m,n):
    fm = []
    fn = []
    cf = []
    if m > n:
        max_no = m
    else:
        max_no = n

    for i in range(1,max_no+1):
        if (m%i) == 0:
            fm.append(i)
        if (n%i) == 0:
            fn.append(i)

    for j in fm:
        if j in fn:
           cf.append(j)

    return (cf[-1]) #Return the larget(rightmost) value in cf

result = gcd(21,24)
print("The gcd of 21,24 is: ", result)
        
