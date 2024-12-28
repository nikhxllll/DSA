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
        if self.root == None:
            self.root = n
        else:
            temp = self.root
            if temp.item > n.item:
                while temp.left!=None or temp.right != None:
                    self.root.left =  n  
            else:
                self.root.right = n
