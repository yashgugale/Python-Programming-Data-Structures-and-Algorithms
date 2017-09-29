def gcd(n1,n2):
    n1_factors = [] # list all numbers that are factors of num1
    n2_factors = [] # list all numbers that are factors of num2
    common_factors = [] # common factors to both num1 and num2
    for i in range(1,n1+1): # as range will give numbers upto n1-1, we add 1 to n1
        if n1 % i == 0:
            n1_factors.append(i) # add factors to list

    for j in range(1,n2+1): # similarly, we add 1 to n2
        if n2 % j == 0:
            n2_factors.append(j) # add factors to list

    for x in range(len(n1_factors)):        # compare the 1st element in list of n1 with every number in list of n2
        for y in range(len(n2_factors)):    
            if n1_factors[x] == n2_factors[y]:
                common_factors.append(n1_factors[x])    # if the factors are same, add them to the common_max list

    gcd_ans = common_factors[0]     # for every element in the common_max list, find out the biggest number. This is the GCD
    for z in range(1,len(common_factors)):
        if common_factors[z] > gcd_ans:
            gcd_ans = common_factors[z]

    return gcd_ans              # return this GCD
result = gcd(14,63)
print("The gcd for the two numbers 14,63 is: ", result)  # print the result
