from node import Node

class AVL:

    def __init__(self):
        self.nodes = []
        self.root = None
        
    def insert(self, node:Node):
        
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
    
    def display(self):
        for node in self.nodes:
            print(node, "- left:", node.left, '- right:', node.right)


tree = AVL()

tree.insert(Node(2))
tree.insert(Node(3))
tree.insert(Node(4))
tree.insert(Node(1))

tree.display()
