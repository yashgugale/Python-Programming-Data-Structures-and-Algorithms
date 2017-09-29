L = [10, 20 , 30]
print("The global list is: ", L)
def f1():
    x = 500
    L = x
    print("The value of L in local function f1() is: ", L)
f1()

def f2():
    x = 500
    L.append(x)
    print("The value of L in local function f2() on appending is: ", L)
f2()

print("The global value of list after appending in local function f2() is: ", L)
          
var = 200
print("\nThe value of the var is: ", var)
def f3():
    y = 1000
    var = y
    print("The local value of var is: ", var)
f3()

print("The global value of var after local change in function f3() is: ", var)
