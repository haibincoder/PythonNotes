# Stack, pop the last element
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()

    def peek(self):
        if not self.isEmpty():
            return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


class Stack2:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.items.append(item)

    def clear(self):
        self.items = []

    def pop(self):
        if not self.isEmpty():
            print(self.size())
            return self.items.pop()

    def peek(self):
        if not self.isEmpty():
            return self.items[self.size() - 1]

s = Stack2()
s.push("first")
s.push("sencond")
print(s.pop())
print(s.peek())
print(s.pop())
print(s.pop())
