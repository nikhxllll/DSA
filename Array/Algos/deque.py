class Deque:
    def __init__(self):
        self.items = []
        self.front = 0
        self.rear = 0
        self.item_count = 0

    def is_empty(self):
        