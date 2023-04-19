from avl import AVL
from node import Node
from random import random


if __name__ == "__main__":
    tree = AVL()

    nodes = [Node(int(random() * 100)) for _ in range(15)]
    for node in sorted(nodes, reverse=True):
        tree.insert(node)
        print(f"Inserted {node}, balanced: {tree.is_balanced()}")

    print(tree.is_balanced())   
    tree.display_tree()

    # for number in range(14, -1, -1):
    #     node = [n for n in tree.nodes if n.key == number][0]
    #     tree.remove(node)
    #     tree.display_tree()
    #     print(f"Deleted {node}, balanced: {tree.is_balanced()}")
    
    print(tree.nodes)
    print(tree.smallest_element(tree.nodes[5]))
    print(tree.biggest_element(tree.nodes[-2]))
