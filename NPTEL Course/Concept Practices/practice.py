import sys

def f1():
    print(sys.getrefcount(10))
    a = 10
    print(sys.getrefcount(10))
    b = a
    print(sys.getrefcount(10))
    c = 10
    d = 10
    print(sys.getrefcount(10))
f1()
