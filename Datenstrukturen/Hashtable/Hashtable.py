class HashTable(object):
    def __init__(self, size):
        self.values = [None] * size

    def inthash(self, x: int):
        return x % len(self.values)

    def strhash(self, x: str):
        n = 0
        for i in x:
            n += ord(i)
        
        return n %len(self.values)

    def insert(self, value: any):
        if isinstance(value, int):
            index = self.inthash(value)
        elif isinstance(value, str):
            index = self.strhash(value)
        
        if self.values[index] == None:
            self.values[index] = LinkedList()
        
        self.values[index].listInsert(value)

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
            print(x.dataval, end="")
        while x.next != None:
            x = x.next
            print(f" - {x.dataval}", end = "")

        print()

###############################
# Testcode
H1 = HashTable(10)

for i in range(10):
    H1.insert(i)

H1.insert("Test")

H1.PrintValues()