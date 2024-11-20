class Priority:
    def __init__(self):
        self.items = []
        self.item_count = 0
    def is_empty(self):   
        return self.item_count == 0
    def push(self,data):
        