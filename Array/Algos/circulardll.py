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
        n = Node(None,data)
        if not self.is_empty():
            n.prev = self.start.prev
            n.next = self.start
            self.start.prev.next = n
            self.start.prev = n
        else:
            n.prev = n
            n.next = n
            self.start = n
    def search(self,data):
        temp = self.start
        if temp.item == data:
            return temp
        else:
            temp = temp.next
        if not self.is_empty():
            while temp.next != self.start:
                if temp.item == data:
                    return temp
                temp = temp.next
            return None
        else:
            return None
    def insert_after(self,temp,data):
        if temp is not None:
            if temp.next == self.start :
                n = Node(temp,data,self.start)
                if temp.item == data:
                    self.insert_at_last()
            elif self.start == data:







# driver code
mylist = Cdll()
mylist.insert_at_start(15)
mylist.insert_at_start(5)
