from random import randint

class stack:
    def __init__(self, size: int) -> None:
        self.values = [None] * size
        self.top = 0

    def push(self, element: any) -> None:
        self.values[self.top] = element
        self.top +=1

    def stackempty(self) -> bool:
        if self.top == 0:
            return True

        else:
            return False

    def pop(self) -> any:
        if self.stackempty() == False:
            self.top -=1
            value = self.values[self.top]
            return value

    def printelements(self) -> None:
        if self.stackempty() == False:
            for i in range(self.top -1, -1, -1):
                print(self.values[i], end=", ")
            print()

################################
# Testcode


stack1 = stack(10)

for i in range(0,5):
    stack1.push(randint(1, 100))

stack1.push(5)
stack1.printelements()
stack1.push(10)
stack1.printelements()
print(stack1.pop())
stack1.printelements()