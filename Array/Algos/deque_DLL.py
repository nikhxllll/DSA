class Node:
    def __init__(self,prev = None,item = None,next = None):
        self.prev = prev
        self.item = item
        self.next = next
class Deque:
    def __init__(self):
        self.front = 0
        self.rear = 0
        self.item_count = 0
    def is_empty(self):
        return self.item_count==0
    def insert_front(self,data):
        n = Node(None,data,self.front)
        if self.is_empty():
            self.front = n
            self.rear = n
        else:
            self.front.prev = n
            self.front = n
        self.item_count +=1
    def insert_rear(self,data):
        n = Node(self.rear,data,None)
        if self.is_empty():
            self.front = n
            self.rear = n
        else:
            self.rear.next = n
            self.rear = n
        self.item_count +=1
    def delete_front(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        elif self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
            self.front.prev = None
        self.item_count -=1 
    def delete_rear(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        elif self.rear == self.front:
            self.rear = None
            self.front = None
        else:
            self.rear=self.rear.prev
            self.rear.next = None  
        self.item_count -=1
    def get_front(self):
        return self.front.item
    def get_rear(self):
        return self.rear.item
    def size(self):
        return self.item_count
# Driver code
d1 = Deque()
d1.insert_front(30)
d1.insert_front(20)
d1.insert_front(10)
d1.insert_rear(40)
# d1.delete_front()
# d1.delete_rear()
print("TotalSize:",d1.size())
print("Top elem:",d1.get_front())
print("Bottom elem:",d1.get_rear())

    


