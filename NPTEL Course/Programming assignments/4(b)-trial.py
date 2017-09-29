def onehop(l):

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
    for city in finallist:
        if(city[0] == city[1]):
            finallist.remove(city)
            
    #sort the tuples in ascending order
    for i in range(len(finallist)-1, 0, -1):
        for j in range(i):
            #compare both 0,1 indexes of tuple to maintain lexicographic order
            if(finallist[j][0] >= finallist[j+1][0] and finallist[j][1] >= finallist[j+1][1]):
               temp = finallist[j]
               finallist[j] = finallist[j+1]
               finallist[j+1] = temp                   
    return(finallist)
