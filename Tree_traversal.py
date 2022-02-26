class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return
        elif data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        elif data > self.data:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()
        elements.append(self.data)
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def pre_order_traversal(self):
        pre_order_list = [self.data]
        if self.left:
            pre_order_list += self.left.pre_order_traversal()
        if self.right:
            pre_order_list += self.right.pre_order_traversal()
        return pre_order_list

    def post_order_traversal(self):
        post_order_list = []
        if self.left:
            post_order_list += self.left.post_order_traversal()
        if self.right:
            post_order_list += self.right.post_order_traversal()
        post_order_list.append(self.data)
        return post_order_list

    def search(self, value):
        if self.data == value:
            return True
        elif value < self.data:
            if self.left:
                return self.left.search(value)
            else:
                return False
        elif value > self.data:
            if self.right:
                return self.right.search(value)
            else:
                return False

    def minimum_node(self):
        if self.left is None:
            return self.data
        else:
            return self.left.minimum_node()

    def maximum_node(self):
        if self.right is None:
            return self.data
        else:
            return self.right.maximum_node()

    def summation_all_nodes(self):
        left_sum = self.left.summation_all_nodes() if self.left else 0
        right_sum = self.right.summation_all_nodes() if self.right else 0
        return self.data + left_sum + right_sum

    def delete_node(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete_node(val)
        if val > self.data:
            if self.right:
                self.right = self.right.delete_node(val)
        else:
            # for deleting the leaf node
            if self.left is None and self.right is None:
                return None
            # when there is no left sub tree
            if self.left is None:
                return self.right
            # when there is no right sub tree
            if self.right is None:
                return self.left
            # when there is both left and right sub tree
            else:
                # min_value = self.right.minimum_node()
                # self.data = min_value
                # self.right = self.right.delete_node(min_value)
                max_val = self.left.maximum_node()
                self.data = max_val
                self.left = self.left.delete_node(max_val)
        return self


def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])
    for item in range(1, len(elements)):
        root.add_child(elements[item])

    return root


if __name__ == '__main__':
    # numbers = [15, 27, 12, 88, 20, 23, 14, 7]
    numbers = [1, 2, 5, 3, 4, 6]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.in_order_traversal())
    print(numbers_tree.search(21))
    print(numbers_tree.pre_order_traversal())
    print(numbers_tree.post_order_traversal())
    print(numbers_tree.minimum_node())
    print(numbers_tree.maximum_node())
    print(numbers_tree.summation_all_nodes())
    numbers_tree.delete_node(23)
    print(numbers_tree.in_order_traversal())
