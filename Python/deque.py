class Deque():
    def __init__(self):
        self.items = [] 
    def addFront(self, item):
        self.items.insert(0, item)
    def addRear(self, item):
        self.items.append(item)
    def removeFront(self):
        return self.items.pop(0)
    def removeRear(self):
        return self.items.pop()
    def displaydeque(self):
        for i in reversed(self.items):
            print(i)
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)


def main():
    deq = Deque()
    deq.addFront(1)
    deq.addFront(2)
    deq.addFront(3)
    deq.addFront(4)
    deq.addRear("z")
    deq.displaydeque()
    print("\n\n\n")
    deq.removeRear()
    deq.removeRear()
    deq.removeFront()
    deq.displaydeque()

if __name__ == "__main__":
    main()

def palindromeDEQUE(message):
    deqObj = Deque()
    message = message.lower()
    for msg in message:
        deqObj.addRear(msg)
    
    i=0
    length = deqObj.size()
    while deqObj.size() > 1:
        front = deqObj.removeFront()
        end = deqObj.removeRear()
        if(front != end):
            return False
        #if (front == end):
           # if(deqObj.size() > 1): #or (front==None) or (end==None)):
            #        return True
           # continue
       # else:
        #    break
       # return True
    return True

print(palindromeDEQUE("racecar"))
print(palindromeDEQUE("notapali"))
print(palindromeDEQUE("madam"))
print(palindromeDEQUE("anna"))
print(palindromeDEQUE("noon"))
print(palindromeDEQUE("test"))
