class Stack:
    def __init__(self):
        self.data = []

    def append(self, data):
        self.data.append(data)
        return data

    def pop(self):
        if len(self.data) == 0:
            return None
        temp = self.data[-1]
        self.data.pop()
        return temp
