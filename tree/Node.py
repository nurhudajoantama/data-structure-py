import imp
from typing import List


class Node:
    def __init__(self, data):
        self.data = data
        self.child: List[Node] = []

    def addChild(self, data):
        self.child.append(Node(data))
