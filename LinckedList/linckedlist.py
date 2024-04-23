class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

#CREATING NODES
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

#CONNECTING NODES
node1.next = node2
node2.next = node3
node3.next = node4
#LINCKED LIST IS READY

#adding new not at beggining 
head = node1
node5 = Node(50)
node5.next = head
head = node5
