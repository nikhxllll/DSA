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
    

        

