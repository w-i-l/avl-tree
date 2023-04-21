class Node:

    index = 0

    def __init__(self, key=0, left=None, right=None):
        self.key = Node.index if key == 0 else key
        Node.index += 1
        self.left = left
        self.right = right
        self.parent = None

    
    def _get_height(self, count=0):
        
        if self.right == None and self.left == None:
            return count

        left = 0
        right = 0

        if self.left != None:
            left = self.left._get_height(count+1)
        
        if self.right != None:
            right = self.right._get_height(count+1)

        return max(left, right)
            

    def get_balance(self):
        
        if self.right == None and self.left == None:
            return 0
        
        left = -1
        right = -1

        if self.left != None:
            left = self.left._get_height()
        
        if self.right != None:
            right = self.right._get_height()

        return left - right

    
    def __str__(self):
        return str(self.key)
    

    def __repr__(self):
        return str(self.key)
    
    def __sub__(self, other):
        if isinstance(other, Node):
            return self.key - other.key
    
    def __ge__(self, other):
        if isinstance(other, Node):
            return self.key >= other.key
    
    def __gt__(self, other):
        if isinstance(other, Node):
            return self.key > other.key
        
    def __lt__(self, other):
        if isinstance(other, Node):
            return self.key < other.key
        
    def __le__(self, other):
        if isinstance(other, Node):
            return self.key <= other.key

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.key == other.key
        
    def __hash__(self):
        return hash(self.key)