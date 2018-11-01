#Implementation of the Python's built in "List" object
#Missing a whole bunch of methods but the important ones are provided

class List:
    def __init__(self):
        self.items = []
    
    def add(self, item):
        self.items.append(item)

    def remove(self, item):
        self.items.remove(item)

    def search(self, item):
        return item in self.items
    
    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def append(self, item):
        self.items.append(item)

    def index(self, item):
        return self.items.index(item)
    
    def insert(self, pos, item):
        self.items.insert(pos, item)

    def pop(self):
        return self.items.pop()

    def pop2(self, pos):
        return self.items.pop(pos)


