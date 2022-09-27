from random import randint

"""
Pseudocode:

Insertion-Sort(A,n)
    for j = 2 to n
        key = A[j]
        //Insert A[j] into the sorted Sequence A[1 .. j .. -1]
        i = j - 1
        while i>0 and A[i]>key
            A[i+1] = A[i]
            i = i-1
        A[i+1] = key
"""

#insert sort algorithm
def InsertSort(A):
    '''sorts given Array with insertion sort algorithm (destructive)'''
    for j in range(1, len(A)):
        key = A[j]
        i = j-1
        while (i > -1 and A[i]>key):
            A[i+1] = A[i]
            i = i-1
        A[i+1] = key


#initialize array
n = 10
feld = []

#initialize array with random integers
for i in range(n):
    feld.append(randint(100, 999))

#Print unsorted array
print(f"Unsortiert:\t {feld}")

#sort array
InsertSort(feld)

#print sorted array
print(f"Sortiert:\t {feld}")