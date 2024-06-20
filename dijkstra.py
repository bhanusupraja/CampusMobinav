from collections import defaultdict
from math import inf

def find_closest(open_list,distances):
    """find the closest node in the open list.  note that this can be more efficient"""
    closest_node,closest_distance = None,inf
    for node in open_list:
        distance = distances[node]
        if distance < closest_distance:
            closest_distance = distance
            closest_node = node
    return closest_node

def extract_path(back_ptr,t):
    """follow back pointers to re-construct the shortest-path"""
    path = []
    while True:
        n = back_ptr[t]
        if n is None: break
        path.append((n,t))
        t = n
    path.reverse()
    return path

def shortest_path(graph,s,t):
    """return the shortest path from s to t in graph.

    graph is a Graph object
    s is a node id (integer) of the start node
    t is a node id (integer) of the end node

    returns a path, which is a list of edges where each edge is a pair of node id's
    if s and t are not connected, returns None
    """

    # map from node to current distance, default to length of infinity
    distances = defaultdict(lambda: inf)

    # save the edge used to get the closest distance
    back_ptr = defaultdict(lambda: None)
    # initialize lists
    closed_list, open_list = set(), set()

    # add start node
    open_list.add(s)
    distances[s] = 0
    back_ptr[s] = None

    while open_list:
        closest_node = find_closest(open_list,distances)
        closest_distance = distances[closest_node]

        open_list.remove(closest_node)
        closed_list.add(closest_node)
        if closest_node == t: break # found destination

        # update distances based on new closest node
        neighbors = graph.node_neighbors[closest_node]
        for neighbor in neighbors:
            if neighbor in closed_list: continue
            length = graph.get_edge_length(closest_node,neighbor)
            neighbor_distance = closest_distance + length
            if neighbor_distance < distances[neighbor]:
                open_list.add(neighbor)
                distances[neighbor] = neighbor_distance
                back_ptr[neighbor] = closest_node

    if t not in closed_list: return None
    return extract_path(back_ptr,t)

