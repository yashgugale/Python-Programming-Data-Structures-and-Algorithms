def transpose(l):
    masterlist = [[] for i in range(len(l[0]))] #1
    for i in range(len(l[0])):  #2
        for j in range(len(l)): #3
            masterlist[i].append(l[j][i])#4
    return(masterlist)

print(transpose([[1,1,1],[2,2,2],[3,3,3]]))


"""
Sample list = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
Here:
size of outer list is 4
size of inner list is 3
1 - Create a list of lists such that the number of inner lists is equal to the
length of the matrix ie, number of columns
Thus, we have 3 empty lists in the master list
2 - For all the length of the inner list do the following: ie in the above example,
do it 3 times.
3 - for the length of outer list, ie 4 times,
4 - add each element given by position i
to master list with position i and inner list must be j ie 4 as the size of list is 4

-------------------------------------------------------------------------------
3.
A two dimensional matrix can be represented in Python row-wise, as a list of lists: each inner list represents one row of the matrix. For instance, the matrix
1  2  3
4  5  6 
would be represented as [[1,2,3],[4,5,6]].

The transpose of a matrix makes each row into a column. For instance, the transpose of the matrix above is
1  4  
2  5
3  6
Write a Python function transpose(m) that takes as input a two dimensional matrix using this row-wise representation and returns the transpose of the matrix using the same representation.

Here are some examples to show how your function should work. You may assume that the input to the function is always a non-empty matrix.

>>> transpose([[1,4,9]])
[[1], [4], [9]]

>>> transpose([[1,3,5],[2,4,6]])
[[1,2], [3,4], [5,6]]
0 
>>> transpose([[1,1,1],[2,2,2],[3,3,3]])
[[1,2,3], [1,2,3], [1,2,3]]
"""
