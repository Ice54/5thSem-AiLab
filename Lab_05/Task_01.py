graph = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D', 'F'],
         'D': ['C', 'E'],
         'E': ['F'],
         'F': ['C', 'E']}

def find_shortest_path(graph, start, end):
    queue = [[start]]
    visited = [start]
    while len(queue) > 0:
        path = queue.pop(0)
        node = path[-1]
        if node == end:
            return path
        for n in graph[node]:
            if n not in visited:
                visited.append(n)
                queue.append(path + [n])
    return None

print(find_shortest_path(graph, 'A', 'D'))