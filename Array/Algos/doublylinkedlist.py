class Node:
    def __init__(self,prev=None,item= None,next= None):
        self.prev = prev
        self.item = item
        self.next = next
class Dll:
    def __init__(self,start=None):
        self.start = start
    def is_empty(self):
        return self.start == None
    def insert_at_start(self,data):
        n = Node(prev=None,data,self.start)
        if self.start == None:
    

        

    