class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if len(self.items) != 0:
            return self.items.pop(0)
        else:
            print("Fila vazia")

    def show_Queue(self):
        return self.items


queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.show_Queue())

queue.dequeue()
print(queue.show_Queue())

queue.dequeue()
print(queue.show_Queue())

queue.dequeue()
print(queue.show_Queue())

queue.dequeue()
