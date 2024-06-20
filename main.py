from maps import Map, draw_path
from graph import Graph
from dijkstra import shortest_path
import matplotlib.pyplot as plt
import networkx as nx

def visualize_graph(path_edges):
    G = nx.Graph()
    v=0
    des=0
    for edge in path_edges:
     v=edge[1][0]
     G.add_edge(edge[0][0], edge[0][1])
     des=edge[1][1]
    G.add_edge(v,des)
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color="skyblue", font_color="black", font_size=8)
    plt.show()

marietta = Map.load("maps/marietta.map")
graph = Graph(marietta.edge_list)

s = 333 # start: Atrium building
t = 444  # end: Sweet Treats
path = shortest_path(graph,s,t)
path_length = graph.get_path_length(path)

print("====================")
print("map: marietta")
print("shortest path from %s to %s:\n  %d meters" % (s,t,path_length))

# Print the sequence of edges in the path
path_edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
print("Edges in the shortest path:")
for edge in path_edges:
    print(edge)
# Join edges in the path into a string
joined_path = " -> ".join([f"{edge[0]}-{edge[1]}" for edge in path_edges])
print("====================")
print("map: marietta")
print("shortest path from %s to %s:\n  %d meters" % (s, t, path_length))


# Visualize the graph
visualize_graph(path_edges)

# Uncomment to draw path on a map (staticmap module must be installed)
#draw_path(marietta, path, "maps/path.png", source_color='red', destination_color='green')


map1 = """
0-1
|X|
2-3
"""

edge_list = [ (0,1,10),
              (0,2,2),
              (0,3,7),
              (1,2,6),
              (1,3,2),
              (2,3,2) ]
graph = Graph(edge_list)

s = 0 # start
t = 1 # end
path = shortest_path(graph,s,t)
path_length = graph.get_path_length(path)

print("====================")
print("map: ", map1)
print("shortest path from %s to %s:\n  %d" % (s,t,path_length))
