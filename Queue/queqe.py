class Queue:
    __queueList = list()
    def __init__(self):
        self.queueList = list()
        self.top = -1
        self.rear = -1
        
    def __str__(self) -> str:
        return_string = 'TOP -> '
        curr = self.top
        if curr == -1:
            return "Sorry, your Queue is empty"
        while curr != -1:
            return_string += str(self.queueList[curr]) + ' -> '
            curr -= 1
        return_string += 'REAR'
        return return_string
        
    def is_empty(self):
        return self.top == -1
    
    def get_size(self):
        if self.top == -1:
            raise Exception("Empty Queue.")
        return self.top+1

    def enqueue(self, value):
        if self.top == -1:
            self.queueList.append(value)
            self.top += 1
            self.rear += 1
            return
        self.queueList.append(value)
        self.top += 1
        
    def dequeue(self):
        if self.top == -1:
            raise Exception("Empty Queue")
        self.queueList.pop(0)
        self.top -= 1
        
if __name__ == '__main__':
    queue = Queue()
    print(queue)
    for i in range(1, 11):
        queue.enqueue(i)
    
    print(queue.queueList)
    print(queue)
    queue.dequeue()
    print(queue)