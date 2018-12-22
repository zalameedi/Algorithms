#Implementation of the HashTable data structure

class HashTable:
    def __init__(self, size):
        self.size = size # Prime number to accomodate collision algorithm
        self.keylist = [None] * self.size #Two lists to contain key, data
        self.valuelist = [None] * self.size
     
    def hash(self, value):
        if type(value) == str:
            n=0
            if value != None:
                for m in value:
                    n += ord(m)
                result = n%self.size
                return result
            else:
                return None
        return value % self.size
    
    def rehash(self, value):
        return (value+1)%self.size
    
    def size(self):
        return len(self.key) #Keys are unique, good indicator for size
    
    def insert(self, key, val):
        hashvalue = self.hash(key) # Get hash value via refactoring

        #Check to see if slot is not occupied (best case)
        if self.keylist[hashvalue] == None:
            self.keylist[hashvalue] = key
            self.valuelist[hashvalue] = val

        else: # Over write value if hash returns same key
            if self.keylist[hashvalue] == key:
                self.valuelist[hashvalue] = val
            else:
                newhash = rehash(val) #Check the next slot contiously to rehash
                while self.keylist[newhash] != None and self.keylist[newhash] != key:
                    newhash = self.rehash(newhash)
                
                #Same procedure as before once new hash is claimed
                if self.keylist[newhash] == None:
                    self.keylist[newhash] = key
                    self.valuelist[newhash] = val 
                else:
                    self.valuelist[newhash] = val
    
    def get(self, key):
        initial = self.hash(key)
        value = None
        found = False
        slot = initial

        # Search algorithm
        while self.keylist[slot] != None and found == False:
            if self.keylist[slot] == key:
                found = True
                value = self.valuelist[slot]
            else:
                slot = self.rehash(slot)
                if slot == initial:
                    found = True 
        return value 

    def getItem(self, key):
        return self.get(key)
    
    def setItem(self, key, value):
        self.insert(key, value)

            

def main():
    hTable = HashTable(11)
    hTable.setItem(20, "A")
    hTable.setItem(21, "B")

    print(hTable.getItem(21))
    print(hTable.getItem(20))

if __name__ == '__main__':
    main()




        



    




    
    








