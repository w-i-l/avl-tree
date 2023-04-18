from avl import AVL
from node import Node


if __name__ == "__main__":
    tree = AVL()

    l = [Node() for _ in range(7)]
    for node in sorted(l, reverse=True):
        tree.insert(node)

    print(tree.is_balanced())   
    tree.display_tree()
    tree.display()

    # tree.insert(Node(18))
    # tree.display_tree()
    # tree.insert(Node(10))
    # tree.display_tree()
    # print(tree.is_balanced())   

    # print(tree.nodes)
    number = 0
    node = [n for n in tree.nodes if n.key == number][0]
    # tree.remove(tree.nodes[4])
    # print(tree.search(node))
    tree.remove(node)
    tree.display_tree()
    tree.display()
    print(tree.is_balanced())

    number = 1
    node = [n for n in tree.nodes if n.key == number][0]
    # tree.remove(tree.nodes[4])
    # print(tree.search(node))
    tree.remove(node)
    tree.display_tree()
    tree.display()
    # print(tree._smallest_element(tree.nodes[-1]))
    print(tree.is_balanced())
