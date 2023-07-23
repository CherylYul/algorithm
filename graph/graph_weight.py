"""
single-source shortest paths problem:
- single-destination shortest-paths: Find a shortest path to a given destination
vertex t from each vertex v. By reversing the direction of each edge in the graph,
we can reduce this problem to a single-source problem.
- single-pair shortest-path: Find a shortest path from u to v for given vertices
u and v. If we solve the single-source problem with source vertex u, we solve this
problem also. Moreover, all known algorithms for this problem have the same worst-case
asymptotic running time as the best single-source algorithms.
- all-pairs shortest-paths: Find a shortest path from u to v for every pair of vertices
u and v. Although we can solve this problem by running a single-source algorithm once
from each vertex, we usually can solve it faster. Additionally, its structure is 
interesting in its own right. Chapter 25 addresses the all-pairs problem in detail.
"""

class Vertex:
    def __init__(self, vertex):
        self.value = vertex
        self.inNeighbors = []
        self.outNeighbors = []
        self.inWeight = []
        self.outWeight = []

        self.distance = None
        self.predecessor = None
        self.status = None

    def has_out_nb(self, v):
        if v in self.outNeighbors:
            return True
        return False

    def has_in_nb(self, v):
        if v in self.inNeighbors:
            return True
        return False

    def has_nb(self, v):
        return self.has_out_nb(v) or self.has_in_nb(v)

    def get_out_nb(self):
        return self.outNeighbors

    def get_in_nb(self):
        return self.inNeighbors

    def add_out_nb(self, v):
        self.outNeighbors.append(v)

    def add_in_nb(self, v):
        self.inNeighbors.append(v)

    def has_out_weight(self, w):
        if w in self.outWeight:
            return True
        return False

    def has_in_weight(self, w):
        if w in self.inWeight:
            return True
        return False

    def has_weight(self, w):
        return self.has_out_weight(w) or self.has_in_weight(w)
    
    def get_out_weight(self):
        return self.outWeight
    
    def get_in_weight(self):
        return self.inWeight

    def add_out_weight(self, w):
        self.outWeight.append(w)
    
    def add_in_weight(self, w):
        self.inWeight.append(w)

    def __repr__(self):
        return str(self.value)

    def __str__(self):
        return self.__repr__()

class Graph:
    def __init__(self, directed = True):
        self.vertices = []
        self.directed = directed
        self.topo = []

    def add_vertex(self, v):
        self.vertices.append(v)

    def add_directed_edge(self, v1, v2, w):
        v1.add_out_nb(v2)
        v2.add_in_nb(v1)
        v1.add_out_weight(w)
        v2.add_in_weight(w)

    def add_undirected_edge(self, v1, v2, w):
        self.add_directed_edge(v1, v2, w)
        self.add_directed_edge(v2, v1, w)

    def get_edge(self):
        edges = []
        for v in self.vertices:
            for nb, w in list(zip(v.outNeighbors, v.outWeight)):
                edges.append((v, nb, w))
        return edges

    """
    Bellman-Ford algorithm: solves the single-source shortest-paths problem in the
    general case in which edges can have negative weight O(VE)
    - Returns true if it is a negative-weight cycle so that no solution exists
    - Returns false if it doesn't have a negative-weight cycle, then produces shortest
    paths and their weights
    """
    def initialize_single_source(self, s): # O(V)
        for v in self.vertices:
            v.distance = float("inf")
            v.predecessor = None
        s.distance = 0
    
    def relax(self, v1, v2, w):
        if v2.distance > v1.distance + w:
            v2.distance = v1.distance + w
            v2.predecessor = v1
    
    def get_distance(self):
        s = ""
        for v in self.vertices:
            s += "{}: {}, ".format(v, v.distance)
        return s
    
    def Bellman_Ford(self, s):
        self.initialize_single_source(s)
        # relaxing each edge of the graph once
        for _ in range(len(self.vertices) - 1):
            for v in self.vertices:
                for nb, w in list(zip(v.outNeighbors, v.outWeight)):
                    self.relax(v, nb, w)
        print(self.get_distance())
        # return true if there is a negative weight cycle
        for v in self.vertices:
            for nb, w in list(zip(v.outNeighbors, v.outWeight)):
                if nb.distance > v.distance + w:
                    return False
        return True
    
    """
    Single-source shortest paths in directed acyclic graphs: topologically sorting
    the dag to impose a linear ordering on the vertices.
    Topo sort: O(V+E), DAG: O(V+E)
    Application: PERT chart: edges represents jobs to be performed and edge weights
    represent the times required to perform particular jobs
    The critical path is a longest path through the dag, means the longest time to 
    perform any sequence of job, so critical path can be seen at total time to perform
    the job
    """
    def topo_sort(self):
        for v in self.vertices:
            v.status = "unvisited"
        for v in self.vertices:
            if v.status == "unvisited":
                self.internal_topo_sort(v)
        return self.topo
    
    def internal_topo_sort(self, v):
        v.status = "visited"
        for nb in v.outNeighbors:
            if nb.status == "unvisited":
                self.internal_topo_sort(nb)
        self.topo.insert(0, v)
    
    def DAG_shortest_paths(self, s):
        self.initialize_single_source(s)
        for v in self.topo:
            for nb, w in list(zip(v.outNeighbors, v.outWeight)):
                self.relax(v, nb, w)
        print(self.get_distance())

    """
    Dijkstra's algorithm: solves the single-source shortest-paths problem in the
    general case with nonnegative weight in edges. (~BFS)
    Dense: O(V^2 + E) = O(V^2)
    Sparse: O((V+E).logV) = O(ElogV)
    """
    def extract_min(self, Q):
        min, pos = Q[0], 0
        for i in range(1, len(Q)):
            if Q[i].distance < Q[0].distance:
                min, pos = Q[i], i
        return min, pos

    def Dijkstra(self, s):
        self.initialize_single_source(s)
        Q = [v for v in self.vertices]
        while Q:
            v, pos = self.extract_min(Q)
            Q.pop(pos)
            for nb, w in list(zip(v.outNeighbors, v.outWeight)):
                self.relax(v, nb, w)
        print(self.get_distance())

    def __repr__(self):
        s = "Vertices: "
        for v in self.vertices:
            s += str(v) + ", " 
        s += "\n"
        s += "Directed: " + str(self.directed) + "\n"
        s += "Edges and Weight: "
        for v1, v2, w in self.get_edge():
            s += "({}, {}, {}), ".format(v1, v2, w)
        return s
    
    def __str__(self):
        return self.__repr__()


