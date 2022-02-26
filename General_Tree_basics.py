class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + '|__' if self.parent else ""
        print(prefix + self.data)
        # if len(self.children) > 0: this can also be written as following
        if self.children:
            for child in self.children:
                child.print_tree()

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level


def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac Book"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Think_pad"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))
    butterfly = TreeNode("LG Butterfly")
    tv.add_child(butterfly)

    mobile = TreeNode("Mobile")
    mobile.add_child(TreeNode("Iphone"))
    mobile.add_child(TreeNode("Google Pixel"))

    root.add_child(laptop)
    root.add_child(tv)
    root.add_child(mobile)

    # print(butterfly.get_level())

    return root


if __name__ == '__main__':
    source_root = build_product_tree()
    source_root.print_tree()
    print(source_root.get_level())