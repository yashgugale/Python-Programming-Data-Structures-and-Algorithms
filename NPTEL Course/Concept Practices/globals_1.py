var = 99

def local():
    var = 0

def glob1():
    global var
    var += 1

def glob2():
    var = 0
    import globals_1
    globals_1.var += 1

def glob3():
    var = 0
    import sys
    glob = sys.modules['globals_1']
    glob.var += 1

def test():
    print(var)
    local()
    glob1()
    glob2()
    glob3()
    print(var)

# or we can use: local(); glob1(); glob2(); glob3();     
    
