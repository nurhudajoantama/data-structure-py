from tree.Node import Node


class Tree:
    def __init__(self):
        self.root = None

    def addRoot(self, data):
        if self.root is not None:
            raise Exception("Root already exists")
        self.root = Node(data)
