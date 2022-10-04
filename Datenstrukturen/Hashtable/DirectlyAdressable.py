def HashInsert(A, key, f):
    A[f(key, len(A))] = key

def HashSearch(A, key, f):
    return A[f(key, len(A))]

def HashDelete(A, key, f):
    A[f(key, len(A))] = None 


n = 8
A = [None] * n
hash = lambda x, n: x % n

HashInsert(A, 10, hash)
HashInsert(A, 11, hash)
HashInsert(A, 12, hash)
print(A)

print(HashSearch(A, 10, hash))

HashDelete(A, 10, hash)
print(A)