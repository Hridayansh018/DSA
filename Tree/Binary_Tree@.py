class TreeNode:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None
        self.insert_data = []

    def create(self, data):
        return TreeNode(data)
    
    def insert(self, Node, data):
        if Node is None:
            return self.create(data)
        if data < Node.data:
            Node.left = self.insert(Node.left, data)
        else:
            Node.right = self.insert(Node.right, data)
        return Node
    
    def insert_with_increment(self, data):
        self.insert_data.append(data)

    def create_tree(self):
        if not self.insert_data:
            print("No data to create tree......!")
            return
        self.root = self.create(self.insert_data[0])
        for i in range(1, len(self.insert_data)):
            self.insert(self.root, self.insert_data[i])

    def print_inorder(self, Node):
        if Node:
            self.print_inorder(Node.left)
            print(Node.data, end=" ")
            self.print_inorder(Node.right)

if __name__ == "__main__":
    tree = Tree()
    print("Enter data for the tree (type 'done' when finished):")
    while True:
        data = input("Enter data (or 'done'): ")
        if data.lower() == 'done':
            break
        try:
            tree.insert_with_increment(int(data) + 1)  # Increment data value by 1
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue
    tree.create_tree()
    print("Inorder traversal of the created tree:")
    tree.print_inorder(tree.root)
