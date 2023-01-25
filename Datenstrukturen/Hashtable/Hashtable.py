# Import Dependencies
from random import randint
from math import floor


# Definition der Klasse Hashtabelle
class HashTable(object):
    def __init__(self, size, hashmethod):
        self.values = [None] * size
        self.hashmethod = hashmethod

    def divhash(self, key: int):
        # Hashfunktion nach der Divisionsmethode
        return key % len(self.values)

    def multhash(self, key: int):
        # Hashfunktion nach der Multiplikationsmethode
        A = 0.314152657  # Konstante zwischen 0 und 1
        return floor(((key*A) % 1) * len(self.values))

    def inthash(self, key: int):
        # Wrappermethode für das hashen von integer Werten
        if self.hashmethod == "division":
            return self.divhash(key)
        elif self.hashmethod == "multiplication":
            return self.multhash(key)

    def strhash(self, key: str):
        # Wrappermethode für das hashen von Strings
        n = 0
        for i in key:
            n += ord(i)

        if self.hashmethod == "division":
            return self.divhash(n)
        elif self.hashmethod == "multiplication":
            return self.multhash(n)

    def insert(self, key: any, value: any):
        # Insert Methode -> Neue werte in die Hashtabelle einfügen
        # Aufrufen der zum Typ passenden Wrappermethode
        if isinstance(key, int):
            index = self.inthash(key)
        elif isinstance(key, str):
            index = self.strhash(key)

        if self.values[index] == None:
            self.values[index] = LinkedList()

        # Einfuegen des Wertes am richtigen Index
        self.values[index].listInsert(value)

    def search(self, key):
        # Suchfunktion für einen gegebenen Schluessel
        if isinstance(key, int):
            index = self.inthash(key)
        elif isinstance(key, str):
            index = self.strhash(key)

        return self.values[index].listSearch(key)

    def PrintValues(self):
        # Ausgeben der Werte innerhalb der Hashtabelle in die Konsole
        index = 0
        for i in self.values:
            if isinstance(i, LinkedList):
                print(f"{index}:\t", end="")
                i.listPrint()
            else:
                print(f"{index}:\t[Nil]")
            index += 1


# Definition der Klassen für die Linkedlist (wird für Chainedhash benoetigt)
class ListNode(object):
    # Ein Knoten der Linkedlist
    def __init__(self, dataval: any):
        self.dataval = dataval
        self.next = None


class LinkedList(object):
    # die Linkedlist an sich
    def __init__(self):
        self.head = None

    def listInsert(self, Value: any):
        # Werte in die Linkedlist einfuegen
        NewNode = ListNode(Value)
        if self.head == None:
            self.head = NewNode
        else:
            x = self.head
            self.head = NewNode
            self.head.next = x

    def listPrint(self):
        # Ausgeben der Linkedlist
        x = self.head
        if (x != None):
            print(str(x.dataval), end="")
        while x.next != None:
            x = x.next
            print(f" - {str(x.dataval)}", end="")

        print()

    def listSearch(self, key):
        # Suchen eines Schluessels in der Linkedlist
        x = self.head
        while x.dataval != key and x.next != None:
            x = x.next

        if x.dataval == key:
            return x.dataval

        else:
            return None


###############################
# Testcode

# Userklasse zum testen der Funktion der Hashtabelle mit nicht Standard Datentypen
class user(object):
    def __init__(self, id, name, firstname):
        self.id = id
        self.name = name
        self.firstname = firstname

    def __str__(self) -> str:
        return f"User: {self.firstname} {self.name} ({self.id})"

    def save(self, HashTable: HashTable):
        HashTable.insert(key=self.id, value=self)


HashTableSize = 8

# Erstellen von Hashtabelle mit den beiden Hashingmethoden
H1 = HashTable(HashTableSize, hashmethod="division")
H2 = HashTable(HashTableSize, hashmethod="multiplication")

# Befuellen der Hashtabelle mit Zufallszahlen
for i in range(32):
    H1.insert(key=randint(1, 100), value=i)
    H2.insert(key=randint(1, 100), value=i)

# Einfuegen eines Teststrings in die Hashtabellen
H1.insert(key="Test", value="Test")
H2.insert(key="Test", value="Test")

# Einfuegen eines Userobjektes in die Hashtabellen
user1 = user(id=4711, name="Daumann", firstname="Patrick")
user1.save(H1)
user1.save(H2)

# Ausgeben der Hashtabellen
print("H1: Division\n", 32*'-')
H1.PrintValues()
print("\nH2: Multiplication\n", 32*'-')
H2.PrintValues()