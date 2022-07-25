from numpy import dsplit


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
    
    def __repr__(self) -> str:
        curr = self.head
        return_string = str()
        while curr:
            return_string += str(curr.data) + ' -> '
            curr = curr.next
        return return_string
           
    def insert(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        
        # iterate till end of linkedlist
        curr = self.head
        while curr.next != None:
            curr = curr.next
        curr.next = Node(data)
        
    def search(self, data):
        no_of_iteration = 0
        if self.head is None:
            print("Linked List is empty!")
            return no_of_iteration 
        curr = self.head
        while curr:
            no_of_iteration += 1
            if curr.data == data:
                return no_of_iteration
            curr = curr.next
        
        print("Element Not Found")
        return no_of_iteration
        
    def delete(self, data):
        if self.head is None:
            raise Exception('Linked List is empty!')
        
        curr = self.head
        
        # delete for starting node
        if curr.data == data:
            self.head = curr.next
            return
        
        while curr.next.data != data:
            curr = curr.next
        curr.next = curr.next.next
    
        
if __name__ == '__main__':
    obj = LinkedList()
    for i in range(0,11):
        obj.insert(i)
        
    obj.delete(7)
    obj.delete(0)
    obj.delete(10)
    print('No of iteration: ' + str(obj.search(9)))
    print(obj)
    
    