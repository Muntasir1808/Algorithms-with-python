class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}

        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
        print(self.graph_dict)

    def get_paths(self, start, end, path=[]):
        path = path + [start]
        # print('path = ', path, 'start = ', start)
        if start == end:
            return [path]
        elif start not in self.graph_dict.keys():
            return []
        else:
            full_path = []
            for node in self.graph_dict[start]:
                # if node not in path:
                # print(f' before , node = {node}, end = {end}, start = {start}, path = {path}')
                new_paths = self.get_paths(node, end, path)
                # print(f' after , node = {node}, end = {end}, start = {start}, path = {path}')
                for item in new_paths:
                    full_path.append(item)
        return full_path

    def get_shortest_path(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.graph_dict:
            return []
        else:
            shortest_path = None
            for node in self.graph_dict[start]:
                sp = self.get_shortest_path(node, end, path)
                if sp or len(sp) < len(shortest_path):
                    shortest_path = sp

        return shortest_path


routes = [
    ('Mumbai', 'Paris'),
    ('Mumbai', 'Dubai'),
    ('Paris', 'Dubai'),
    ('Paris', 'New York'),
    ('Dubai', 'New York'),
    ('New York', 'Toronto'),
]
initial = input()
end = input()
route_graph = Graph(routes)
print(route_graph.get_paths(initial, end))
print(route_graph.get_shortest_path(initial, end))
