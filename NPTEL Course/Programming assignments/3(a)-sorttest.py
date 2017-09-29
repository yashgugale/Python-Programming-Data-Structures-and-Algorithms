def ascending(l):
    num = 0
    if len(l) == 1: #check if length of the list is 1
        num = True
    else:
        for i in range(len(l)-1):
            if l[i] <= l[i+1]:
               num = True
            else:
                num = False
                break   #break out of the loop even if once it is false
    return(num)
        
"""
Define a Python function ascending(l) that returns True if each element in its input list is at least as big as the one before it.

Here are some examples to show how your function should work.

>>> ascending([])
True
>>> ascending([3,3,4])
True
>>> ascending([7,18,17,19])
False

"""
