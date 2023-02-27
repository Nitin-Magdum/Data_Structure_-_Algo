import math
def BinarySearchingInterative(A,key):
    L=0
    R=len(A)-1
    while L<=R:
        m=math.floor((L+R)/2)
        if key==A[m]:
            return m
        elif key<A[m]:
            R=m-1
        elif key>A[m]:
            L=m+1
    return -1

A = [11,22,33,34,35,36,37,38,39,40]
found = BinarySearchingInterative(A, 30)
if found !=-1:
    print("result:", found)
else:
    print("key not found....")

