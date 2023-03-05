class Node:
    def __init__(self, value):
        self.value = value 
        self.prev = None 
        self.next = None 

class DoublyLinkedList:
    def __init__(self):
        self.head = None 
        self.tail = None 

    def __str__(self):
        return self.printNodesFromHeadToTail() + "\n" + self.printNodesFromTailToHead()
        
    
    def printNodesFromHeadToTail(self):
        currentNode = self.head 
        listOfNodes = []
        while currentNode is not None:
            listOfNodes.append(currentNode.value)
            currentNode = currentNode.next 

        stringifiedListOfNodes = map(str, listOfNodes) 
        print(" ---> ".join(stringifiedListOfNodes)) 
        return " ---> ".join(stringifiedListOfNodes)         

    def printNodesFromTailToHead(self):
        currentNode = self.tail 
        listOfNodes = []
        while currentNode is not None:
            listOfNodes.append(currentNode.value)
            currentNode = currentNode.prev 

        stringifiedListOfNodes = map(str, listOfNodes)
        print(" ---> ".join(stringifiedListOfNodes))
        return " ---> ".join(stringifiedListOfNodes)

    def setHead(self, node):
        self.head.prev = node 
        node.next = self.head 
        self.head = node        

    def setTail(self, node):
        self.tail.next = node 
        node.prev = self.tail 
        self.tail = node 
        
    def insertBefore(self, node, nodeToInsert):
        pass 

    def insertAfter(self, node, nodeToInsert):
        pass 

    def insertAtPosition(self, position, nodeToInsert):
        pass 

    def removeNodesWithValue(self, value):
        currentNode = self 
        while currentNode is not None:
            if currentNode.value == value:
                currentNode = removeNodeBindingsAndReturnNextNode(self, currentNode)
        
    def removeNodeBindingsAndReturnStandaloneNode(self, node):
        if node == self.head:
            self.head = self.head.next
        if node == self.tail:
            self.tail = self.tail.prev
        if node.prev is not None:
            node.prev.next = node.next 
        if node.next is not None:
            node.next.prev = node.prev 
        node.prev = None
        node.next = None 
        return node 

    def removeNodeBindingsAndReturnLinkedList(self, node):
        if node == self.head:
            self.head = self.head.next
        if node == self.tail:
            self.tail = self.tail.prev
        if node.prev is not None:
            node.prev.next = node.next 
        if node.next is not None:
            node.next.prev = node.prev 
        node.prev = None
        node.next = None 
        return self 
    
    def removeNodeBindingsAndReturnNextNode(self, node):
        if node.next is not None:
            nextNode = node.next
        if node == self.head:
            self.head = self.head.next
        if node == self.tail:
            self.tail = self.tail.prev
        if node.prev is not None:
            node.prev.next = node.next 
        if node.next is not None:
            node.next.prev = node.prev 
        node.prev = None
        node.next = None 
        return nextNode 

    def removeNodeBindingsAndReturnPrevNode(self, node):
        if node.prev is not None:
            prevNode = node.prev
        if node.next is not None:
            nextNode = node.next
        if node == self.head:
            self.head = self.head.next
        if node == self.tail:
            self.tail = self.tail.prev
        if node.prev is not None:
            node.prev.next = node.next 
        if node.next is not None:
            node.next.prev = node.prev 
        node.prev = None
        node.next = None 
        return prevNode 

    def containsNodeWithValue(self, value):
        currentNode = self.head 
        while currentNode is not None:
            if currentNode.value == value:
                return True 
            currentNode = currentNode.next

        return False
            


# DoublyLinkedList:   1 <---> 2 <---> 3 <---> 4 <---> 5 
nodeOne = Node(1)
nodeTwo = Node(2)
nodeThree = Node(3)
nodeFour = Node(4)
nodeFive = Node(5)

nodeThreeStandalone = Node(3)
nodeSevenStandalone = Node(7)
nodeSixStandalone = Node(6)
nodeZeroStandAlone = Node(0)

nodeOne.next = nodeTwo 
nodeTwo.prev = nodeOne 
nodeTwo.next = nodeThree
nodeThree.prev = nodeTwo 
nodeThree.next = nodeFour
nodeFour.prev = nodeThree 
nodeFour.next = nodeFive 
nodeFive.prev = nodeFour

# TRRRRRRRRRRRRRRRRRRRRRRRRRAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIIIIIIIIIIIIIIIIIIIIIIIIIIIIINNNNNNNNNNNNNNNNNNNNNNNNNNNNN
inputLinkedList = DoublyLinkedList()
inputLinkedList.head = nodeOne 
inputLinkedList.tail = nodeFive 

inputLinkedList.printNodesFromHeadToTail()
inputLinkedList.printNodesFromTailToHead()

inputLinkedList.setHead(nodeZeroStandAlone)
inputLinkedList.printNodesFromHeadToTail()
inputLinkedList.printNodesFromTailToHead()

inputLinkedList.setTail(nodeSixStandalone)
inputLinkedList.printNodesFromHeadToTail()
inputLinkedList.printNodesFromTailToHead()


standAloneNode = inputLinkedList.removeNodeBindingsAndReturnStandaloneNode(nodeTwo)
inputLinkedList.printNodesFromHeadToTail()
inputLinkedList.printNodesFromTailToHead()
print(standAloneNode.value, standAloneNode.prev, standAloneNode.next)

standAloneNodeNow = inputLinkedList.removeNodeBindingsAndReturnStandaloneNode(nodeZeroStandAlone)
inputLinkedList.printNodesFromHeadToTail()
inputLinkedList.printNodesFromTailToHead()
print(standAloneNodeNow.value, standAloneNodeNow.prev, standAloneNodeNow.next)

inputLinkedList.printNodesFromHeadToTail()
print(inputLinkedList.containsNodeWithValue(6))
print(inputLinkedList.containsNodeWithValue(2))

print(inputLinkedList)