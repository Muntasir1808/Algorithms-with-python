def print_solution(dist):
    print("Vertex Distance from Source")
    for key, value in dist.items():
        print('  ' + key, ' :    ', value)


class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.edges = []
        self.nodes = []

    def add_edge(self, s, d, w):
        self.edges.append([s, d, w])

    def addNode(self, value):
        self.nodes.append(value)

    def bellmanFord(self, src):
        # dist = {i: float("Inf") for i in self.nodes}
        # dist[src] = 0
        dist = {}
        infinity = float("inf")
        for nodes in self.nodes:
            dist[nodes] = infinity
        dist[src] = 0

        for _ in range(self.V - 1):
            for s, d, w in self.edges:
                if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                    dist[d] = dist[s] + w

        for s, d, w in self.edges:
            if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                print("Graph contains negative cycle")
                return

        print_solution(dist)


g = Graph(5)
g.addNode("A")
g.addNode("B")
g.addNode("C")
g.addNode("D")
g.addNode("E")
g.add_edge("A", "C", 6)
g.add_edge("A", "D", 6)
g.add_edge("B", "A", 3)
g.add_edge("C", "D", 1)
g.add_edge("D", "C", 2)
g.add_edge("D", "B", 1)
g.add_edge("E", "B", 4)
g.add_edge("E", "D", 2)
g.bellmanFord("E")
