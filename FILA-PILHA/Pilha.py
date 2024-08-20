class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if len(self.items) != 0:
            return self.items.pop()
        else:
            print("Stack vazia")

    def show_stack(self):
        return self.items



stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

print(stack.show_stack())

stack.pop()
print(stack.show_stack())

stack.pop()
print(stack.show_stack())

stack.pop()
