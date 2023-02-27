def BinarySearchingRecursive(A,key,L,R):
    if L>R:
        return -1
    else:
        m=(L+R)//2
        if key==A[m]:
            return m
        elif key<A[m]:
            return BinarySearchingRecursive(A,key,L,m-1)
        elif key>A[m]:
            return BinarySearchingRecursive(A,key,m+1,R)


A = [11,22,33,34,35,36,37,38,39,40]
found =BinarySearchingRecursive(A, 35,0,len(A)-1)
if found !=-1:
    print("result:", found)
else:
    print("key not found....")

