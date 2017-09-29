def intersection_indexing(L1,L2):
    common = []
    for i in range(len(L1)):
        if L1[i] in L2:
            if not L1[i] in common:
                common.append(L1[i])
    return common

print(intersection_indexing([10, 20 ,30],[20, 50, 40]))
print(intersection_indexing((20, 30, 20, 40, 50),(20, 30, 40)))
print("trying out with strings: ")
print(intersection_indexing(["hello","world","empty"],["hello","empty", "new"]))

def intersection_noindex(L1,L2):
    common = []
    for x in L1:
        if x in L2 and not x in common:
            common.append(x)
    return (common)
print ("\nnew function for intersection:")
print(intersection_noindex({10, 20 ,30}, { 20, 30, "hello", 3.142}))
print(intersection_noindex((3.142, 99, "hey", "oK"),(3.142, "Ok", 99, "hey")))
print(intersection_noindex([3.142, 99, "hey", "oK"],[3.142, "Ok", 99, "hey"]))

