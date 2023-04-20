from avl import AVL
from node import Node
from random import random


if __name__ == "__main__":
    tree = AVL()

    nodes = [Node() for _ in range(15)]
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
    
    # print(tree.nodes)
    # print(tree.smallest_element(tree.nodes[5]))
    # print(tree.biggest_element(tree.nodes[-2]))
    # tree.display()

    # print(tree.get_node(4))

    print(tree.dfs(tree.root, []))
    # print(tree.numbers_in_range(tree.get_node(3), tree.get_node(14), []))
    # print(tree.dfs([]))
    
    # print(tree.closest_element(Node(32)))
