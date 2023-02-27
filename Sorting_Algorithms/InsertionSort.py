def InsertionSort(A):
    n=len(A)
    for i in range(1,n):
        cvalue=A[i]
        position=i
        while position > 0 and A[position-1] > cvalue:
            A[position]=A[position-1]
            position=position-1
        A[position]=cvalue

A=[9,8,7,6,5,4,3,2,1]
print("Original List:",A)
InsertionSort(A)
print("Sorted List:",A)