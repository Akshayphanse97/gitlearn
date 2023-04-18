class Stack:

    def __init__(self) -> None:
        self.element=[]
        
    def push(self,data):
        self.element.append(data)
    
    def Pop(self):
        self.element.pop()
    
    def peek(self):
        return self.element[-1]
        
    def is_empty(self):
        return len(self.element)==0

    def display(self):
        return self.element


stack=Stack()

stack.push(1)
stack.push(2)
stack.push(3)
print(stack.display())
print(stack.peek())
stack.Pop()
print(stack.peek())

print(stack.is_empty())
