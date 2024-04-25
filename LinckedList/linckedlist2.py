class Node:
    def __init__(self,data = None, next = None):
        self.data = data
        self.next = next

class linckedlist:
    def __init__(self):
        self.head = None

    #Print updated lincked list
    def printt(self):
        current = self.head
        while current is not None:
            print(current.data,end="-->")
            current = current.next
        print(None)

    #Add node at beggining
    def insertB(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    #insert at the end
    def insertL(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while  current.next is not None:
            current = current.next
        current.next = new_node

ll = linckedlist()

node1 = Node(20)
node2 = Node(30)
node3 = Node(40)
node4 = Node(50)
node5 = Node(60)
node6 = Node(70)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
#Setting the head 
ll.head = node1