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
        temp = self.start
        if not self.start and self.start.priority > priority:

