L1 = [10, 20 ,30]
print("Global list L: ", L1)

def f1():
    L1[2] = 500
    print("L1 from function on in place change is is: ", L1)
    print("\nShallow copy of L1 to L2")
    L2 = L1
    L2.append(600)
    print("Lists L1 and L2 are: L1:", L1, "L2: ", L2)

    print("\nDeep copy of L1 to L3")
    L3 = L1.copy()
    L3.append(700)
    print("Lists L1 and L3 are: L1:", L1, "L3: ", L3)
f1()
print("\nGlobally L1 after all the changes is: ", L1)

# how can we, from a local function without using a 'global' or a 'nonlocal'
# change the value of a LIST used globally?
# It is true for both dimensions of mutability: 1. in place change 2. grow/shrink, so,
# is this property applicable to all mutable data types? List, Dict, Set?

S = { 10, 20, 30}
print("\nThe global value of set S", S)
def f2():
    S.add(400)
    print("The values of set S are: ", S)
f2()
print("The value of set S after function f2 is: ", S)

D = { 'a' : 10, 'b' : 20, 'c' : 30}
print("\nThe dictionary is: ", D)
def f3():
    D.update({'d' : 40})
    print("The value of dict D is: ", D)
f3()
print("The value of dict D after function f3 is: ", D)

# as we can see, we are able to do do without using 'global' or 'nonlocal'
# why does this work?
