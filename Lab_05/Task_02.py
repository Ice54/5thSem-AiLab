class DWGraph:
    def __init__(self):
        self.graph = {}

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = {}

    def add_edge(self, a, b, cost):
        self.graph[a][b] = cost

    def find_path(self, start, end, path=[], cost=0):
        path = path + [start]
        if start == end:
            return path, cost
        for node in self.graph[start]:
            if node not in path:
                result = self.find_path(node, end, path, cost + self.graph[start][node])
                if result:
                    return result
        return None

g = DWGraph()
for n in ['A', 'B', 'C', 'D', 'E', 'F']:
    g.add_node(n)

g.add_edge('A', 'B', 2)
g.add_edge('A', 'C', 1)
g.add_edge('B', 'C', 2)
g.add_edge('B', 'D', 5)
g.add_edge('C', 'D', 1)
g.add_edge('C', 'F', 3)
g.add_edge('D', 'C', 1)
g.add_edge('D', 'E', 4)
g.add_edge('E', 'F', 3)
g.add_edge('F', 'C', 1)
g.add_edge('F', 'E', 2)

result = g.find_path('A', 'E')
if result:
    print("Path:", result[0])
    print("Cost:", result[1])
else:
    print("No path")