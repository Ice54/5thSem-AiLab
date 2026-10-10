import networkx as nx

graph = nx.Graph()
graph.add_edges_from([(5,8),(8,2),(5,4),(4,3),(4,1),(5,7),(7,6),(6,9)])
print(list(nx.dfs_preorder_nodes(graph,5)))