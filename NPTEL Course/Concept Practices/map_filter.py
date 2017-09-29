def square(x):
    return(x*x)

def iseven(x):
    return(x%2 == 0)

L = list(map(square,(filter(iseven, range(50)))))
print(L)
print("length of L:", len(L))

"""

MAP FILTER USING LIST COMPREHENSION:

L = [(x*x) for x in range(100) if x%2 == 0]

>>> L
[0, 4, 16, 36, 64, 100, 144, 196, 256, 324, 400,
484, 576, 676, 784, 900, 1024, 1156, 1296, 1444, 1600,
1764, 1936, 2116, 2304, 2500, 2704, 2916, 3136, 3364,
3600, 3844, 4096, 4356, 4624, 4900, 5184, 5476, 5776,
6084, 6400, 6724, 7056, 7396, 7744, 8100, 8464, 8836, 9216, 9604]
