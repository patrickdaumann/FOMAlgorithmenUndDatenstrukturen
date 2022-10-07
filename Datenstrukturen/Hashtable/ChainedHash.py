from random import randint

# Class definitions
class node:
    def __init__(self, dataval):
        self.next = None
        self.prev = None
        self.dataval = dataval

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def ListInsert(self, dataval, verbose:bool=False):
        x = node(dataval=dataval)
        x.next = self.head
        if self.head != None:
            self.head.prev = x
        self.head = x
        x.prev = None
        if verbose:
            print(f"{x.dataval} inserted!")


    def ListDelete(self, verbose:bool=False):
        x = self.head
        if x .prev != None:
            x.prev.next = x.next
        else:
            self.head = x.next
        if x.next != None:
            x.next.prev = x.prev
        
        if verbose:
            print(f"{x.dataval} removed!")

    def PrintList(self):
        x = self.head
        if x == None:
            print("[Empty List]", end="")

        while x != None:
            print(f"{x.dataval}", end= " ")
            x = x.next
        
        else:
            print("")

class ChainedHashTable:
    
    def __init__(self, size):
        self.data = [None] * size
        
        for i in range(size):
            self.data[i] = DoublyLinkedList()

        self.hashfunc = lambda x, n: x % n

    def HashInsert(self, key):
        self.data[self.hashfunc(key, len(self.data))].ListInsert(key)

    def HashSearch(self, key):
        return [self.hashfunc(key, len(self.data))]

    def HashDelete(self, key):
        self.data[self.hashfunc(key, len(self.data))].ListDelete(key)
    
    def print(self):
        for i in self.data:
            i.PrintList()
    

Hashtable1 = ChainedHashTable(10)

for i in range(99): 
    Hashtable1.HashInsert(i)

Hashtable1.print()