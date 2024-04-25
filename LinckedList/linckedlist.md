
---

## Implementation of a Linked List in Python

This Python code creates a linked list data structure and performs various operations such as insertion, deletion, and traversal.

### `Node` Class

The `Node` class represents individual nodes in the linked list. Each node contains a `data` attribute to store the data and a `next` attribute to point to the next node in the list.

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

### Creating Nodes and Connecting Them

```python
# Creating Nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

# Connecting Nodes
node1.next = node2
node2.next = node3
node3.next = node4
```

This section creates individual nodes with respective data values and connects them to form a linked list.

### Printing the Linked List

```python
def printt(self):
    current = head
    while current is not None:
        print(current.data, end="-->")
        current = current.next
    print("None")
```

The `printt` method is used to print the data of each node in the linked list, followed by `None`, indicating the end of the list.

### Insertion Operations

- **Insertion at Beginning**

```python
# Adding a new node at the beginning
head = node1
node5 = Node(50)
node5.next = head
head = node5
```

This code snippet adds a new node with data `50` at the beginning of the linked list.

- **Insertion at the End**

```python
# Adding a new node at the end
current = node1
node6 = Node(60)
while current.next is not None:
    current = current.next
current.next = node6
```

This code snippet adds a new node with data `60` at the end of the linked list.

- **Insertion at Specific Position**

```python
# Adding a node at a specific position
node7 = Node(25)
current = node5
while current is not None and current.data != 20:
    current = current.next
node7.next = current.next
current.next = node7
```

This code snippet adds a new node with data `25` after the node with data `20` in the linked list.

### Deletion Operations

- **Deletion from Beginning**

```python
# Deleting the first node from the beginning
if head is not None:
    head = head.next
```

This code snippet deletes the first node from the beginning of the linked list.

- **Deletion from End**

```python
# Deleting the last node from the end
current = head
while current.next.next is not None:
     current = current.next
current.next = None
```

This code snippet deletes the last node from the end of the linked list.

- **Deletion from Specific Position**

```python
# Deleting a node from a specific position
current = head
while current.next.next.data != 30:
    current = current.next
current.next = current.next.next
```

This code snippet deletes the node with data `30` from the linked list.

---

[code](https://github.com/Hridayansh018/DSA/blob/main/LinckedList/linckedlist.py)