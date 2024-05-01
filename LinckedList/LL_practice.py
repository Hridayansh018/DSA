#linckedlist

class Node:
    def __init__(self,data = None, next = None):
        self.data = data
        self.next = next

class linckedlist:
    def __init__(self):
        self.head = None
        self.size = 0

    #Printing the updated linckedlist
    def prt(self):
        current = self.head
        while current is not None:
            print(current.data,end="--->")
            current = current.next
        print(None)

    def get_length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    #addition operators
    def insB(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1  # Increment size when adding a new node

    def insL(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.size += 1  # Increment size for the first node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node
        self.size += 1  # Increment size for the new node

    def insS(self, data,index):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")
        if index == 0:
            self.insB(data)
            return
        count = 0
        current = self.head
        while current:
            if count == index - 1:
                node = Node(data, current.next)
                current.next = node
                break
            current = current.next
            count += 1

    #deletion operators
    def delB(self):
        if self.head is None:
            return
        self.head = self.head.next
        self.size -= 1
    
    def delL(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            self.size = 0
            return
        current = self.head
        while current.next.next is not None:
            current = current.next
        current.next = None
        self.size -= 1
            
    def delS(self,index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")
        if index == 0:
            self.head = self.head.next
            self.size -=1
            return
        count = 0
        current = self.head
        while current:
            if count == index - 1:
                current.next = current.next.next
                self.size -= 1
                break
            current = current.next
            count += 1
        
        
#Creating Lincked list instance
ll = linckedlist()

#Creating nodes
node1 = Node(20)
node2 = Node(30)
node3 = Node(40)
node4 = Node(50)
node5 = Node(60)
node6 = Node(70)
node7 = Node(80)

#Adding nodes in a linckedlist
ll.head = node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7

ll.prt()

ll.insB(10)
ll.prt()

ll.insL(90)
ll.prt()

ll.insS(45, 4)
ll.prt()

ll.delB()
ll.prt()

ll.delL()
ll.prt()

ll.delS(3)
ll.prt()