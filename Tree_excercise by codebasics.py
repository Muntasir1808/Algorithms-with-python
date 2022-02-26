class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def print_tree(self, level_limit):
        if self.get_level() <= level_limit:
            spaces = ' ' * self.get_level() * 3
            prefix = spaces + "|__" if self.parent else ""
            print(prefix + self.data)
            for child in self.children:
                child.print_tree(level_limit)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level


def build_location_tree():
    root = TreeNode("Global")
    india = TreeNode("India")
    gujarat = TreeNode("Gujarat")
    gujarat.add_child(TreeNode("Ahmedabad"))
    gujarat.add_child(TreeNode("Baroda"))

    karnataka = TreeNode("Karnataka")
    karnataka.add_child(TreeNode("Bangalore"))
    karnataka.add_child(TreeNode("Mysore"))

    root.add_child(india)
    india.add_child(gujarat)
    india.add_child(karnataka)

    usa = TreeNode("USA")
    root.add_child(usa)
    new_jersey = TreeNode("New Jersey")
    new_jersey.add_child(TreeNode("Princeton"))
    new_jersey.add_child((TreeNode("Trenton")))

    california = TreeNode("California")
    california.add_child(TreeNode("San Francisco"))
    california.add_child(TreeNode("Mountain view"))
    california.add_child(TreeNode("Palo Alto"))

    usa.add_child(new_jersey)
    usa.add_child(california)
    # print(california.get_level()
    return root


if __name__ == '__main__':
    root_node = build_location_tree()
    root_node.get_level()
    level_no = int(input())
    root_node.print_tree(level_no)
