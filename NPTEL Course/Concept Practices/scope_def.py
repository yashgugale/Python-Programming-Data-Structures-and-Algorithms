def f1():
    x = 88
    def f2(x=x):    # var = val in the def header means that the argument arg will
        print(x)    # default to the value val if no real value is passed to arg in a call
    f2()
f1()

"""
CODE:

def f1():
    x = 88
    def f2(x=x):    # var = val in the def header means that the argument arg will
        print(x)    # default to the value val if no real value is passed to arg in a call
    f2()   # Note that here no arg is passed to f2(). thus, we get deafult val
f1()

OUTPUT:

 RESTART: C:/Users/yashg/Desktop/Python Programming/practice codes/scope_def.py 
88
-------------------------------------------------------------------------------
CODE:

def f1():
    x = 88
    def f2(x=x):    # var = val in the def header means that the argument arg will
        print(x)    # default to the value val if no real value is passed to arg in a call
    f2(20)   # as argument '20' is passed to f2(20), we get output as 20 and not default val.
f1()

OUTPUT:

>>> 
 RESTART: C:/Users/yashg/Desktop/Python Programming/practice codes/scope_def.py 
20
>>> 
"""
