class Queue:
    def __init__(self):
        self.items = []
        # self.front = None
        # self.rear = None
    def is_empty(self):
        return len(self.items)==0
    def enqueue(self,data):
        self.items.append(data)
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError('Stack is empty')
    def front(self):
        if not self.is_empty():
            return self.items[0]
    def rear(self):
        if not self.is_empty():
            return self.items[-1]
    def size(self):
        return len(self.items)
# Driver code
q1 = Queue()
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
print("Removed elem",q1.dequeue())
print("Front elem:",q1.front())
print("rear elem:",q1.rear())
