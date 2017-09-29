def frequency(l):

    #first sorting the list
    for i in range(len(l)-1, 0, -1):
        for j in range(i):
            if(l[j] > l[j+1]):
                temp = l[j]
                l[j] = l[j+1]
                l[j+1] = temp
    print("Initial sorted list: ",l)
    
    #add the distinct elements to a new list
    m = []
    for element in l:
        if element not in m:
            m.append(element)
    print("List of distinct elements: ", m)

    #create a new list to store the count of the individual elements
    count = [[0] for i in range(len(m))]

    #for all elements in m, add their counts to the count list
    for j in range(len(m)):
        for i in range(len(l)):
            if m[j] == l[i]:
                count[j][0] += 1
    print("List containing count of every element with positions: ", count)

    #set minfreq and max frequency to the first element
    minfreq = count[0][0]
    maxfreq = count[0][0]

    #if current element is less than minfreq, make current as minfreq
    for i in range(len(count)):
        if(count[i][0] < minfreq):
           minfreq = count[i][0]

    #if current element is greater than maxfreq, make current as maxfreq        
    for i in range(len(count)):
        if(count[i][0] > maxfreq):
            maxfreq = count[i][0]      

    print("Minimum frequency in the count list: ", minfreq)
    print("Maximum frequency in the count list: ", maxfreq)

    #Create two empty lists than will hold the final numbers
    minlist = []
    maxlist = []

    #if any element has count == the minfreq, add it to the minlist
    #if any element has count == the maxfreq, add it to the maxlist
    for i in range(len(count)):
        if(count[i][0] == minfreq):
            minlist.append(m[i])
        if(count[i][0] == maxfreq):
            maxlist.append(m[i])

    #print result
    print(minlist)
    print(maxlist)
l = [1,2,3,4,5,5,4,3,2,3,4,5,5,4,5]
frequency(l)

"""
1. PROBLEM STATEMENT:

Write a Python function frequency(l) that takes as input a list of integers and returns a pair of the form (minfreqlist,maxfreqlist) where
minfreqlist is a list of numbers with minimum frequency in l, sorted in ascending order
maxfreqlist is a list of numbers with maximum frequency in l, sorted in ascending
For instance
>>> frequency([13,12,11,13,14,13,7,11,13,14,12])
([7], [13])

>>> frequency([13,12,11,13,14,13,7,11,13,14,12,14,14])
([7], [13, 14])

>>> frequency([13,12,11,13,14,13,7,11,13,14,12,14,14,7])
([7, 11, 12], [13, 14])

Sample Test Cases:
Input	                                                          Output
Test Case 1: frequency([1,2,3,4,5,5,4,3,2,3,4,5,5,4,5])          ([1], [5])
Test Case 2: frequency([4,4,4,1,1,2,2,2,3,3])                    ([1, 3], [2, 4])
Test Case 3: frequency([1,1,1,1,1])                             ([1], [1])
"""
