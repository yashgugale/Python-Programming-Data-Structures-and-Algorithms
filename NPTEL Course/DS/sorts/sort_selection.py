#Selection sort:
#Time complexity: O(n^2)
"""
Every time select the next
"""
#import random
#L = random.sample(range(5000),3000)

L = [20, 20, 90, 40, 10, 30, 60, 90, 50]
print(L)
for i in range(len(L)):
    for j in range(len(L)):
        if L[j] > L[i]: #just inverting the > sign will change from ascending to descending sort
            tmp = L[i]
            L[i] = L[j]
            L[j] = tmp

print(L)

"""
OUTPUT:

1. if L[j] < L[i]:

 RESTART: C:/Users/yashg/Desktop/Python Programming/practice codes/Nptel Python/sorts/sort_selection.py 
[90, 60, 50, 40, 30, 20, 10]
>>> 

2. if L[j] > L[i]:

 RESTART: C:/Users/yashg/Desktop/Python Programming/practice codes/Nptel Python/sorts/sort_selection.py 
[10, 20, 30, 40, 50, 60, 90]
>>> 

"""
