class TreeNode:
    def __init__(self,value,left,right):
        self.data = value
        self.left = None
        self.right = None

class Tree:
    def create(self,data):
        return TreeNode(data)
    
    def insert(self,Node,data):
        if Node is None:
            return self.create(data)
        if data < Node.data:
            Node.left = self.insert(Node.left,data)
        else:
            Node.right = self.insert(Node.right,data)
        return Node