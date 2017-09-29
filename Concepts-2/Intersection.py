def intersection(L1, L2):
    common = [] 
    for i in range(len(L1)):    # take the length of L1 and iterate that many times
        if L1[i] in L2:     # if the element in L1 is present in L2
            if not L1[i] in common: # and if it has already not been added to common list
                common.append(L1[i])    # add it to the list
    return common       #return the list

print(intersection([10, 20, 30, 40, 50, 80, 90, 100, 10, 20], [30, 40, 50, 60, 70]))
print(intersection((10, 20, 30, 40, 50), (30, 40, 50, 60, 70)))
# print(intersection({10, 20 ,30, 40, 50}, {30, 40, 50, 60, 70}))
# note that as we are using iteration, and set does not support indexing, we
# will get error here. Note that in the next function definition, we are not
# using indexing. Hence, set will work.
def intersection(L1, L2):
    common = []
    for x in L1:
        if x in L2 and not x in common:
            common.append(x)
    return (common) 
print(intersection([10, 20, 30, 40, 50], [30, 40, 50, 60, 70]))
print(intersection((10, 20, 30, 40, 50), (30, 40, 50, 60, 70)))
print(intersection({10, 20 ,30, 40, 50}, {30, 40, 50, 60, 70}))

