def merge(A,B):
    (C, m, n) = ([], len(A), len(B))
    (i, j) = (0, 0)

    while i+j < m+n:
        if i == m:
            C.append(B[j])
            j = j+1
        elif j == n:
            C.append(A[i])
            i = i+1
        elif A[i] <= B[j]:
            C.append(A[i])
            i = i+1
        elif A[i] > B[j]:
            C.append(B[j])
            j = j+1

    return(C)
l = [10,30,40,50]
m = [5, 15, 25]
L = merge(l,m)
print(L)

def mergesort(A, left, right):
    if right - left <= 1:
        return(A[left:right])

    if right - left > 1:
        mid = (left+right)//2

        L = mergesort(A,left,mid)
        R = mergesort(A,mid,right)

        return(merge(L,R))
