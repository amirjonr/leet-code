class Tree:
    def __init__(self, root, children=None):
        self.root = root
        self.children = children if children is not None else []


def tree_to_dict(node):
    result = {'key': node.root}

    if node.children:
        result['children'] = [tree_to_dict(child) for child in node.children]

    return result


def print_tree(node, level=0):
    indent = "  " * level
    print(f"{indent}- {node['key']}")

    if 'children' in node:
        for child in node['children']:
            print_tree(child, level + 1)


tree = Tree(1)
tree.children.append(Tree(2))
tree.children.append(Tree(3))
tree.children.append(Tree(4))
tree.children.append(Tree(5))

tree.children[0].children.append(Tree(5))
tree.children[0].children.append(Tree(6))
tree.children[1].children.append(Tree(7))
tree.children[1].children.append(Tree(8))
tree.children[1].children.append(Tree(9))

tree_dict = tree_to_dict(tree)
print_tree(tree_dict)

# example of use:
# file systems
