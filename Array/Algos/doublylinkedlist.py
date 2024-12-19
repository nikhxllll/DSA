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
    def insert_at_last(self,data):
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
        while temp is not None:
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
        temp = self.start
        while temp is not None:
            print(temp.item)
            temp = temp.next
    def delete_first(self):
        if self.start is not None:
            self.start = self.start.next
            if self.start is not None:
                self.start.prev = None
    def delete_last(self):
        if self.start is not None:
            temp = self.start 
            while temp.next is not None:
                temp = temp.next
            temp.prev.next = None
        elif self.start.next == None:
            self.start = None
        elif self.start == None:
            pass   



mylist = Dll()

mylist.insert_at_start(20)
mylist.insert_at_start(10)
mylist.insert_at_last(30)
# mylist.search(30)
mylist.insert_after(mylist.search(30),40)
mylist.print_list()


    

        

    