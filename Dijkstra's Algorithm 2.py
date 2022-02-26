graph = {'a': {'b': 10, 'c': 3}, 'b': {'c': 1, 'd': 2}, 'c': {'b': 4, 'd': 8, 'e': 2}, 'd': {'e': 7}, 'e': {'d': 9}}
print(graph["c"].items())


def dijkstra(graph, start, goal):
    shortest_distance = {}
    predecessor = {}
    unseenNodes = graph
    infinity = float("inf")
    path = []
    for node in unseenNodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0

    while unseenNodes:
        # print(f"inside while {unseenNodes}")
        minNode = None
        for node in unseenNodes:
            if minNode is None:
                minNode = node
            elif shortest_distance[node] < shortest_distance[minNode]:
                minNode = node
        path_options = graph[minNode].items()
        print(path_options)
        for childNode, weight in path_options:
            if weight + shortest_distance[minNode] < shortest_distance[childNode]:
                print(f"weight + shortest[minNode] = {weight} + {shortest_distance[minNode]} = {weight + shortest_distance[minNode]}")
                print(f"initial = {shortest_distance[childNode]:}")
                shortest_distance[childNode] = weight + shortest_distance[minNode]
                print(f"final = { shortest_distance[childNode]}")
                predecessor[childNode] = minNode
        # print(f"{unseenNodes.pop(minNode)} is popped")
        unseenNodes.pop(minNode)

        print(predecessor)

    currentNode = goal
    while currentNode != start:
        try:
            path.append(currentNode)
            currentNode = predecessor[currentNode]
        except KeyError:
            print('Path not reachable')
            break
    path.append(start)
    path.reverse()
    if shortest_distance[goal] != infinity:
        print('Shortest distance is ' + str(shortest_distance[goal]))
        print('And the path is ' + str(path))


dijkstra(graph, 'a', 'b')

