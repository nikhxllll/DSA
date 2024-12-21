class Node:
    def __init__(self,prev = None,item= None,next = None):
        self.prev = prev
        self.item = item 
        self.next = next
class Cdll:
    def __init__(self,start = None):
        self.start = start
    def is_empty(self):
        return self.start == None
    def insert_at_start(self,data):
        n = Node(None,data)
        if not self.is_empty():
            n.next = self.start
            n.prev = self.start.prev
            self.start.prev.next = n
            self.start.prev = n
        else:
            n.next = n
            n.prev = n
        self.start = n
    def insert_at_last(self,data):
        if not self.is_empty():
            n = Node()

# driver code
mylist = Cdll()
mylist.insert_at_start(15)
mylist.insert_at_start(5)
