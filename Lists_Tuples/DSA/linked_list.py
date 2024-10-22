# Linked List Implementation: Create a linked list data structure using lists and tuples. Implement basic operations like insertion, deletion, and traversal.

class linkedList:
    def __init__(self):
        self.head = None
    
    def create_node(self, value):
        return (value, None)
    
    def insert_begining(self, value):
        new_node = self.create_node(value)
        new_node = (new_node[0], self.head)
        self.head = new_node
     
    
    def traverse(self):
        current = self.head
        while current is not None:
            print(current[0], end="->")
            current = current[1]
        print("None")

ll = linkedList()
ll.insert_begining(5)
ll.insert_begining(4)
ll.insert_begining(3)
ll.traverse()
