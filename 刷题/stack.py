class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def clear(self):
        del self.items[:]

    def empty(self):
        return len(self.items)==0

    def size(self):
        return len(self.items)

    def top(self):
        return self.items[-1]