from node import Node

class AVL:

    def __init__(self):
        self.nodes = []
        self.root = None
        
    def insert(self, node:Node):

        if node in self.nodes:
            return
        
        self.nodes.append(node)

        if self.root == None:
            self.root = node
        
        else:

            curent:Node = self.root

            while True:

                if node >= curent:
                    if curent.right == None:
                        curent.right = node
                        return
                    
                    curent = curent.right

                else:
                    if curent.left == None:
                        curent.left = node
                        return
                    
                    curent = curent.left
    
    def is_balanced(self):
        for node in self.nodes:
            if node.get_balance() not in [-1, 0, 1]:
                return False

        return True


    # node is the anchor of rotation
    def left_left(self, node:Node):
        
        left_child = node.left
        if node == self.root:
            self.root = left_child
        
        node.left = left_child.right if left_child else None

        left_child.right = node
    
    
    # node is the anchor of rotation
    def left_right(self, a:Node):
        
        b = a.left
        c = b.right

        b.right = c.left
        a.left = c.right

        c.left = b
        c.right = a


        if a == self.root:
            self.root = c



    def display(self):
        for node in self.nodes:
            print(node, "- left:", node.left, '- right:', node.right)


tree = AVL()

tree.insert(Node(5))
tree.insert(Node(3))
tree.insert(Node(4))
# tree.insert(Node(2))
# tree.insert(Node(1))

# tree.insert(Node(3))

tree.display()
print(tree.is_balanced())   

tree.left_right(tree.nodes[0])
tree.display()
print(tree.is_balanced())   

