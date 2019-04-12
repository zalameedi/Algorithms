#Construct node class
class Node:
    def __init__(self, data=None):
        self.data=data
        self.next = None 
        #Two entries within a node

class LinkedList:
    def __init__(self):
        self.head=Node() #Head node is not accessible. Placeholder for first element
    def append(self, data): #Iterates through each node starting from head
        newNode = Node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = newNode
    def length(self): #Same concept as append except we have an accumulator for length
        i = 0
        cur = self.head
        while cur.next != None:
            i += 1
            cur = cur.next
        return i
    def traverseList(self): #Iterates through each node and prints out the data
        cur = self.head
        print("START")
        while cur.next != None:
            cur = cur.next # Skip the head node
            print(cur.data,"->")
        print("END")
    def ToList(self): #Converts all the node's data entries to a list
        myList = []
        cur = self.head
        while cur.next != None:
            cur = cur.next
            myList.append(cur.data)
        return myList
    def extract(self, index): #Index technique for extracting a certain data node
        try:
            if(index >= self.length()):
                return 1
            cur = self.head
            ind = 0
            while True:
                if ind == index:
                    return cur.data
                ind += 1
                cur = cur.next
        except:
            print("FAILED")
    def remove(self, data): #Deletes nodes. set them to NONE (Auto garbage collection)
        pHead = self.head
        if(pHead.data == data) and (pHead is not None):
            self.head = pHead.next #Set a new head
            pHead=None #Deleted the head
            return
        while(pHead is not None):
            if(pHead.data == data):
                break #Found the data entry
            prev = pHead
            pHead = pHead.next #Keep track of previous and next links
        if(pHead == None): #Key was not found
            return
        prev.next = pHead.next
        pHead = None
    def ToDict(self):
        cur = self.head
        myDict = {}
        i = 0
        while (cur.next != None):
            cur = cur.next
            myDict[i]=cur.data
            i += 1
        return myDict
            


def main():
    # Creating the obj and mess around
    LL = LinkedList()
    LL.append(21) 
    LL.append("Programmer")
    LL.append("Anywhoozies")
    LL.traverseList()
    print("Length: {0}".format(LL.length()))
    tempL = LL.ToList()
    print("List format: ", tempL)
    print("2nd Index: {0}".format(LL.extract(2)))
    print("Deleted Node")
    LL.remove(21)
    LL.traverseList()
    myDict = LL.ToDict()
    print("Dictionary of Linked List: ", myDict)

if __name__ == "__main__":
    main()
