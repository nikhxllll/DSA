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
        return self.rsearch(self.root,data)
    def rsearch(self,root,data):
        if root == None or root.item == data:
            return root
        if data < root.item:
            return self.rsearch(root.left,data)
        elif data > root.item:
            return self.rsearch(root.right,data)
    def in_order(self):
        result = []
        self.rinorder(self.root,result)
        return result
    def rinorder(self,root,result):
        if root:
            self.rinorder(root.left,result)
            result.append(root.item)
            self.rinorder(root.right,result)
    def preorder(self):
        result = []
        self.rpreorder(self.root,result)
        return result
    def rpreorder(self,root,result):
        if root:
            result.append(root.item)
            self.rpreorder(root.left,result)
            self.rpreorder(root.right,result)
    def postorder(self):
        result = []
        self.rpostorder(self.root,result)
        return result
    def rpostorder(self,root,result):
        if root:
            self.rpostorder(root.left,result)
            self.rpostorder(root.right,result)
            result.append(root.item)
    def minimum(self,root):
        while root.left is not None:
            root = root.left
        return root.item
    def maximum(self,root):
        while root.right is not None:
            root = root.right
        return root.item


# driver code
bst = Bst()
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(60)
bst.insert(10)
bst.insert(40)
bst.insert(30)
bst.insert(35)
bst.insert(45)
print(bst.search(45))
print(bst.in_order())
print(bst.preorder())
print(bst.postorder())
