#Working with doubly lincked list 

class Node:
    def __init__(self,data = None, next = None, previous = None):
        self.data = data
        self.next = next
        self.previous = previous

class linckedlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def prt(self):
        if self.head is None:
            print("Linked list is empty.")
            return
        outF = ""
        currentF = self.head
        while currentF is not None:
            outF += f"{currentF.data}<===>"
            currentF = currentF.next
        outB = ""
        currentB = self.tail
        while currentB is not None:
            outB += f"{currentB.data}<===>"
            currentB = currentB.previous
        if self.head.previous is None:
            print(f"None<===>{outF}None")

    def connect(self, node1, node2):
        if node1 is None or node2 is None:
            return
        node1.next = node2
        node2.previous = node1
        if self.head is None:
            self.head = node1
        self.tail = node2

    def get_length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
    
    def insB(self,data):
        new_node = Node(data, next=self.head)
        if self.head is not None:
            self.head.previous = new_node
        self.head = new_node
        if self.tail is None:
            self.tail = new_node
        self.size += 1

    def insL(self,data):
        new_node = Node(data, previous=self.tail)
        if self.tail is not None:
            self.tail.next = new_node
        self.tail = new_node
        if self.head is None:
            self.head = new_node
        self.size += 1

    def insS(self,data,index):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")
        if index == 0:
            self.insB(data)
            return
        count = 0
        current = self.head
        while current:
            if count == index - 1:
                new_node = Node(data,current.next,current)
                current.next.previous = new_node
                current.next = new_node
                self.size += 1
                break
            current = current.next
            count += 1

    def delB(self):
            if self.head is None:
                return
            if self.head.next is None:
                self.head = None
                self.tail = None
                self.size = 0
                return
            self.head = self.head.next
            self.head.previous = None
            self.size -= 1
            
    def delL(self):
        if self.tail is None:
            return
        if self.tail.previous is None:
            self.head = None
            self.tail = None
            self.size = 0
            return
        self.tail = self.tail.previous
        self.tail.next = None
        self.size = 0

    def delS(self,index):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")
        if index == 0:
            self.delB()
            return
        if index == self.get_length() - 1:
            self.delL()
            return
        count = 0
        current = self.head
        while current:
            if count == index:
                current.previous.next = current.next
                current.next.previous = current.previous
                self.size -= 1
                break
            current = current.next
            count += 1
                            
ll = linckedlist()

node1 = Node(20)
node2 = Node(30)
node3 = Node(40)
node4 = Node(50)
node5 = Node(60)
node6 = Node(70)
node7 = Node(80)

ll.connect(node1, node2)
ll.connect(node2, node3)
ll.connect(node3, node4)
ll.connect(node4, node5)
ll.connect(node5, node6)
ll.connect(node6, node7)

ll.prt()

ll.insB(10)
ll.prt()

ll.insL(90)
ll.prt()

ll.insS(45,4)
ll.prt()

ll.delB()
ll.prt()

ll.delL()
ll.prt()

ll.delS(3)
ll.prt()