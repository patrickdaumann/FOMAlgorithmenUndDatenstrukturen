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
        while x != None:
            print(x.dataval, end= " ")
            x = x.next
        else:
            print("")


######Testing Code##############################
#Verbose Mode: Set Printing for list-inserts and list-deletes
verbose: bool = False

#Init list
list1 = DoublyLinkedList()

#Fill list with random values
for i in range(5):
    list1.ListInsert(randint(1, 100), verbose=verbose)

#List operations
list1.PrintList()
list1.ListDelete(verbose=verbose)
list1.PrintList()
list1.ListDelete(verbose=verbose)
list1.PrintList()
list1.ListInsert(randint(1000, 2400), verbose=verbose)
list1.ListInsert(randint(3000, 10000), verbose=verbose)
list1.PrintList()