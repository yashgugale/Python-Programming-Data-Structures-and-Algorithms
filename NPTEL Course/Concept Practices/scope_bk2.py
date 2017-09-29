x = 200
print("The value of x from global scope is: ", x)
print("Global scope of global: ", globals())
def f1():
    global x
    x = 2000
    print("\nWe have now changed x to 2000 by using - global x. Value of x is: ",x)
    print("Global scope of f1: ", globals())
    print("Local scope of f1: ", locals())
f1()

print("\nOutside function, x is still changed as the global x in function f1 changed it. x is: ", x)
print("After f1 global x, global scope: ", globals())

def f2():
    y = 20
    print("\nValue of y in f2 is: ", y)
    print("Local scope of f2: ", locals())
    def f3():
        y = 30
        def f4():
            nonlocal y
            y = 200
            print("\nValue of y in f3 is: ", y)
            print("Local scope fo f4: ", locals())
        f4()
        print("\nLocal scope fo f3: ", locals())
    f3()
    print("\nafter using nonlocal in f3, y must change to the value assigned in f3. y is: ",y)
    print("Local scope of f2 again: ", locals())
f2()    
