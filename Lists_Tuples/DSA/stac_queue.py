class Stack:
    def __init__(self) -> None:
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items.pop()
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

class Queue:
    def __init__(self) -> None:
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items.pop(0)
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print(stack.pop())
print(stack.peek())

queue = Queue()
queue.enqueue(50)
queue.enqueue(60)
queue.enqueue(70)
queue.enqueue(80)
print(queue.dequeue())
print(queue.peek())