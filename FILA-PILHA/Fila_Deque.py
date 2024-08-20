from collections import deque

class Fila():
    def __init__(self) -> None:
        self.fila = deque([])

    def Add_Fila(self,item):
        self.fila.append(item)

    def Add_Head(self,item):
        self.fila.appendleft(item)

    def Remover_Fila(self):
        self.fila.popleft()

    def Show_Fila(self):
        return self.fila
    
queue = Fila()

xablau = [1,2,3,4,5]
for i in xablau:
    queue.Add_Fila(i)

print(queue.Show_Fila())

queue.Add_Head(32)

print(queue.Show_Fila())

queue.Remover_Fila()
queue.Remover_Fila()
queue.Remover_Fila()
queue.Remover_Fila()
queue.Remover_Fila()
print(queue.Show_Fila())

