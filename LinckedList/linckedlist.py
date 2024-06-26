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

def printt(self):
        current = head
        while current is not None:
            print(current.data,end="-->")
            current = current.next
        print("None")

print(node4.next)

#adding new node at beginning 
head = node1
node5 = Node(50)
node5.next = head
head = node5

print(node5.data)
printt(Node)

#adding new node at the end
head = node1
current = node1
node6 = Node(60)
while current.next is not None:
    current = current.next
current.next = node6

print(node4.next.data)
printt(Node)

#adding node at specific position
node7 = Node(25)
current = node5
while current is not None and current.data != 20:
    current = current.next
node7.next = current.next
current.next = node7

print(node7.data)
printt(Node)

#deleting from beginning
if head is not None:
    head = head.next
printt(Node)

#deleting from end
current = head
while current.next.next is not None:
     current = current.next
current.next = None
printt(Node)

#deleting from specific position
current = head
while current.next.next.data != 30:
    current = current.next
current.next = current.next.next
printt(Node)