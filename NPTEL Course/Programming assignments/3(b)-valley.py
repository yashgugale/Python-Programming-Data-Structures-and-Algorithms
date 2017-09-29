"""
2. Problem Statement:
A list of integers is said to be a valley if it consists of a sequence of strictly decreasing values followed by a sequence of strictly increasing values. The decreasing and increasing sequences must be of length at least 2. The last value of the decreasing sequence is the first value of the increasing sequence.

Write a Python function valley(l) that takes a list of integers and returns True if l is a valley and False otherwise.

Here are some examples to show how your function should work.

>>> valley([3,2,1,2,3])
True
>>> valley([3,2,1])
False
>>> valley([3,3,2,1,2])
False
"""

#This code is derived form reference code given below in the comments section
def valley(l):
    if len(l) < 3:  #for list size 0,1,2, return False
        return(False)
    if(l[0]<l[1]):  #if list in ascending order, return False
       return(False)
    for i in range(len(l)-1):   #check for the entire list
        if(l[i] < l[i+1]):
            position = i
            break
        if(l[i] == l[i+1]): #if elements are equal, return False
           return(False)
    else:                   #if all elements in descending order, ie for loop 
        return(False)       #is completely executed, run else and return False 
    for i in range(position, len(l)-1): 
           if(l[i] >= l[i+1]):  #if element greater than or equal, return False
               return(False)
    return(True)
           
"""
NPTEL SOLUTION:

def uplist(l):
    if len(l) < 2:
        return(False)
    for i in range(len(l)-1):
        if l[i] >= l[i+1]:
            return(False)
    return(True)
        
def downlist(l):
    if len(l) < 2:
        return(False)
    for i in range(len(l)-1):
        if l[i] <= l[i+1]:
            return(False)
    return(True)

def valley(l):
    for i in range(1,len(l)-1):
        if downlist(l[0:i+1]) and uplist(l[i:len(l)]):
            return(True)
    return(False)
"""
         
"""
Reference code: (Correct):
def valley(list):
  if(len(list)==0):
    return(True)
  if(len(list)==1):
    return(False)
  if(list[0]<list[1]):
    return(False)
  for i in range(0,len(list)-1):
    if(list[i]<list[i+1]):
      pos=i
      break
    if(list[i]==list[i+1]):
      return(False) 
  else:
    return(False)
  for i in range(pos,len(list)-1):
    if(list[i]>=list[i+1]):
      return(False)
  return(True)
print(valley([2,1]))

CODE:
1. Code without referring anything (giving some error on one test case
ie partially Correct:

def valley(l):
    count_up = 0
    count_down = 0
    down = True  #initial conditions
    up = False   #initial conditions
    #if len(l) < 3:
        #return(False)
    for i in range(len(l)-1):   #check for the entire list
        if(down == True):
            if(l[i] == l[i+1]):     #if any element is == to the next, return False
                return(False)
            if(l[i] > l[i+1]):
                count_down += 1
            else:
                down = False
                up = True
                count_down += 1      # for condition 3, 2, 3
        #if down == False and count_down < 2:    #if count_down and both down are false,
           #return(False)                        #only then return
        if down == False and up == True:
            if(l[i] == l[i+1]): #if any element is == to the next, return False
               return(False)
            if(l[i] < l[i+1]):
              count_up += 1
            else:
              break

    count_up += 1   #Increment count after breaking out of loop
    if(count_down >= 2 and count_up >= 2):  #finally check both counts before returning
        return(True)                        #final result
    else:
        return(False)

""" 
