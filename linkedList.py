class Node:
    def __init__(self, dataVal = None):
        self.dataVal = dataVal
        self.nextVal = None

class SLinkedList:
    def __init__(self):
        self.headVal = None
    
    def listPrint(self):
        # Traversing
        printVal = self.headVal
        while printVal is not None:
            print (printVal.dataVal)
            printVal = printVal.nextVal

    def AtBeginning(self, data):
        # Insertion at beginning
        newNode = Node(data)
        # update the new nodes next val to existing node
        newNode.nextVal = self.headVal
        self.headVal = newNode

    def AtEnd(self,data):
        newNode = Node(data)
        if(self.headVal is None):
            self.headVal = newNode
            return
        
        laste = self.headVal
        while(laste.nextVal):
            laste = laste.nextVal

        laste.nextVal = newNode

        

list1 = SLinkedList()
list1.headVal = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

# Link first Node to second node
list1.headVal.nextVal = e2
# link second Node to third node
e2.nextVal = e3

# insert at beginning
list1.AtBeginning("Sun")

# insert at End
list1.AtEnd('Thur')
# Traversing linked list
list1.listPrint()