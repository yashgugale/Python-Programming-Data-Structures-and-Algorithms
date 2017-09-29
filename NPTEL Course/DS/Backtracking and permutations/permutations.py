def permutation(l):
    i = len(l)-1
    while l[i] < l[i-1]:
        i = i-1
    next_suffix = i-1
    print(next_suffix)

    while l[next_suffix] < l[i]:
        i += 1
    swap_letter = i-1
    print(swap_letter)
    print(l)

    l[swap_letter], l[next_suffix] = l[next_suffix], l[swap_letter]
    print(l)

    for i in range(len(l)-1, next_suffix, -1):
        for j in range(next_suffix+1, i, +1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    print("The permutation output is: ")
    print(l)
    return

    
l = ['b', 'f', 'a', 'i', 'j', 'h', 'g', 'e', 'd', 'c']
permutation(l)
        
"""
OUTPUT:

3
4
['b', 'f', 'a', 'i', 'j', 'h', 'g', 'e', 'd', 'c']
['b', 'f', 'a', 'j', 'i', 'h', 'g', 'e', 'd', 'c']
The permutation output is: 
['b', 'f', 'a', 'j', 'c', 'd', 'e', 'g', 'h', 'i']

"""
