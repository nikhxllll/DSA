class Node:
    def __init__(self,item = None,next = None):
        self.item = item
        self.next = next

class Sll:
    def __init__(self,start):
        self.start = start
    def is_empty(self):
        return self.start == None
    def insert_at_start(self,data):
        n = Node(data,self.start)
        self.start = n
    def insert_at_last(self,data):
        n = Node(data)
        if self.is_empty():
            self.start = n
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next    
            temp.next = n
    def search(self,data):
        temp = self.start
        while temp.next is not None:
            
            temp = temp.next

