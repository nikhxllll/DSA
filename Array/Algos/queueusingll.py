class Node:
    def __init__(self,item = None,next = None):
        self.item = None
        self.next = None
class Queue:
    def __init__(self):
        self.start = None
        self.item_count= 0
    def is_empty(self):
        return self.start == None
    def enqueue(self,data):
        n = Node(data,self.start)
        self.start = n
        self.item_count +=1
    def dequeue(self):
        if not self.is_empty():
            temp = self.start
            while temp.next.next != None:
                temp = temp.next
            temp.next = None
            self.item_count -= 1 
    def front(self):
        pass
    def rear(self):
        return self.start.item
    def size(self):
        return self.item_count()


