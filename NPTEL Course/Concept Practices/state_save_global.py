import sys
x = 0

def add(n1,n2):
    global x
    y = x
    if y == 200:
        print("Max limit of 200 reached. Exiting now")
        sys.exit(0)
    x = n1 + n2 + y
    return x

l = add(10,20)
print("The value of add() called 1st is: ", l)
print("The global value of x is: ", x)

m = add(30,40)
print("The value of add() called 2nd time is: ", m)
print("The global value of x is: ", x)

n = add(50,50)
print("The value of add() called 3rd time is: ", n)
print("The global value of x is: ", x)

# Note that as every time the function is called, the value of x computed by the
# previous call is saved in global x. Hence, we can say that the 'state' can be
# saved in this way for further use by the function call.

o = add(5,5)
print("The value of add() called 4th time is: ", o)
print("The global value of x is: ", x)

# thus, from the saved state of the value of x, we deduced that further calls to
# add must exit the program. Thus, we can use 'global' to save the state as shown
