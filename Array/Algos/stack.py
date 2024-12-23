class Stack:
    def __init__(self):
        self.s = []
    def is_empty(self):
        return len(self.s)==0
    def push(self,data):
            self.s.append(data)
        