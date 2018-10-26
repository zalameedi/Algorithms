class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self, item):
        self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop(0)
    def size(self):
        return len(self.items)
    def print(self):
        for i in reversed(self.items):
            print(i)
    def peek(self):
        return self.items[0]
    def isEmpty(self):
        return self.items == []

q = Queue()
q.enqueue(4)
q.enqueue(21)
q.enqueue("z")
#print(q.size())
q.print()
q.dequeue()
print("\n")
q.print()

