from avl import AVL
from node import Node


if __name__ == "__main__":
    tree = AVL()

    l = [Node() for _ in range(7)]
    for node in sorted(l, reverse=True):
        tree.insert(node)

    print(tree.is_balanced())   
    tree.display_tree()

    # tree.insert(Node(18))
    # tree.display_tree()
    # tree.insert(Node(10))
    # tree.display_tree()
    # print(tree.is_balanced())   

    # print(tree.nodes)
    tree.remove(tree.nodes[1])
    tree.display_tree()
    tree.display()
