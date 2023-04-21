from avl import AVL
from node import Node
from random import random


if __name__ == "__main__":
    tree = AVL()
    keys = [26, 25, 24, 23, 20, 19, 18, 11, 9, 7, 6, 4, 3]
    nodes = [Node(int(random() * 30)) for i in range(13)]
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

    # print(tree.dfs(tree.root, []))
    # print(tree.biggest_element())
    # print(tree.smallest_element())
    # print(tree.nodes)
    node = Node(int(random() * 30)) 
    print(node)
    print(tree.biggest_element_smaller_than(node))
    print(tree.smallest_element_bigger_than(node))
    # print(tree.numbers_in_range(tree.get_node(3), tree.get_node(14), []))
    # print(tree.dfs([]))
    
    # print(tree.closest_element(Node(32)))
