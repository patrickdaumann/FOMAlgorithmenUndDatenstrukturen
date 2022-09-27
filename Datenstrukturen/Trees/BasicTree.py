class node:
    def __init__(self, dataval):
        self.dataval = dataval
        self.left = None
        self.right = None

class tree:
    def __init__(self):
        self.root = None

    def printleft(self):
        x = self.root
        while x != None:
            print(x.dataval)
            x = x.left

tree1 = tree()
node1 = node(dataval=10)
node2 = node(dataval=12)
node3 = node(dataval=13)
node4 = node(dataval=14)

tree1.root = node1
tree1.root.left = node2
tree1.root.right = node3
tree1.root.left.left = node4

tree1.printleft()