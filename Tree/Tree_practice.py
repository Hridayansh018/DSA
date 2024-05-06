# Tree Data Structre Practice, creating tree with user input

class TreeNode:
    def __init__(self,data):
        self.data = data
        self.parent = None
        self.children = []

    def add_child(self,child):
        child.parent = self
        self.children.append(child)

    def level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level
    
    def printTree(self):
        spaces = "  "*self.level()*3
        prefix = spaces + "|_ _ _ _" if self.parent else " "
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.printTree()

def build_Tree():
    data = input("Enter the name of Tree:- ")
    root = TreeNode(data)
    print("Tree Initiated")
    running = True
    while running:
        bname = input("Enter Branch Name (or exit to finish):- ")
        if bname.lower() != "exit":
            bnode = TreeNode(bname)
            n = int(input("How many data u want:- "))
            for i in range(n):
                y = input(f"Enter data {i+1}:- ")
                bnode.add_child(TreeNode(y))
            root.add_child(bnode)
        else:
            running = False
            break
    root.printTree()
    return root

build_Tree()