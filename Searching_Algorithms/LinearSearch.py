def linearSearch(A, key):
    index = 0
    while index < len(A):
        if A[index] == key:
            return index
        index += 1
    return -1


A = [92, 18, 95, 65, 55, 47, 44]
found = linearSearch(A, 100)
if found !=-1:
    print("result:", found)
else:
    print("key not found....")
