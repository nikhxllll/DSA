class Node:
    def __init__(self,item = None,next = None):
        self.item = item
        self.next = next
class Cll:
    def __init__(self,last = None):
        self.last = last

    def is_empty(self):
        return self.last == None
    def insert_at_start(self,data):
        n = Node(data)
        if self.is_empty():
            n.next = n
            self.last = n
        else:
            n.next = self.last.next
            self.last.next = n
    def insert_at_last(self,data):
        n = Node(data)
        if self.is_empty():
            n.next = n
            self.last = n
        else:
            n.next = self.last.next
            self.last.next = n
            self.last = n
    def search(self,data):
        if self.is_empty():
            return None
        temp = self.last.next
        while temp != self.last:
            if temp.item == data:
                return temp
            temp = temp.next
        if temp.next == data:
            return temp
        return None
    def insert_after(self,temp,data):
        if temp is not None:
            n = Node(data,temp.next)
            temp.next = n
            if temp == self.last:
                self.last = n
    def print_list(self):
        temp = self.last.next
        while temp != self.last:
            print(temp.item,end =' ')
            temp = temp.next
        if temp == self.last:
            print(temp.item)
    def delete_first(self):
        if self.is_empty():
            pass
        elif self.last.next == self.last:
            self.last = None
        else:
            self.last.next = self.last.next.next
                 
    


mylist = Cll()
mylist.insert_at_start(15)
mylist.insert_at_start(5)
mylist.insert_at_last(35)
mylist.insert_after(mylist.search(15),25)
# mylist.search(15)
mylist.print_list()