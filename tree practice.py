class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def createNode(self, data):
        return Node(data)

    def insert(self, node, data):
        if node is None:
            return self.createNode(data)
        if data < node.data:
            node.left = self.insert(node.left, data)
        else:
            node.right = self.insert(node.right, data)
            print(node.right.data)
        return node


tree = Tree()
root = tree.createNode(5)
tree.insert(root, 2)
tree.insert(root, 10)
tree.insert(root, 7)



