
L = [43, 32, 22, 78, 63, 57, 91, 13]

def quicksort(L, left,right):
    if right - left <=1:    #base case
        return ()

    yellow = left+1 # set yellow pointer for nos less than pivot

    for green in range(left+1, right):  # green pointer traverses the list
        if L[green] <= L[left]:
            (L[yellow],L[green]) = (L[green],L[yellow]) # if number less than pivot, swap
            yellow = yellow + 1

    (L[left], L[yellow-1]) = (L[yellow-1],L[left])

    quicksort(L, left, yellow-1) #recursively call for left and right lists
    quicksort(L, yellow, right)

quicksort(L, 0, len(L))
print(L)
