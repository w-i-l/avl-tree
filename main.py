from avl import AVL
from node import Node
from random import random


if __name__ == "__main__":
    
    tree = AVL()
    
    # 1. Insertion
    nodes = [Node(int(random() * 30)) for i in range(13)]
    for node in sorted(nodes, reverse=True):
        tree.insert(node)
        print(f"Inserted {node}, balanced: {tree.is_balanced()}")

    print(f'Tree balanced: {tree.is_balanced()}')   
    tree.display_tree()

    # 2. Remove
    # for number in range(14, -1, -1):
    #     node = [n for n in tree.nodes if n.key == number][0]
    #     tree.remove(node)
    #   # tree.display_tree()
    #     print(f"Deleted {node}, balanced: {tree.is_balanced()}")
    

    # 3. Search
    node = Node(15)
    print(f'Is {node} in tree: {tree.search(node)}')
    print()


    # 4. Biggest Y, Y <= X
    print(f'Biggest element smaller than {node} : {tree.biggest_element_smaller_than(node)}')
    print()


    # 5. Smallest Y, Y >= X
    print(f'Smallest element bigger than {node} : {tree.smallest_element_bigger_than(node)}')
    print()


    # 6. Numbers in range
    node1 = tree.nodes[-3]
    node2 = tree.nodes[2]

    if node1 > node2:
        node1, node2 = node2, node1

    print(f'Numbers in range {node1} to {node2} :\n{tree.get_numbers_in_range(tree.root, node1, node2)}')

