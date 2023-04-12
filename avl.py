from node import Node
from math import log2, ceil

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

            parent:Node = None
            curent:Node = self.root

            while True:

                if node >= curent:
                    if curent.right == None:

                        curent.right = node
                        node.parent = curent if curent != node else None

                        if parent != None:
                            self.balance(parent, curent, node)

                        self._final_balance()
                        return
                    
                    curent = curent.right

                else:
                    if curent.left == None:
            
                        curent.left = node
                        node.parent = curent if curent != node else None

                        
                        if parent != None:
                            self.balance(parent, curent, node)
                        
                        self._final_balance()
                        return
                    
                    curent = curent.left
                
                parent = curent.parent
        

    # we check to see if they are
    # any unbalanced nodes at final
    def _final_balance(self):
        
        result = self.is_balanced()

        if result == True and isinstance(result, bool):
            return
        
        for node in result:
            self.balance(node, node.left)
            self.balance(node, node.right)


    # reorder the tree from the inserted node
    def balance(self, parent:Node, curent:Node, node:Node = None):


        if parent.get_balance() > 1:

            # left-left
            if curent.get_balance() >= 1:
                self._left_left(parent)
            
            #left-right
            elif curent.get_balance() <= -1:
                self._left_right(parent)

        elif parent.get_balance() < -1:

            # right-left
            if curent.get_balance() >= 1:
                self._right_left(parent)
            #right-right
            elif curent.get_balance() <= -1:
                self._right_right(parent)

    

    # returns True if yes
    # or a list with all unbalanced nodes
    def is_balanced(self):

        unbalanced = []

        for node in self.nodes:
            if node.get_balance() not in [-1, 0, 1]:
                unbalanced.append(node)

        return True if len(unbalanced) == 0 else unbalanced


    # a is the anchor of rotation
    #      a
    #     /
    #    b
    #   /
    #  c
    def _left_left(self, a:Node):
        
        b = a.left

        if a == self.root:
            self.root = b
            self.root.parent = None
        
        a.left = b.right if b else None
        if b.right:
            b.right.parent = a

        b.right = a
        b.parent = a.parent

        a.parent = b

        # we link the subgraph to its main graph
        if b.parent:
            b.parent.left = b
    
    
    # a is the anchor of rotation
    #    a
    #   /
    #  b
    #   \
    #    c
    def _left_right(self, a:Node):
        
        b = a.left
        c = b.right

        b.right = c.left
        a.left = c.right

        # update parents
        if c.left:
            c.left.parent = b
        if c.right:
            c.right.parent = a
        
        c.left = b
        c.right = a

        # remember the parent
        c.parent = a.parent

        # update parents
        b.parent = c
        a.parent = c

        # we link the subgraph to its main graph
        if c.parent:
            c.parent.left = c

        if a == self.root:
            self.root = c
            self.root.parent = None



    # a is the anchor of rotation
    # a
    #  \
    #   b
    #    \
    #     c
    def _right_right(self, a:Node):
        
        b = a.right

        if a == self.root:
            self.root = b
            self.root.parent = None
        
        a.right = b.left if b else None

        if b.left:
            b.left.parent = a

        b.left = a
        # remember the parent
        b.parent = a.parent
        # update parent
        a.parent = b

        # we link the subgraph to its main graph
        if b.parent:
            b.parent.right = b


    # a is the anchor of rotation
    #    a
    #     \
    #      b
    #     /
    #    c
    def _right_left(self, a:Node):

        b = a.right
        c = b.left

        a.right = c.left
        b.left = c.right
        
        # update parents
        if c.left:
            c.left.parent = a
        if c.right:
            c.right.parent = b
        
        c.left = a
        c.right = b

        # remember the parent
        c.parent = a.parent

        # update parents
        a.parent = c
        b.parent = c

        # we link the subgraph to its main graph
        if c.parent:
            c.parent.right = c

        if a == self.root:
            self.root = c
            self.root.parent = None


    # prints the nodes based on the insertion order
    def display(self):
        print()

        just = 4

        for node in self.nodes:
            print(f"{str(node).ljust(just//2)} - left: {str(node.left).ljust(just)} - right: {str(node.right).ljust(just)} - parent: {str(node.parent).ljust(just)} - balance: {str(node.get_balance()).ljust(just)}")

        print()

    
    def display_tree(self):
        
        nodes = [self.root]
        print(str(self.root).rjust(len(self.nodes) + 1))

        index = ceil(log2(len(self.nodes))) - 1
        last = 2**(index + 1)
        alignment = len(str(self.nodes[3]))

        while index != 0:
            copy = []
            for node in nodes:
                if node:
                    copy.append(node.left)
                    copy.append(node.right)

            nodes = copy

            if set(nodes) != {None}:
                
                # last = 2**(index)
                default = 2**(index)

                # if default != 0:
                #     print(" ", end= ' ')

                # if last == 2:
                #     last = 1

                print(str(nodes[0]).rjust(default), end = ' ' * (last - len(str(nodes[0]))))

                for i, node in enumerate(nodes[1:]):
                    if node:
                        print(str(node), end = ' ' *  max((last - len(str(node))), 1))
                    else:
                        print(".", end = ' ' * max((last-1), 2))
                print()

                last = default
            else:
                break
            
            index -= 1

        copy = []
        for node in nodes:
            if node:
                copy.append(node.left)
                copy.append(node.right)

                print(node.left if node.left else '-', node.right if node.right else '-', end= ' ')
            else:
                print('- -', end = ' ')
