# This Is the simple code for a general tree

class TreeNode:
    def __init__(self,data):
        self.data = data
        self.parent = None
        self.children = []

    def level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        spaces = "  " * self.level() * 3
        prefix = spaces + "|_ _ _" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

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
tree_root.print_tree()