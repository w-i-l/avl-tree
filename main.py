from avl import AVL


if __name__ == "__main__":
    tree = AVL()

    l = [Node() for _ in range(7)]

    for node in sorted(l, reverse=True):
        tree.insert(node)

    tree.display()
    print(tree.is_balanced())   