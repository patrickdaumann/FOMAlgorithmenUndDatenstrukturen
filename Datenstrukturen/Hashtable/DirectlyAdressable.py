class HashTable:
    
    def __init__(self, size):
        self.data = [None] * size
        self.hashfunc = lambda x, n: x % n

    def HashInsert(self, key):
        self.data[self.hashfunc(key, len(self.data))] = key

    def HashSearch(self, key):
        return [self.hashfunc(key, len(self.data))]

    def HashDelete(self, key):
        self.data[self.hashfunc(key, len(self.data))] = None
    
    def print(self):
        print(self.data)



test = HashTable(10)
test.HashInsert(10)
test.HashInsert(2)
test.HashInsert(3)

test.print()

test.HashDelete(3)
test.print()
