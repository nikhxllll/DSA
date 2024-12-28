class Node:
    def __init__(self,item = None,left = None,right = None):
        self.item=item
        self.left = left
        self.right = right
class Bst:
    def __init__(self):
        self.root = None
    def insert(self,data):
        n = Node(data)
        
