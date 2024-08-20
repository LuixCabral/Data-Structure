from collections import deque

class Stack():
    def __init__(self):
        self.items = deque([])

    def Add_to_Stack(self,item):
        self.items.append(item)
        return True
    
    def Remove_from_Stack(self):
        if len(self.items)==0:
            return False
        else:
            self.items.pop()
            return True
        
    def Show_Stack(self):
        return self.items


x  = Stack()

x.Add_to_Stack(1)
x.Add_to_Stack(2)
x.Add_to_Stack(3)
x.Add_to_Stack(4)
 
print(x.Show_Stack())#[1,2,3,4]

x.Remove_from_Stack()
x.Remove_from_Stack()

print(x.Show_Stack())#[1,2]
        
