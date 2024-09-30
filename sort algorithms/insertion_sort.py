"""
Each time it selects an element and returns to the beginning
    of the list and compares to find its place

"""

A = [5, 2, -3, 4, 6, -7, 1, 9, 12, 5, -6]

count = 0
for k in range(1, len(A)):
    item = A[k]
    i = k
    while i > 0 and item < A[i - 1]:

        A[i] = A[i - 1]
        print(A)
        i -= 1
        count += 1
    A[i] = item
    # print(A)

print(count)
