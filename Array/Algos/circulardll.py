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
        
