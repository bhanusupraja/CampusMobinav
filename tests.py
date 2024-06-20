from math import inf
from maps import Map, draw_path
from graph import Graph
from dijkstra import shortest_path

def test_marietta():
    marietta = Map.load("maps/marietta.map")
    graph = Graph(marietta.edge_list)

    s = 5637
    t = 212
    path = shortest_path(graph,s,t)
    path_length = graph.get_path_length(path)

    assert path_length == 4337

def test_graph_one():
    edge_list = [ (0,1,10),
                  (0,2,2),
                  (0,3,7),
                  (1,2,6),
                  (1,3,2),
                  (2,3,2) ]
    graph = Graph(edge_list)

    s,t = 0,1
    path = shortest_path(graph,s,t)
    path_length = graph.get_path_length(path)

    assert path_length == 6

def test_graph_two():
    edge_list = [ (0,1,1),
                  (1,2,1),
                  (3,4,1),
                  (4,5,1) ]
    graph = Graph(edge_list)

    s,t = 0,5
    path = shortest_path(graph,s,t)

    assert path == None

def test_graph_three():
    edge_list = [ (0,1,1),
                  (1,2,1),
                  (3,4,1),
                  (4,5,1) ]
    graph = Graph(edge_list)

    s,t = 0,0
    path = shortest_path(graph,s,t)

    assert path == []

def test_graph_four():
    n = 1000
    # chain graph 0 -- 1 -- 2 -- ... -- n
    edge_list = [ (i,i+1,i+1) for i in range(n+1) ]
    graph = Graph(edge_list)

    s,t = 0,n
    path = shortest_path(graph,s,t)
    path_length = graph.get_path_length(path)
    opt_length = int(n*(n+1)/2)

    assert path_length == opt_length
