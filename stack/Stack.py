class Stack:
    def __init__(self):
        self.data = []

    def push(self, data):
        self.data.append(data)
        return data

    def pop(self):
        if len(self.data) == 0:
            return None
        temp = self.data[-1]
        self.data.pop()
        return temp

    def peek(self):
        if len(self.data) == 0:
            return None
        return self.data[-1]
