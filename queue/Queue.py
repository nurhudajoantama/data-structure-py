class Queue:
    def __init__(self):
        self.data = []

    def enQueue(self, data):
        self.data.append(data)
        return data

    def deQueue(self):
        if len(self.data) == 0:
            return None
        return self.data.pop(-1)
