class Queue:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.size() == 0

    def put(self,item):
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            result = self.items[0]
            self.items.remove(result)
            return result

    def clear(self):
        self.items = []

    def peek(self):
        if not self.isEmpty():
            return self.items[0]

t = Queue()
t.put(10)
t.put(20)
t.put(30)
print(t.size())
print(t.pop())
print(t.pop())
print(t.peek())
print(t.pop())
print(t.pop())