graph ={
    'S' : [('A',0),('C',5),('B',5)],
    'A' : [('S',0)],
    'B' : [('S',5)],
    'C' : [('S',5)]
}
stack2 =[]

def get_neighbours(graph, node, stack, path):
    path.append(node[0])
    stack2.append(node[0])
    count = 0
    for child_node in graph[node]:
        if child_node[0] not in path:
            stack.append(child_node)
            count = count + 1
    for values in range(count):
        next_node = stack.pop()
        if next_node[0] not in path:
            get_neighbours(graph,next_node[0], stack, path)
    return path

print(get_neighbours(graph,'S',[],[]))
