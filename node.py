class Node:

    index = 0

    def __init__(self, key=0, left=None, right=None):
        self.key = Node.index if key == 0 else key
        Node.index += 1
        self.left = left
        self.right = right

    
    def _get_height(self, count=0):
        
        if self.right == None and self.left == None:
            return count

        left = 0
        right = 0

        if self.left != None:
            left = self.left.get_height(count+1)
        
        if self.right != None:
            right = self.right.get_height(count+1)

        return max(left, right)
            

    def get_balance(self):
        
        if self.right == None and self.left == None:
            return 0
        
        left = 0
        right = 0

        if self.left != None:
            left = self.left.get_height()
        
        if self.right != None:
            right = self.right.get_height()

        return left - right

    
    def __str__(self):
        return str(self.key)
    

    def __repr__(self):
        return str(self.key)

# n0 = Node(0)
# n1 = Node(1,n0)
# n2 = Node(2,n1)
# n3 = Node(3,n2)
# n4 = Node(4)
# n5 = Node(5,n3)
# n6 = Node(6)
# n7 = Node(7, n5, n4)
# n8 = Node(8, n7, n6)

# print(n4.get_balance())