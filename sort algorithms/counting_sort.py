"""

We have a certain number of categories, the number of which should be less than the number of objects in our data (this is the ideal state of this algorithm)
Then we start counting how many data we have from each category and then categorize.

"""

A = [1, 2, 2, 2, 1, 3, 3, 8, 1, 2, 4, 5]
m = max(A)
B = [0] * (m + 1)
C = []
for i in A:
    B[i] += 1

for i, j in enumerate(B):
    C.extend([i] * j)

print(C)
