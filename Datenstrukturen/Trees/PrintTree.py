class Node(object):
    def __init__(self, key) -> None:
        self.key = key
        self.left = None
        self.right = None

    def printnodesrecurse(self, x) -> None:
        if x != None:
            print(x.key)
            self.printnodesrecurse(x.left)
            self.printnodesrecurse(x.right)

class BinaryTree(object):
    def __init__(self, rootval) -> None:
        self.root = Node(rootval)

    def printtree(self) -> None:
        self.root.printnodesrecurse(self.root)



Tree = BinaryTree(1)

Tree.root.left = Node(2)
Tree.root.right = Node(3)
Tree.root.left.left = Node(4)
Tree.root.left.right = Node(5)
Tree.root.right.left = Node(6)
Tree.root.right.right = Node(7)


Tree.printtree()