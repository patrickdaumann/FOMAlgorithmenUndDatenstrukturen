from random import randint

class queue:
    def __init__(self, size: int) -> None:
        self.values = [None] * size
        self.head = 0
        self.tail = 0

    def isempty(self):
        if self.head == self.tail:
            return True
        else:
            return False
    
    def incrementhead(self):
        if self.head +1 > len(self.values):
            self.head = 0

        else:
            self.head +=1
 
    def incrementtail(self):
        if self.tail +1 > len(self.values)-1:
            self.tail = 0

        else:
            self.tail +=1
        
 
    def enqueue(self, element) -> None:
        self.values[self.tail] = element
        self.incrementtail()

    def dequeue(self) -> any:
        x = self.values[self.head]
        self.incrementhead()
        return x


#####################################
# Testcode

q1 = queue(32)

for i in range(6):
    q1.enqueue(i)

while not q1.isempty():
    print(q1.dequeue())


for i in range(100, 124):
    q1.enqueue(i)

while not q1.isempty():
    print(q1.dequeue())