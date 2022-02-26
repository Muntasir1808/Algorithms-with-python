class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.level = None


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
        return node

    def in_order_traversal(self, root, elements=[]):
        if root is not None:
            self.in_order_traversal(root.left, elements)
            elements.append(root.data)
            self.in_order_traversal(root.right, elements)
        return elements

    def pre_order_traversal(self, root, elements=[]):
        if root is not None:
            elements.append(root.data)
            self.pre_order_traversal(root.left, elements)
            self.pre_order_traversal(root.right, elements)
        return elements

    def post_order_traversal(self, root, elements=[]):
        if root is not None:
            self.post_order_traversal(root.left, elements)
            self.post_order_traversal(root.right, elements)
            elements.append(root.data)
        return elements
    

    def height(self, root):
        if root is None:
            return -1
        else:
            return max(self.height(root.left), self.height(root.right)) + 1

    def level_order_traversal(self, root):
        q = [root]
        res = []
        while len(q) != 0:
            root = q.pop(0)
            # print(root.data)
            res.append(root.data)
            if root.left is not None:
                q.append(root.left)
            if root.right is not None:
                q.append(root.right)
        return res

    def top_view(self, root):
        q = [root]
        d = dict()
        root.level = 0
        while len(q) != 0:
            root = q.pop(0)
            if root.level not in d:
                d[root.level] = root.data
            if root.left:
                q.append(root.left)
                root.left.level = root.level - 1
            if root.right:
                q.append(root.right)
                root.right.level = root.level + 1
        # print(sorted(d.values()))
        r = sorted(d.values())
        print(*r)



tree = Tree()
root = tree.createNode(5)
tree.insert(root, 2)
tree.insert(root, 10)
tree.insert(root, 7)
tree.insert(root, 15)
tree.insert(root, 12)
tree.insert(root, 20)
tree.insert(root, 30)
tree.insert(root, 6)
tree.insert(root, 8)
print('In-order traversal: ', tree.in_order_traversal(root))
print('Pre-order traversal: ', tree.pre_order_traversal(root))
print('Post-order traversal: ', tree.post_order_traversal(root))
print('Height of the tree: ', tree.height(root))
print('Level order traversal: ', tree.level_order_traversal(root))
tree.top_view(root)

