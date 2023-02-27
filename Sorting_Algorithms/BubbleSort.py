def BubbleSort(A):
    n=len(A)
    for passes in range(n-1,0,-1):
        for i in range(passes):
            if A[i] > A[i+1]:
                A[i],A[i+1]=A[i+1],A[i]

A=[9,8,7,6,5,24,3,2,1,10]
print("Original List:",A)
BubbleSort(A)
print("Sorted List:",A)