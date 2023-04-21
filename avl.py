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
        
        # sort by the deeper node
        result = sorted(result, key=lambda x: -x._get_height())

        for node in result:
            self.balance(node, node.left)
            if self.is_balanced() != True:
                self.balance(node, node.right)


    # reorder the tree from the inserted node
    def balance(self, parent:Node, curent:Node, node:Node = None):


        if curent != None and parent.get_balance() > 1:

            # left-left
            if curent.get_balance() >= 1:
                self._left_left(parent)
            
            #left-right
            elif curent.get_balance() <= -1:
                self._left_right(parent)

        elif curent != None and parent.get_balance() < -1:

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
        
        a.left = b.right

        if b.right:
            b.right.parent = a

        b.right = a

        # remember the parent
        b.parent = a.parent
        # update parent
        a.parent = b

        # we link the subgraph to its main graph
        if b.parent:
            if b.parent.left == a:
                b.parent.left = b
            elif b.parent.right == a:
                b.parent.right = b
    
    
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
            if c.parent.left == a:
                c.parent.left = c
            elif c.parent.right == a:
                c.parent.right = c

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
        
        a.right = b.left

        if b.left:
            b.left.parent = a

        b.left = a
        
        # remember the parent
        b.parent = a.parent
        # update parent
        a.parent = b

        # we link the subgraph to its main graph
        if b.parent:
            if b.parent.right == a:
                b.parent.right = b
            elif b.parent.left == a:
                b.parent.left = b
        

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
            if c.parent.left == a:
                c.parent.left = c
            elif c.parent.right == a:
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

        if len(self.nodes) == 0:
            return

        print()
        
        nodes = [self.root]

        index = ceil(log2(len(self.nodes))) - 1
        last = 2**(index + 1)

        print(str(self.root).rjust(last))
        # alignment = len(str(self.nodes[3]))

        while index >= 0:
            copy = []
            for node in nodes:
                if node:
                    copy.append(node.left)
                    copy.append(node.right)
                else:
                    copy.append(None)
                    copy.append(None)

            nodes = copy

            if set(nodes) != {None}:
                
                default = 2**(index)

                if nodes[0] != None:
                    print(str(nodes[0]).rjust(default), end = ' ' * (last - len(str(nodes[0]))))
                else:
                    print('. '.rjust(default), end = ' ' * (last - 1))

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
        
        print()
        print()
    

    # returns True if the node is in tree
    def search(self, node:Node):

        curent = self.root

        while curent != None:

            if curent == node:
                return True

            if node < curent:
                curent = curent.left
            else:
                curent = curent.right 

        return False
    
    
    # returns the smallest number from tree
    def smallest_element(self):
        
        curent = self.root

        while True:

            if curent.left != None:
                curent = curent.left
            else:
                return curent


    # returns the biggest number from tree
    def biggest_element(self):
        
        curent = self.root

        while True:

            if curent.right != None:
                curent = curent.right
            else:
                return curent


    def biggest_element_smaller_than(self, node:Node):
        
        curent = self.root

        while curent and curent != node:
            
            # right subtree
            if curent < node:
                
                # check if the next move is imposible
                if curent.right == None:
                    
                    # check if the curent value is not ok
                    if curent > node:

                        # we search for the good value
                        while curent > node:
                            curent = curent.parent
                    break
                
                # we iterate to the next node
                curent = curent.right
            
            # left subtree
            else:

                # check if the next move is imposible
                if curent.left == None:

                    # check if the curent value is not ok
                    if curent > node:

                        # we search for the good value
                        while curent > node:
                            curent = curent.parent
                        break
                # we iterate to the next node
                curent = curent.left
        
        return curent
    

    def smallest_element_bigger_than(self, node:Node):
        
        curent = self.root

        while curent and curent != node:
            
            # right subtre
            if curent < node:
                
                # check if the next move is imposible
                if curent.right == None:

                    # we search for the good value
                    while curent < node:
                        curent = curent.parent
                    break

                # we iterate to the next node
                curent = curent.right
            
            # left subtree
            else:

                # check if the next move is imposible
                if curent.left == None:

                    # we search for the good value
                    while curent < node:
                        curent = curent.parent
                    break

                # we iterate to the next node
                curent = curent.left
        
        return curent


    def remove(self, node:Node):
        
        # the node is not in tree
        if self.search(node) == False:
            raise ValueError("Node was not found")
        
        # leaf node
        if node.left == None and node.right == None and node.parent != None:
            
            # it's on the right side
            if node.parent.right == node:
                node.parent.right = None

                # we balance back
                if node.parent.get_balance() not in [-1, 0, 1]:
                    if node.parent.right:
                        self._left_right(node.parent)
                    elif node.parent.left:
                        self._left_left(node.parent)

            # it's on the left side
            elif node.parent.left == node:
                node.parent.left = None

                # we balance back
                if node.parent.get_balance() not in [-1, 0, 1]:
                    if node.parent.right:
                        self._right_right(node.parent)
                    elif node.parent.left:
                        self._right_left(node.parent)


        # only right or left subtree
        elif node.right == None or node.left == None:
            
            # root node case
            if node == self.root:
                if node.right != None:
                    self.root = node.right
                    node.right.parent = None
                elif node.left != None:
                    self.root = node.left
                    node.left.parent = None

            # it's on the right side
            elif node.parent.right == node:
                # right subtree
                if node.right != None:
                    node.right.parent = node.parent
                    node.parent.right = node.right

                #left subtree
                elif node.left != None:
                    node.left.parent = node.parent
                    node.parent.right = node.left
            
            # it's on the left side
            elif node.parent.left == node:
                # right subtree
                if node.right != None:
                    node.right.parent = node.parent
                    node.parent.left = node.right

                #left subtree
                elif node.left != None:
                    node.left.parent = node.parent
                    node.parent.left = node.left
        
        
        # both subtrees
        elif node.right != None and node.left != None:
            
            # get the smallest node from the right side
            smallest = self.smallest_element(node.right)

            node.key = smallest.key

            self.remove(smallest)

        
        self._final_balance()
        self.nodes.remove(node)


    def get_node(self, key:int):
        
        curent = self.root

        while curent != None:

            if curent.key == key:
                return curent

            if key < curent.key:
                curent = curent.left
            else:
                curent = curent.right 

        return None


    def dfs(self, from_node:Node = None, nodes = []):
        
        curent_node = self.root

        if from_node != None:
            curent_node = from_node
        

        for node in [curent_node.left, curent_node.right]:

            if curent_node not in nodes :
                nodes.append(curent_node)


            if node and node not in nodes:
                self.dfs(node, nodes)

        return nodes