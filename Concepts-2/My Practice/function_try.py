import sys

def findmin(L):
    alphabet = None
    digit = None
    if type(L) != list:
        print("L must be a list")
        print("Program will terminate now!")
        sys.exit(-1)

    if len(L) <= 0:
        print("L must not be empty")
        print("Program will terminate now!")
        sys.exit(-1)
        
    for x in range(len(L)):
        if type(L[x]) == str:
            alphabet = True               
        if type(L[x]) == int:
            digit = True
             
    if (alphabet == True and digit == True):
        print("Invalid list elements: both digit and alphabets used")
        print("Program will terminate now!")
        sys.exit(-1)
            
    min_element = L[0]
    for i in range(len(L)):
        if L[i] < min_element:
            min_element = L[i]
    return min_element

L1 = [10, 20, 30, 40, 50]
L2 = [2, 40, 20, 10, 50]
L3 = ['a', 'c', 'd', 'f', 'z']
L4 = [30, 20, 'a', 'z']
L5 = []

print(findmin(L1))
print(findmin(L2))
print(findmin(L3))
findmin(L4)
print(findmin(L5))
print(findmin(None))
