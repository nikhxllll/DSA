class Node:
    def __init__(self,item = None,next = None):
        self.item = item
        self.next = next
class Cll:
    def __init__(self,last = None):
        self.last = last

    def is_empty(self):
        return self.last == None
    def insert_at_start(self,data):
        n = Node(data)
        if self.is_empty():
            n.next = n
            self.last = n
        else:
            n.next = self.last.next
            self.last.next = n
    def insert_at_last(self,data):
        n = Node(data)
        if self.is_empty():
            n.next = n
            self.last = n
        else:
            n.next = self.last.next
            self.last.next = n
            self.last = n
    def search(self,data):
        if self.is_empty():
            return None
        temp = self.last
        while temp != self.last:
            if temp.item == data:
                return temp
            temp = temp.next
        if temp.next == data:
            return temp
        return None

    
