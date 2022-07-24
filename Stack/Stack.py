def create_stack():
    stack = list()
    global top
    top = -1
    return stack, top

def is_empty(top):
    return top == -1

def push(stack, top, value):
    top += 1
    stack.append(value)
    return top

def pop(stack, top):
    top -= 1
    stack.pop()
    return top

def get_top(stack):
    if len(stack) == 0:
        raise Exception("EMPTY STACK.")    
    return stack[-1]
    

if __name__ == "__main__":
    stack, top = create_stack()
    print(get_top(stack))
    top = push(stack, top, 10)
    top = push(stack, top, 15)
    print(get_top(stack))
    top = pop(stack, top)
    print(stack, top)
