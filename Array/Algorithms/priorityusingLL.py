class Node:
    def __init__(self,item = None,priority = None,next = None):
        self.item = item
        self.priority = priority
        self.next = next
class PriorityQueue:
    def __init__(self):
        self.start = None
        self.item_count = 0
    def push(self,data,priority):
        n = Node(data,priority)
        if not self.start or self.start.priority < priority:
            n.next = self.start
            self.start = n
        else:
            temp = self.start
            while temp.next != None and temp.next.priority <= priority:
                temp=temp.next
            n.next = temp.next
            temp.next = n
        self.item_count +=1
    def is_empty(self):
        return self.item_count == 0
    def pop(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        data = self.start.item
        self.start = self.start.next
        self.item_count -=1
        return data
    def size(self):
        return self.item_count
    
# driver code
q = PriorityQueue()
q.push("Ny",10)
q.push("Jy",20)
q.push("Sy",30)
q.push("Ky",40)

while not q.is_empty():
    print(q.pop())
    
        
            

        

