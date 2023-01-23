class linkedlist:
    def __init__(self) -> None:
        self.head = None
    
    def addnode(self, newnode) -> None:
        if self.head == None:
            self.head = newnode
        
        else:
            x = self.head
            while x.next != None:
                x = x.next

            x.next = newnode

    def printlist(self) -> None:
        x = self.head
        while x != None:
            x.dataval.printvalues()
            x = x.next


class listnode:
    def __init__(self, dataval) -> None:
        self.dataval = dataval
        self.next = None

class Hashtable:
    def __init__(self, size: int) -> None:
        self.values = [None] * size

    def add(self, value: any, key: any, hashfunction):

        address = hashfunction(key, len(self.values))
        if self.values[address] == None:
            self.values[address] = linkedlist()

        else:
            self.values[address].addnode(listnode(value))

    def findvalue(self, key: any, hashfunction):
        return self.values[hashfunction(key, len(self.values))]


class user:
    def __init__(self, username: str, id: int, firstname: str, surname: str, email: str) -> None:
        self.username = username
        self.id = id
        self.firstname = firstname
        self.surname = surname
        self.email = email

    def printvalues(self) -> None:
        print(f"Username: {self.username}\nID: {self.id}\nFirstname: {self.firstname}\nSurname: {self.surname}\nE-Mail: {self.email}")



########################################
hashfunction = lambda x, n:x % n

user1 = user("JDoe19", 999, "John", "Doe", "john.doe@contoso.com")

Hash1 = Hashtable(size=20)

Hash1.add(user1, user1.id, hashfunction)

Hash1.findvalue(user1.id, hashfunction).printlist()

for x in Hash1.values:
    if x is Hashtable:
        x.printlist()
