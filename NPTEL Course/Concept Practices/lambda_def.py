def makeActions():
    acts = []
    for i in range(5):
        acts.append(lambda x, i=i: i ** x)
    return acts

acts = makeActions()
print(acts[0])

print(acts[0](2))
print(acts[1](2))
print(acts[2](2))
print(acts[3](2))
print(acts[4](2))

"""
OUTPUT: Expected Correct Output:

<function makeActions.<locals>.<lambda> at 0x000002195F478730>
0
1
4
9
16

"""

"""
def makeActions():
    acts = []
    for i in range(5):
        acts.append(lambda x: i ** x)
    return acts

acts = makeActions()
print(acts[0])

print(acts[0](2))
print(acts[1](2))
print(acts[2](2))
print(acts[3](2))
print(acts[4](2))

OUTPUT: Wrong Output:
<function makeActions.<locals>.<lambda> at 0x000001E9EBF38730>
16
16
16
16
16

"""

"""
def func():
    x = 4
    action = (lambda n,x=x: x ** n)
    return action

x = func()

print(x(5))
"""
