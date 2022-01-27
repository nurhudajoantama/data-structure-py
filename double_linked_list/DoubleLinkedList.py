from hashlib import new
from double_linked_list.Node import Node


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def read(self, at):
        if at > self.length:
            raise Exception('linked list not sufficient')

        if at > self.length / 2:
            temp = self.tail
            for _ in range(self.length-at-1):
                if temp.prev == None:
                    return None
                temp = temp.prev
        else:
            temp = self.head
            for _ in range(at):
                if temp.next == None:
                    return None
                temp = temp.next
        if temp == None:
            return None
        return temp.data

    def append(self, data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
            self.length += 1
            return data

        self.tail.next = Node(data)
        self.tail.next.prev = self.tail
        self.tail = self.tail.next
        self.length += 1

    def insert(self, at, data):
        newNode = Node(data)
        if at == 0:
            if self.head == None:
                newNode.next = None
                self.tail = newNode
            else:
                self.head.prev = newNode
                newNode.next = self.head
            self.head = newNode
            self.length += 1
            return data

        if at > self.length:
            raise Exception('linked list not sufficient')
        at -= 1
        if at > self.length / 2:
            temp = self.tail
            for _ in range(self.length-at-1):
                if temp.prev == None:
                    return None
                temp = temp.prev
        else:
            temp = self.head
            for _ in range(at):
                if temp.next == None:
                    return None
                temp = temp.next
        if temp == None:
            return None
        newNode.next = temp.next
        newNode.prev = temp
        temp.next = newNode
        if newNode.next != None:
            newNode.next.prev = newNode
        else:
            self.tail = newNode
        if at == self.length:
            self.tail = newNode
        self.length += 1
        return data
