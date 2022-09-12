#Node Klasse
class node:
    def __init__(self, dataval = None):
        self.next = None
        self.dataval = dataval

#Singly Linked List
class SLinkedList:
    def __init__(self):
        self.head = None

    def AddNode(self, newnode):
        x = self.head
        self.head = newnode
        newnode.next = x
    
    def PrintValues(self):
        x = self.head
        while x != None:
            print(x.dataval)
            x = x.next
    
    def SearchKey(self, key):
        i = 1
        x = self.head
        while x != None:
            if x.dataval == key:
                print(f"Key: {key} an Position: {i} gefunden!")
                break
            else:
                i += 1
                x = x.next
        if x == None:
            print(f"Key: {key} nicht in Liste!")


#Neue Liste initialisieren
List = SLinkedList()

#Liste mit Werten füllen
for i in range(10):
    List.AddNode(node(dataval=i))

List.SearchKey(key=1)

#Liste ausgeben
#List.PrintValues()