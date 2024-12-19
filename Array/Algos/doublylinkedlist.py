class Node:
    def __init__(self,prev=None,item= None,next= None):
        self.prev = prev
        self.item = item
        self.next = next
class Dll:
    def __init__(self,start=None):
        self.start = start
    def is_empty(self):
        return self.start == None
    def insert_at_start(self,data):
        n = Node(None,data,self.start)
        if self.start == None:           #You can optimize that thing by 
            self.start = n               # if not self.isempty(): self.start.prev = n; self.start = n the last part is out of the if statement so that it should run either way even if if statement works or not
        else:                  
            self.start = n
            self.start.prev = n
    def insert_at_last(self,data,temp):
        temp = self.start
        if not self.is_empty():
            while temp.next is not None:
                temp = temp.next
        
        n = Node(temp,data,None)
        if temp == None:
            self.start = n
        else:
            temp.next = n
    def search(self,data):
        temp = self.start
        while temp.next is not None:
            if temp.item == data:
                return temp
            temp = temp.next
        return None
    def insert_after(self,temp,data):
        if temp is not None:
            n = Node(temp,data,temp.next)
            if temp.next != None:
                temp.next.prev = n
            temp.next = n
    def print_list(self):
       



    

        

    