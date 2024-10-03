"""
Merge Sort is a divide-and-conquer sorting algorithm. 
It recursively splits the list into two halves, sorts each half, 
and then merges the sorted halves back together to form a completely sorted list.

"""


def mergesort(A):
    if len(A) < 2:
        return A

    mid = len(A) // 2
    B = A[:mid]
    C = A[mid:]

    B = mergesort(B)
    C = mergesort(C)
    i = j = 0
    A = []
    while i < len(B) and j < len(C):
        if B[i] <= C[j]:
            A += [B[i]]
            i += 1
        else:
            A += [C[j]]
            j += 1
        print(A)
    A += B[i:] + C[j:]
    print(A)
    return A


mergesort([3, 5, 1, 8, 43, 9, 3, 0])
