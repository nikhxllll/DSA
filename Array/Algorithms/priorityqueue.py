class PriorityyQueue:
    def __init__(self):
        self.items = []
        self.item_count = 0
    def is_empty(self):   
        return self.item_count == 0
    def push(self,data,priority):
        index = 0
        while index < len(self.items) and self.items[index][1]<= priority:
            index +=1
        self.items.insert(index,(data,priority))
        self.item_count +=1
    def pop(self):
        if not self.is_empty():
            self.item_count -=1
            return self.items.pop(0)[0]   
    def size(self):
        return self.item_count()
    # driver Code
p=PriorityyQueue()
p.push("Nikhil",10)
p.push("Saif",20)
p.push("Raja",30)
p.push("Rahul",30)

while not p.is_empty():
    print(p.pop())

