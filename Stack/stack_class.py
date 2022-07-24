
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class Stack:
    def __init__(self):
        self.top = -1
        self.head = Node("Head")
        
    def __str__(self) -> str:
        curr = self.head.next
        return_string = str()
        while curr:
            return_string += str(curr.value) + '->'
            curr = curr.next
        return return_string
        
    def is_empty(self):
        return self.top == -1
    
    def get_size(self):
        if self.top != -1:
            raise Exception("Stack is Empty.")
        return self.top+1
    
    def push(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.top += 1
        
    def pop(self):
        if self.is_empty():
            raise Exception("Stack is Empty.")
        remove = self.head.next.value
        self.head.next = self.head.next.next
        return remove
    
if __name__ == "__main__":
    stack = Stack()
    for value in range(1, 11):
        stack.push(value=value)
    print("stack: {}".format(stack))
    
    for _ in range(1,6):
        remove = stack.pop()
        print("removed value: {}".format(remove))
        
    print("stack: {}".format(stack))
    
