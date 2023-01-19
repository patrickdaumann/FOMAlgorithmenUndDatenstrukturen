from random import randint

def Left(i):
    i +=1
    return (2*i)-1

def Right(i):
    i+=1
    return 2*i

def MaxHeapify(A, i, n):
    l = Left(i)
    r = Right(i)
    
    if l <= n and A[l]>A[i]:
        largest = l
    else:
        largest = i
    if r <=n and A[r]>A[largest]:
        largest = r

    if largest != i:
        cache = A[i]
        A[i] = A[largest]
        A[largest] = cache
        MaxHeapify(A, largest, n)

def BuildMaxHeap(A, n):
    x = (n//2)-1
    for i in reversed(range(0, x)):
        MaxHeapify(A, i, len(A)-1)  #???

n = 10
A = [None] * n

for i in range(n):
    A[i] = randint(1, 10)

print(A)
#MaxHeapify(A, 1, len(A))
BuildMaxHeap(A, len(A))
print(A)