def SelectionSort(A):
    n=len(A)
    for i in range(n-1):
        positions=i
        for j in range(i+1,n):
            if A[j] < A[positions]:
                positions=j

         #Swapping the numbers        
        A[i], A[positions] = A[positions], A[i]

A=[9,8,7,6,5,4,3,2,1]
print("Original List:",A)
SelectionSort(A)
print("Sorted List:",A)