class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
class BST:
    
    def __init__(self) -> None:
        self.head = None
        
    def insert(self, data):
        if self.head == None:
            self.head = Node(data)
            return
        curr = self.head
        while curr:
            if curr.data > data:
                if curr.left:
                    curr = curr.left
                else:
                    curr.left = Node(data)
                    return
            elif curr.data < data:
                if curr.right:
                    curr = curr.right
                else:
                    curr.right = Node(data)
                    return
                
    def minValueNode(self):
        current = self.head
        while(current.left is not None):
            current = current.left

        return current
                
    def deleteNode(self, root, key):
        if root is None:
            return root
        if key < root.data:
            root.left = self.deleteNode(root.left, key)
        elif(key > root.data):
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp

            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self.head
            while(temp.left is not None):
                temp = temp.left

            root.data = temp.data
            root.right = self.deleteNode(root.right, temp.data)

        return root
                             
    def inorder(self, curr):
        
        if curr is not None:
            self.inorder(curr.left)
            print(str(curr.data) + "->", end=' ')
            self.inorder(curr.right)
            
    def display(self):
        self.inorder(self.head)
            
if __name__ == '__main__':
    tree = BST()
    tree.insert(5)
    tree.insert(3)
    tree.insert(1)
    tree.insert(7)
    tree.insert(9)
    tree.deleteNode(tree.head, 5)
    tree.display()
