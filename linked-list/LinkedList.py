from Node import Node


class LinkedList:
    def __init__(self):
        self.head: Node = None

    def push(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def append(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            return

        temp = self.head
        while temp.next != None:
            temp = temp.next

        temp.next = newNode

    def insertAt(self, at, data):
        newNode = Node(data)

        if at == 0:
            if self.head == None:
                newNode.next = None
            else:
                newNode.next = self.head.next
            self.head = newNode
            return

        temp = self.head
        for i in range(at-1):
            if (temp.next == None) and (i != at-1):
                raise Exception('linked list not sufficient')
            temp = temp.next

        newNode.next = temp.next
        temp.next = newNode

    def read(self, at):
        temp = self.head
        for _ in range(at):
            if temp.next == None:
                return None
            temp = temp.next
        if temp == None:
            return None
        return temp.data

    def pop(self):
        temp = self.head
        if temp.next == None:
            self.head = None
            return
        while temp.next.next != None:
            temp = temp.next
        temp.next = None

    def removeAt(self, at):
        temp = self.head
        if self.head == None:
            raise Exception('Not have an data')
        if at == 0:
            self.head = temp.next

        for i in range(at-1):
            if (temp.next.next == None) and (i != at-1):
                raise Exception('Not have an data')
            temp = temp.next
        temp.next = temp.next.next
