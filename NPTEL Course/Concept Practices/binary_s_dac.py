#Binary search:
#Time complexity: O(logn)

def binarysearch(L, left, right, element):
    if right >= left:
        median = left + (right - left)//2

        if L[median] == element:
            return median
        elif L[median] > element:
            return binarysearch(L, left, median -1, element)
        else:
            return binarysearch(L, median + 1, right, element)

    else:
        return -1

L = [x for x in range(0,25,2)]
print(L)
element = int(input("Enter the element to search: "))
print(element)

result = binarysearch(L, 0, len(L)-1, element)

if result != -1:
    print("The element is found at index: ", result)
else:
    print("The element is not found")


"""
OUTPUT:

>>> 
 RESTART: C:\Users\yashg\Desktop\Python Programming\practice codes\Nptel Python\binary_s_dac.py 
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]
Enter the element to search: 6
6
The element is found at index:  3
>>> 
 RESTART: C:\Users\yashg\Desktop\Python Programming\practice codes\Nptel Python\binary_s_dac.py 
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]
Enter the element to search: 23
23
The element is not found

"""
