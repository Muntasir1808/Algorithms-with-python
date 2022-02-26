from queue import Queue
# adj_list = {}
# n = int(int(input()))
# for item in range(n):
#     key = input()
#     value = list(input().split())
#     adj_list.update({key: value})
# print(adj_list)
adj_list = {
    "A": ["B", "D"],
    "B": ["A", "C"],
    "C": ["B"],
    "D": ["A", "E", "F"],
    "E": ["D", "F", "G"],
    "F": ["D", "E", "H"],
    "G": ["E", "H"],
    "H": ["G", "F"]
}
print("adj list is :")
print(adj_list)

visited = {}
level = {}
parent = {}
bfs_traversal_output = []
queue = Queue()
for node in adj_list.keys():
    visited[node] = False
    parent[node] = None
    level[node] = -1
# print(visited)
# print(level)
# print(parent)
s = "A"
visited[s] = True
level[s] = 0
queue.put(s)
while not queue.empty():
    u = queue.get()
    bfs_traversal_output.append(u)
    for items in adj_list[u]:
        if not visited[items]:
            visited[items] = True
            parent[items] = u
            level[items] = level[u] + 1
            queue.put(items)
print(bfs_traversal_output)
# to find shortest distance
print(level)
# print level of D
print(level["D"])

