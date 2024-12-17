class Node:
    def __init__(self,item = None,next = None):
        self.item = item
        self.next = next

class Sll:
    def __init__(self,start = None):
        self.start = start
    def is_empty(self):
        return self.start == None
    def insert_at_start(self,data):
        n = Node(data,self.start)
        self.start = n
    def insert_at_last(self, data):
        n = Node(data)
        if not self.is_empty():
             temp = self.start             #(its because we have to finf the last element in the node, so what we did we simply made temp variable)
             while temp.next is not None:  #(if in temp, the next variable value is not NONE, then we have to save the value of next in the temp)
                 temp=temp.next            #(After, this we have to save the value of next in the temp, upto the value of next must have to be zero)
             temp.next = n
        else:
            self.start = n
    def search(self,data):
        temp = self.start
        while temp.next is not None:
            if temp.item == data:
                return temp
            temp = temp.next
        return None
    def insert_after(self, temp, data):    #(we are passing node reference).       
        if temp is not None:
            n = Node(data, temp.next)
            temp.next = n
    def print_list(self):
        temp = self.start
        while temp is not None:
            print(temp.item)
            temp = temp.next
    def delete_first(self):
        if self.start == None:
            pass
        else:
            self.start = self.start.next
    def delete_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start = None
        else:
            temp = self.start
            while temp.next.next is not None:
                temp.next = None
    def delete_after(self,data):
        if self.start is None:
            pass
        elif self.start.next is None:
            if self.start.item == data:
                self.start = None
        else:
            temp = self.start
            while temp.next is not None:
                if temp.next.item == data:
                    temp.next = temp.next.next
                    break
                temp = temp.next

            


my_list = Sll()

my_list.insert_at_start(20)
my_list.insert_at_start(10)
my_list.insert_at_start(30)
my_list.insert_after(my_list.search(30),40)


my_list.print_list()