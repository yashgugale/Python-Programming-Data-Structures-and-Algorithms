def findpos(l,v):

    for i in range(len(l)):
        if l[i] == v:
            pos = i
            break   # exit, report position
    else:
        pos = -1    # no break, v not in l
    return(pos)
# else is a part of for
# else can also be a part of while
# note that the else part will get executed only if the entire loop was scanned
# and yet the element was not found
# if we find the element in the loop, then it will break and else will be skipped
# altogether.

"""Refer the foll code:
x = 10
for i in range(0,10):
    print("loop executed for foll times: ",i)
    if i == 5:
        break
else:
    x = 11
    
print("If x is = 11, then full loop was iterated and else changes the value of x:",x,"otherwise the for loop broke in between")

OUTPUT:

>>> 
 RESTART: C:/Users/yashg/Desktop/Python Programming/practice codes/Nptel Python/tmp.py 
loop executed for foll times:  0
loop executed for foll times:  1
loop executed for foll times:  2
loop executed for foll times:  3
loop executed for foll times:  4
loop executed for foll times:  5
If x is = 11, then full loop was iterated and else changes the value of x: 10
otherwise the for loop broke in between

"""


"""
def findpos(l,v):
    pos = -1
    for i in range(len(l)):
        if l[i] == v:
            pos = i
            break   # break breaks out of for loop
    return(pos)
"""

"""
def findpos(l,v):
    
    (pos,i) = (-1,0)

    for x in l:
        if x == v:
            pos = i
            break      # break breaks our of for loop
        i = i+1
        
    return(pos)
"""

result = findpos([10,20,30,10,20,40,50], 30)
print("result is: ",result)
