class Heap:
    def __init__(self):
        self.heap = []
    def createHeap(self,list1):
        for l in list1:
            self.insert(l)
    def insert(self,n):
        

