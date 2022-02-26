from collections import defaultdict


def dfs(graph, start, visited, path):
    path.append(start)
    visited[start] =True
    for neighbour in graph[start]:
        if not visited[neighbour]:
            dfs(graph, neighbour, visited, path)
    return path


vertex, edge = map(int, input().split())
graph = defaultdict(list)
for item in range(edge):
    u, vertex = map(str, input().split())
    print(f"for {item} = {u} {vertex}")
    graph[u].append(vertex)
    graph[vertex].append(u)
print(graph)
path = []
start = "A"
visited = defaultdict(bool)
traversed_path = dfs(graph, start, visited, path)
print(traversed_path)
