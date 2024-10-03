"""
Selection Sort is a simple comparison-based sorting algorithm. 
It repeatedly selects the smallest (or largest) element from the 
unsorted portion of the list and swaps it with the first unsorted element, 
gradually sorting the list in place.


"""

A = [1, 0, -5, 10, 11, 25, 3]
n = len(A)

for i in range(n - 1):
    selection = i
    for j in range(i + 1, n):
        if A[j] < A[selection]:
            selection = j
    A[i], A[selection] = A[selection], A[i]
    print(A)
