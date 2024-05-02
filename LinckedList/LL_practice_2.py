class Node:
    def __init__(self,data = None, next = None, previous = None):
        self.data = data
        self.next = next
        self.previous = previous


class linckedlist:
    def __init__(self):
        self.head = None
        self.tail = None
    
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
        if node1.previous is None:
            print(f"None<===>{outF}{outB}None")


    def connect(self, node1, node2):
        if node1 is None or node2 is None:
            return
        node1.next = node2
        node2.previous = node1
        if self.head is None:
            self.head = node1
        self.tail = node2


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