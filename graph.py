from collections import defaultdict

class Graph:
    """A basic class for representing an undirected graph with weights on edges.
    Each node is a unique integer.
    Each edge is a tuple (x_id,y_id,length).
    """

    def __init__(self,edge_list):
        """edge list is a list of edges, where an edge is a tuple (x_id,y_id,length)"""
        self.edge_list = edge_list
        # map from edge (x,y) to length
        self.edge_lengths = {}
        # map from node to a list of its neighbors
        self.node_neighbors = defaultdict(set)

        self.m = len(edge_list) # number of edges
        self.n = 0              # number of nodes
        for x_id,y_id,length in edge_list:
            self._add_edge(x_id,y_id,length)

    def _add_node(self,node_id):
        if node_id not in self.node_neighbors:
            self.node_neighbors[node_id] = set()
        # assuming index 0 is a node, the number of nodes is the maximum id + 1
        self.n = max(self.n,node_id+1)

    def _add_edge(self,x_id,y_id,length):
        self._add_node(x_id)
        self._add_node(y_id)
        self.node_neighbors[x_id].add(y_id)
        self.node_neighbors[y_id].add(x_id)
        x_id,y_id = Graph._normalize(x_id,y_id)
        self.edge_lengths[(x_id,y_id)] = length

    @classmethod
    def _normalize(cls,x,y):
        """for an edge (x,y), reorder x and y so that x<y"""
        return (x,y) if x<y else (y,x)
        
    def get_edge_length(self,x,y):
        x,y = Graph._normalize(x,y)
        if (x,y) not in self.edge_lengths:
            raise Exception("error: edge (%d,%d) not found" % (x,y))
        return self.edge_lengths[(x,y)]

    def get_path_length(self,path):
        if path is None:
            raise Exception("error: path is None")
        length = 0
        for x,y in path: # for each edge (x,y) on the path
            length += self.get_edge_length(x,y)
        return length
