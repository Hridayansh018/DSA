
---

## Linked List Implementation in Python

This Python code implements a linked list data structure with various functionalities such as insertion at the beginning, end, and at specific locations, as well as deletion from the beginning, end, and at specific locations.

### `Node` Class

The `Node` class represents individual nodes in the linked list. Each node contains a `data` attribute to store the data and a `next` attribute to point to the next node in the list.

```python
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
```

### `LinkedList` Class

The `LinkedList` class represents the linked list itself. It contains methods to perform various operations on the linked list.

#### Constructor

```python
def __init__(self):
    self.head = None
```

The constructor initializes an empty linked list with the `head` attribute set to `None`.

#### Printing the Linked List

```python
def printt(self):
    current = self.head
    while current is not None:
        print(current.data, end="-->")
        current = current.next
    print(None)
```

The `printt` method prints the data of each node in the linked list, followed by `None`, indicating the end of the list.

#### Insertion Operations

- **Insertion at Beginning**

```python
def insertB(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node
```

This method inserts a new node with the given data at the beginning of the linked list.

- **Insertion at End**

```python
def insertL(self, data):
    new_node = Node(data)
    if self.head is None:
        self.head = new_node
        return
    current = self.head
    while current.next is not None:
        current = current.next
    current.next = new_node
```

This method inserts a new node with the given data at the end of the linked list.

- **Insertion at Specific Location**

```python
def incertS(self, data):
    new_node = Node(data)
    if self.head is None or data <= self.head.data:
        new_node.next = self.head
        self.head = new_node
        return
    current = self.head
    while current.next is not None and current.next.data < data:
        current = current.next
    new_node.next = current.next
    current.next = new_node
```

This method inserts a new node with the given data at a specific location based on a condition.

#### Deletion Operations

- **Deletion from Beginning**

```python
def deleteB(self):
    if self.head is None:
        return
    self.head = self.head.next
```

This method deletes the first node from the beginning of the linked list.

- **Deletion from End**

```python
def deleteL(self):
    if self.head is None:
        return
    if self.head.next is None:
        self.head = None
        return
    Current = self.head
    while Current.next.next is not None:
        Current = Current.next
    Current.next = None
```

This method deletes the last node from the end of the linked list.

- **Deletion at Specific Location**

```python
def deleteS(self, data):
    if self.head is None:
        return
    if self.head.data == data:
        self.head = self.head.next
        return
    current = self.head
    while current.next is not None and current.next.data != data:
        current = current.next
    if current.next is not None:
        current.next = current.next.next
```

This method deletes a node with the given data from a specific location in the linked list.

### Usage Example

```python
# Creating Linked List Instance
ll = LinkedList()

# Setting the head and nodes
# (omitted for brevity)

# Perform operations such as insertion and deletion
# (omitted for brevity)
```

This code snippet demonstrates how to use the `LinkedList` class to create and manipulate a linked list.

---

[code](https://github.com/Hridayansh018/DSA/blob/main/LinckedList/linckedlist2.py)