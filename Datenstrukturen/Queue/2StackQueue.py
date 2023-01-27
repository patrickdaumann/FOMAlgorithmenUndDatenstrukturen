"""
Aufgabe 4: Implementierung Warteschlange über Stapel:
Zeigen Sie, wie eine Warteschlange unter Verwendung von zwei Stapeln implementiert werden kann. Analysieren Sie die Laufzeit der Warteschlangenoperationen.

Laufzeit = O(n)
"""

class Stack(object):
    def __init__(self, size: int) -> None:
        self.values = [None] * size
        self.top = 0

    def isempty(self) -> bool:
        if self.top == 0:
            return True
        else:
            return False

    def isfull(self) -> bool:
        if self.top == len(self.values):
            return True
        else:
            return False

    def push(self, x):
        if not self.isfull():
            self.values[self.top] = x
            self.top += 1
        else:
            raise Exception('Stack is already full!')

    def pop(self):
        if not self.isempty():
            self.top -= 1
            return self.values[self.top]
        else:
            return None


class TwoStackQueue(object):
    def __init__(self, values):
        size = len(values)
        self.inputstack = Stack(size)
        self.outputstack = Stack(size)

        for i in values:
            self.inputstack.push(i)
        
        while not self.inputstack.isempty():
            self.outputstack.push(self.inputstack.pop())

    def pop(self):
        if not self.outputstack.isempty():
            return self.outputstack.pop()

Stack1 = Stack(10)

for i in range(10):
    Stack1.push(i)


values = [1,2,3,4,5,6,7,8,9,10]

TsQ = TwoStackQueue(values=values)

for i in range(len(values)):
    print(TsQ.pop())