class Node:
    def __init__(self,item = None,left = None,right = None):
        self.item=item
        self.left = left
        self.right = right
class Bst:
    def __init__(self):
        self.root = None
    def insert(self,data):
        self.root = self.rinsert(self.root,data)
    def rinsert(self,root,data):
        if root == None:
            return Node(data)
        if data < root.item:
            root.left = self.rinsert(root.left,data)
        elif data > root.item:
            root.right = self.rinsert(root.right,data)
        return root
    def search(self,data):
        
