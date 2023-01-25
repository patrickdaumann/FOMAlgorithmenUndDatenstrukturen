from random import randint
from math import floor

class HashTable(object):
    def __init__(self, size, hashmethod):
        self.values = [None] * size
        self.hashmethod = hashmethod

    def divhash(self, key: int):
        return key % len(self.values)

    def multhash(self, key: int):
        A = 0.314152657
        return floor(((key*A)%1) * len(self.values))
        


    def inthash(self, key: int):
        if self.hashmethod == "division":
            return self.divhash(key)
        elif self.hashmethod == "multiplication":
            return self.multhash(key)

    def strhash(self, key: str):
        n = 0
        for i in key:
            n += ord(i)
        
        if self.hashmethod == "division":
            return self.divhash(n)
        elif self.hashmethod == "multiplication":
            return self.multhash(n)

    def insert(self, key: any, value: any):
        if isinstance(key, int):
            index = self.inthash(key)
        elif isinstance(key, str):
            index = self.strhash(key)
        
        if self.values[index] == None:
            self.values[index] = LinkedList()
        
        self.values[index].listInsert(value)

    def search(self, key):
        if isinstance(key, int):
            index = self.inthash(key)
        elif isinstance(key, str):
            index = self.strhash(key)

        return self.values[index].listSearch(key)

    def PrintValues(self):
        for i in self.values:
            i.listPrint()

class ListNode(object):
    def __init__(self, dataval:any):
        self.dataval = dataval
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None

    def listInsert(self, Value: any):
        NewNode = ListNode(Value)
        if self.head == None:
            self.head = NewNode
        else:
            x = self.head
            self.head = NewNode
            self.head.next = x
    
    def listPrint(self):
        x = self.head
        if(x != None):
            print(str(x.dataval), end="")
        while x.next != None:
            x = x.next
            print(f" - {str(x.dataval)}", end = "")

        print()

    def listSearch(self, key):
        x = self.head
        while x.dataval != key and x.next != None:
            x = x.next
        
        if x.dataval == key:
            return x.dataval
        
        else:
            return None


###############################
# Testcode

class user(object):
    def __init__(self, id, name, firstname):
        self.id = id
        self.name = name
        self.firstname = firstname

    def __str__(self) -> str:
        return f"User: {self.firstname} {self.name} ({self.id})"
    
    def save(self, HashTable: HashTable):
        HashTable.insert(key=self.id, value=self)



H1 = HashTable(4, hashmethod="division")
H2 = HashTable(4, hashmethod="multiplication")

for i in range(32):
    H1.insert(key = randint(1,100), value= i)
    H2.insert(key = randint(1,100), value= i)

#H1.insert(key = "Test", value="Test")

#user1 = user(id=4711, name="Daumann", firstname="Patrick")
#user1.save(H1)

print("H1: Division")
H1.PrintValues()
print("\nH2: Multiplication")
H2.PrintValues()