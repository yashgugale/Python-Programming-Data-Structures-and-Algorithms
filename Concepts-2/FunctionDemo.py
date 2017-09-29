import sys

def findmax(L):

    if type(L) != list:
        print("L MUST BE A LIST OBJECT")
        sys.exit(-1) 

    if len(L) <= 0:
        print("L MUST BE NON EMPTY")
        sys.exit(-1) 
    
    max_element = L[0] 
    for i in range(1, len(L)):
        if L[i] > max_element:
            max_element = L[i]
    return max_element

L1 = [10, 3, 234, 2, 345, 25476, 2342]
L2 = [x**2 for x in range(100)] # 99 ** 2 = 9801 which is the max element here
L3 = [213214,432,12321543,5436,7656685,7645643,65,213]

m = findmax(L1)
print("Max element in L1 is:", m)

m = findmax(L2)
print("Max element in L2 is:", m)

m = findmax(None)
print("Value of None:", m)

# as we have added sys.exit in the code where we are checking if it is a list object
# the next two function calls will not get executed as the program terminates
m = findmax(L3)
print("Max element in L3 is:", m)

m = findmax(L1)
print("Max element in L1 again is: ", m)





        
