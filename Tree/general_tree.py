# This Is the simple code for a general tree

class TreeNode:
    def __init__(self,data):
        self.data = data
        self.parent = None
        self.children = []

    def print_tree(self, level=0):
        indent = '    ' * level
        print(indent + self.data)
        if self.children:
            for child in self.children:
                child.print_tree(level + 1)

    def add_child(self,child):
        child.parent = self
        self.children.append(child)

    
def build_tree():
    root = TreeNode("Electronics")

    Laptop = TreeNode("Laptop")
    Laptop.add_child(TreeNode("vivobook"))
    Laptop.add_child(TreeNode("victus"))
    Laptop.add_child(TreeNode("ROG TUF"))
    root.add_child(Laptop)
    return root

tree_root = build_tree()

laptop_node = tree_root.children[0]  # Assuming Laptop is the first child
laptop_node.print_tree()