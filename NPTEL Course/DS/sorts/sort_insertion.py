#Insertion sort:
#Time complexity: O(n^2)
import random

L = [10,40,20,60,70,40,90,30]

print(L)

for i in range(1,len(L)):   #We can use range from 1, as initially i=0 and so j=0
                            #which means that the first while loop will not execute as j !>0
    j = i
    while j > 0 and L[j-1] > L[j]:
        temp = L[j-1]
        L[j-1] = L[j]
        L[j] = temp
        j = j-1
            
print(L)
