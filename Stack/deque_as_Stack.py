# Using deque as a Stack

from collections import deque
stack = deque()

for i in range(7):
    x = input("enter data:- ")
    stack.append(x)

print(stack)

# Using it as a class instance
class Stack:
    def __init__(self):
        self.container = deque()

    def push(self,data):
        self.container.append(data)

    def pop(self):
        return self.container.pop()

    def peek(self):
        if len(self.container) == 0:
            print("Stack is empty.")
            return None
        else:
            print(self.container[-1])
            return self.container[-1]
    
    def is_empty(self):
        return len(self.container)==0
    
    def size(self):   
        return len(self.container)
    
s = Stack()
s.is_empty()
s.push(5)
s.is_empty()
s.push("yooo")
s.push(12.4)
s.push("hemlo")
s.peek()
s.size()
s.pop()
s.size()

print("Data in the stack (top to bottom):")
while not s.is_empty():
    print(s.peek())
    s.pop()