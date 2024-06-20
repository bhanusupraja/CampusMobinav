from graph import Graph
#import staticmap

class Map:
    """A basic class for representing the graph of a street map."""

    def __init__(self,nodes,edges):
        """nodes is a list of node_id,(lat,lon) pairs.
        edges is a list of (x_id,y_id,name,length) tuples.
        """
        self.coordinates = {}
        self.street_names = {}
        self.street_lengths = {}
        self.edge_list = []

        for id,coord in nodes:
            self.coordinates[id] = coord
        for x_id,y_id,name,length in edges:
            x_id,y_id = Graph._normalize(x_id,y_id)
            length = int(length) # convert to integers
            self.street_names[(x_id,y_id)] = name
            self.street_lengths[(x_id,y_id)] = length
            self.edge_list.append((x_id,y_id,length))

    """
    @classmethod
    def load_pickle(cls,filename):
        import pickle
        with open(filename,"rb") as f:
            sgraph = pickle.load(f)
        nodes = sgraph.nodes.items() # (id,(lat,lon))
        edges = sgraph.edges.values() # x,y,name,length
        return Map(nodes,edges)
    """

    @classmethod
    def load(cls,filename):
        do_edges = False
        nodes = []
        edges = []
        with open(filename,"r") as f:
            lines = f.readlines()
        for line in lines:
            line = line.strip()
            if line.startswith("nodes"):
                pass
            elif line.startswith("edges"):
                do_edges = True
            elif not do_edges: # do nodes
                node_id,lat,lon = line.split(":")
                node_id = int(node_id)
                lat = float(lat)
                lon = float(lon)
                nodes.append((node_id,(lat,lon)))
            else: # do edges
                x_id,y_id,name,length = line.split(":")
                x_id = int(x_id)
                y_id = int(y_id)
                length = int(length)
                edges.append((x_id,y_id,name,length))
        return Map(nodes,edges)

    def save(self,filename):
        with open(filename,"w") as f:
            f.write("nodes\n")
            for node_id in sorted(self.coordinates.keys()):
                lat,lon = self.coordinates[node_id]
                f.write("%d:%.8f:%.8f\n" % (node_id,lat,lon))
            f.write("edges\n")
            for x_id,y_id,length in self.edge_list:
                name = self.street_names[(x_id,y_id)]
                name = name.replace(":","")
                f.write("%d:%d:%s:%d\n" % (x_id,y_id,name,length))
            
def draw_path(my_map,path,filename):
    """uses staticmap module to draw a path on a map"""
    import staticmap

    line_color = "red"
    line_length = 10

    m = staticmap.StaticMap(1024,1024,64)
    for x,y in path:
        xlat,xlon = my_map.coordinates[x]
        ylat,ylon = my_map.coordinates[y]

        lats = [xlat,ylat]
        lons = [xlon,ylon]

        line = [ (xlon,xlat), (ylon,ylat) ]
        line = staticmap.Line(line,line_color,line_length)
        m.add_line(line)

    image = m.render()
    image.save(filename)

