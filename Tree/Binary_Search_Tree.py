#Binary Search Tree

class BSTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return #Node already exist
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BSTree(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BSTree(data)

    def search(self, val):
        if self.left == val:
            return True
        
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
            
        if val > self.data:
            if self.left:
                return self.right.search(val)
            else:
                return False
    
            
def build_tree(elements):
    if not elements:
        return    
    root = BSTree(elements[0])
    for element in elements[1:]:
        root.add_child(element)
    return root


if __name__=="__main__":
    elm = [17, 4, 1, 20, 9, 23, 18, 34]
    elmTree = build_tree(elm)

    countries = ["India","Pakistan","Germany", "USA","China","India","UK","USA"]
    country_tree = build_tree(countries)

    print("UK is in the list? :- ", country_tree.search("UK"))
    print("Sweden is in the list? :- ", country_tree.search("Sweden"))