tests = []
tests.append({
    "graph": 0,
    "vertices": ["s", "t", "x", "y", "z"],
    "edges": [("s", "t", 6), ("s", "y", 7), ("t", "x", 5), ("t", "y", 8), ("t", "z", -4), 
              ("x", "t", -2), ("y", "x", -3), ("y", "z", 9), ("z", "s", 2), ("z", "x", 7)],
    "index": [(0, 1, 6), (0, 3, 7), (1, 2, 5), (1, 3, 8), (1, 4, -4), 
              (2, 1, -2), (3, 2, -3), (3, 4, 9), (4, 0, 2), (4, 2, 7)],
    "DAG": False,
    "negative": True
})

tests.append({
    "graph": 1,
    "vertices": ["r", "s", "t", "x", "y", "z"],
    "edges": [("r", "s", 5), ("r", "t", 3), ("s", "t", 2), ("s", "x", 6), ("t", "x", 7), 
              ("t", "y", 4), ("t", "z", 2), ("x", "y", -1), ("x", "z", 1), ("y", "z", -2)],
    "index": [(0, 1, 5), (0, 2, 3), (1, 2, 2), (1, 3, 6), (2, 3, 7), 
              (2, 4, 4), (2, 5, 2), (3, 4, -1), (3, 5, 1), (4, 5, -2)],
    "DAG": True,
    "negative": True
})

tests.append({
    "graph": 2,
    "vertices": ["s", "t", "x", "y", "z"],
    "edges": [("s", "t", 10), ("s", "y", 5), ("t", "x", 1), ("t", "y", 2), ("x", "z", 4), 
              ("y", "t", 3), ("y", "x", 9), ("y", "z", 2), ("z", "s", 7), ("z", "x", 6)],
    "index": [(0, 1, 10), (0, 3, 5), (1, 2, 1), (1, 3, 2), (2, 4, 4), 
              (3, 1, 3), (3, 2, 9), (3, 4, 2), (4, 0, 7), (4, 2, 6)],
    "DAG": False,
    "negative": False
})

def simple_test():
    for test in tests:
        print("===============Testing Graph {} ===============".format(test["graph"]))
        print("Test 1: Graph Representation")
        G = Graph()
        for v in test["vertices"]:
            G.add_vertex(Vertex(v))
        for v1, v2, w in test["index"]:
            G.add_directed_edge(G.vertices[v1], G.vertices[v2], w)
        print(G)

        print("Test 2: Bellman Ford")
        if G.Bellman_Ford(G.vertices[0]):
            print("There is no negative weight cycle")
        
        print("Test 3: Single-source Shortest-paths for DAG based on Topo")
        if test["DAG"]:
            print("Topo: ", G.topo_sort())
            G.DAG_shortest_paths(G.vertices[1])
        
        print("Test 4: Dijkstra's algorithm")
        if not test["negative"]:
            G.Dijkstra(G.vertices[0])

simple_test()
#python3 graph/graph_weight.py
