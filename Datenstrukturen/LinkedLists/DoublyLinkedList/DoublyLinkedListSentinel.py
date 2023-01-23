class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.prev = None
        
class Linkedlist:
    def __init__(self) -> None:
        self.nil = Node(None)
        self.nil.next = self.nil
        self.nil.prev = self.nil

    def listsearch(self, key):
        x = self.nil.next
        while x is not self.nil and x.data != key:
            x = x.next

        return x

    def listinsert(self, x: Node):
        x.next = self.nil.next
        self.nil.next.prev = x
        self.nil.next = x
        x.prev = self.nil

    def listdelete(self, x: Node):
        x.prev.next = x.next
        x.next.prev = x.prev

    def listprint(self):
        x = self.nil.next
        while True:
            print(x.data, end="")
            if x.next is not self.nil:
                print(" - ", end="")
            x = x.next
            if x == self.nil:
                break
        print()

#######################################
# Testcode

l = Linkedlist()

for i in range(1, 10):
    l.listinsert(Node(i))

l.listprint()

l.listdelete(l.listsearch(key = 2))
l.listdelete(l.listsearch(key = 7))
l.listdelete(l.listsearch(key = 5))

l.listinsert(Node(10))

l.listprint()