def onehop(l):

    print("initial list: ", l,"\n")

    finallist = []
    #main logic
    for directflight in range(len(l)):
        for j in range(len(l)):
            if(l[directflight][1] == l[j][0]):
                interflight = [l[directflight][0], l[j][1]]
                interflight = tuple(interflight)
                if(interflight not in finallist):
                    finallist.append(interflight)

    #remove the city is i,j are same
    print("finallist: ", finallist)
    rem_city = []
    for city in finallist:
        if(city[0] == city[1]):
            rem_city.append(city)
    print("Rem city: ", rem_city)      
    for city in rem_city:
        if(city in finallist):
            finallist.remove(city)
            
    #sort the tuples in ascending order
    for i in range(len(finallist)-1, 0, -1):
        for j in range(i):
            #compare both 0,1 indexes of tuple to maintain lexicographic order
            if(finallist[j][0] >= finallist[j+1][0] and finallist[j][1] >= finallist[j+1][1]):
               temp = finallist[j]
               finallist[j] = finallist[j+1]
               finallist[j+1] = temp                   
    print("The final list with one intermediate stop is: ", finallist)
    
l = [(1,2),(2,1)]
onehop(l)

"""
main logic:
1.
-for all pairs in the list l, we select each pair one by one
-We take the len(l)-1 because the indexes are less by one and we want to compare
similar to l[j] and l[j+1] ie one element with next element. Hence, we need to stop
when we reach the 2nd last element. This element has index len(l) - 2. But this
additional subtraction is avoided as range itself does not consider the last element

2.
Then we take the range(len(l)-1, 0, -1) ie similar to bubble sort and then assign
this range value to the next for loop of j

3. Then it checks for numbers from the next element as the 0th index will represent
the current city and we dont want to compare current with current. Also, we add
by one as we need to go upto last city and here we are not doing l[j] and l[j+1]
comparison.

4. Finally, when we find the match of the city, we check if it is already in the
intermediatelist ie finallist. If not, we add it

5. Note the comparison is: (1,2) and (2,3) ie we compare if element[1] matches
with anotherelement[0]. Then we can add element[0], anotherelement[1]

Hence, we get the final solution in this way
"""
