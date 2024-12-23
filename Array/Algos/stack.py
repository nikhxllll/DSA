class Stack:
    def __init__(self):
        self.s = []
    def is_empty(self):
        return len(self.s)==0
    def push(self,data):
            self.s.append(data)
    def pop(self):
        if not self.is_empty():
            return self.s.pop()
        else:
            raise IndexError('Stack is empty')
    def peek(self):
        if not self.is_empty():
            return self.s[-1]
        else:
            raise IndexError('Stack is empty')
    
              
    
    
        