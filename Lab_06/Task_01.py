stack = []
graph = {
    'S': ['d', 'e', 'p'],
    'a': [],
    'b': ['a'],
    'c': ['a'],
    'd': ['b', 'c', 'e'],
    'e': ['h', 'r'],
    'f': ['c', 'G'],
    'G': [],
    'h': ['p', 'q'],
    'p': ['q'],
    'q': [],
    'r': ['f'],
}
path = []

def get_neighbours(graph, node, stack, path):
    path.append(node)
    count = 0
    for child_node in graph[node]:
        if child_node not in path:
            stack.append(child_node)
            count = count + 1
    for values in range(count):
        next_node = stack.pop()
        if next_node not in path:
            get_neighbours(graph,next_node, stack, path)
    return path

print(get_neighbours(graph, 'S', stack, path))