class Heap:
    def __init__(self, size):
        self.A = [None] * size
        self.i = 0

    def Right(self, n):
        return n * 2 + 1
    
    def Left(self, n):
        return n * 2

    def append(self, value):
        self.A[self.i] = value
        self.i += 1

H1 = Heap(10)
H1.append(1)
H1.append(2)
H1.append(3)
H1.append(4)
print(H1.A)