class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = new_node

    def remove(self, data):
        current = self.head
        previous = None
        while current and current.data != data:
            previous = current
            current = current.next
        if not current:
            return False  
        if not previous:
            self.head = current.next 
        else:
            previous.next = current.next
        return True

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(elements)



linked_list = LinkedList()
linked_list.add(1)
linked_list.add(2)
linked_list.add(3)
linked_list.display()  # Saída: [1, 2, 3]
    
linked_list.remove(2)
linked_list.display()  # Saída: [1, 3]

linked_list.remove(1)
linked_list.display()  # Saída: [3]
    
linked_list.remove(3)
linked_list.display()  # Saída: []
