class Vertex:
    def __init__(self, vertex):
        self.value = vertex
        self.inNeighbors = []
        self.outNeighbors = []
        # attributes for DFS and BFS
        self.predecessor = None
        self.discovery = None
        self.finish = None
        self.color = "W"
        self.distance = None
        self.path = None
    
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

    def add_directed_edge(self, v1, v2):
        v1.add_out_nb(v2)
        v2.add_in_nb(v1)

    def add_undirected_edge(self, v1, v2):
        self.add_directed_edge(v1, v2)
        self.add_directed_edge(v2, v1)

    def get_edge(self):
        edges = []
        for v in self.vertices:
            for nb in v.outNeighbors:
                edges.append((v, nb))
        return edges
    
    """
    DFS depth_first_search: DFS enumerates the deepest paths, only backtracking when
    it hits a dead end or an already-explored section of the graph.
    - To prevent loop, we keep track of color of each vertex (W: unvisited, G: explored, 
    B: finish backtrack), then skipping the non-W vertices
    - Keep track of the predecessor of vertices
    - Marks 2 auto-incrementing timestamps discovery and finish to inidicate when the node
    was explored or finished backtracking.
    O(V+E)

    There are 4 types of edges in depth-first forests:
    1. Tree edges: an edge from predecessor vertex to successor neighbor, say in  (v, n), 
    n was first discovered from v
    2. Back edges: connect vertex to its ancestor neighbor (neighbor should be gray which
    was discovered before by other node)
    3. Forward edges: a non-tree edge connect vertex to descendant neighbor in a dfs 
    (neighbor's discovery time must after vertex's discovery time)
    4. Cross edges: other edges
    """
    def DFS(self, verbose = False):
        for v in self.vertices:
            v.predecessor = None
            v.color = "W"
            v.discovery = None
            v.finish = None
        time = 0
        for v in self.vertices:
            if v.color == "W":
                time = self.internal_DFS(v, time, verbose)
    
    def internal_DFS(self, v, time, verbose):
        time += 1
        v.color = "G"
        v.discovery = time
        if verbose:
            print("{} discovered time: {}". format(v, time))

        for nb in v.outNeighbors:
            if not verbose: 
                if nb.color == "W":
                    nb.predecessor = v
                    time = self.internal_DFS(nb, time, verbose)
            else:
                if nb.color == "W":
                    print("{} and {} is a tree edge".format(v, nb))
                    nb.predecessor = v
                    time = self.internal_DFS(nb, time, verbose)
                elif nb.color == "G":
                    print("{} and {} is a back edge".format(v, nb))
                elif nb.discovery > v.discovery:
                    print("{} and {} is a forward edge".format(v, nb))
                else:
                    print("{} and {} is a cross edge".format(v, nb))

        time += 1
        v.color = "B"
        v.finish = time
        self.topo.insert(0, v)
        if verbose:
            print("{} finished time: {}". format(v, time))
        return time
    
    def DFS_stack(self, v):
        pass

    """
    Topological_sort: a linear ordering of all its vertices such that if graph contains
    an edge (u, v) then u appears before v in the ordering.
    O(V+E)
    """
    def topo_sort(self):
        if not self.topo:
            self.DFS()
        print(self.topo)

    """
    SCC strongly connected components O(V+E)
    1. Call DFS to create DFS forest, choose starting vertices in any order, keep track of
    finishing times.
    2. Reverse all the edges in the graph.
    3. Do DFS again to create another DFS forest, start with the vertex has largest finishing
    time (order the nodes in the reverse order of the finishing times that they had from the
    first DFS run)
    4. The SCCs are the different trees in the second DFS forest
    """
    def SCC(self):
        if not self.topo:
            self.DFS()
        for v in self.vertices:
            v.color = "W"
        SCCs = []
        for v in self.topo:
            if v.color == "W":
                scc = [v]
                scc = self.internal_SCC(v, scc)
                SCCs.append(scc) 
        return SCCs
    
    def internal_SCC(self, v, scc):
        v.color = "G"
        for nb in v.inNeighbors:
            if nb.color == "W":
                scc.append(nb)
                scc = self.internal_SCC(nb, scc)
        v.color = "B"
        return scc

    """
    Simple_path: O(V+E): returns the number of simple paths from u to v. We can do it
    by rechecking the vertices spreading to v, until reach vertex u. To avoid subproblems
    we can take the advantage of topo-sort, since there is only possible path from u to v 
    """
    def simple_path(self, u, v):
        try:
            start = self.topo.index(u)
            end = self.topo.index(v)
        except ValueError:
            print("{} or {} is not the vertex of the graph".format(u, v))
        if end <= start:
            return 0
        for i in range(start, end+1):
            self.topo[i].path = None
        v.path = 1
        return self.simple_path_aid(start, end)

    def simple_path_aid(self, i, end):
        if i > end:
            return 0
        elif self.topo[i].path:
            return self.topo[i].path
        else:
            self.topo[i].path = 0
            for nb in self.topo[i].outNeighbors:
                nb_i = self.topo.index(nb)
                self.topo[i].path += self.simple_path_aid(nb_i, end)
            return self.topo[i].path

    """
    BFS breadth_first_search: expands the frontier between discovered and undiscovered
    nodes uniformly across the breadth of the frontier, discovering all nodes at a distance
    k from the source node before nodes at distance k + 1. Shortest path from s to v is 
    δ(s, v) = v.d, which is the distance: track[v]["distance"]

    - BFS keep track of color of each vertex (W: unvisited, G: explored, B: finished checking
    its neighbors)
    - Keep track of the predecessor of vertices
    - Using a queue to enqueue and dequeue in order after each of the node changing color to B

    Enqueued O(1) + Dequeued O(1) V times + Scanning adjacency lists at most E times
    O(V + E)
    """
    def BFS(self, v):
        for u in self.vertices:
            u.predecessor = None
            u.color = "W"
            u.distance = None
        v.distance = 0
        v.color = "G"
        L = [[] for _ in range(len(self.vertices))]
        L[0] = [v]
        for i in range(len(L)):
            for v in L[i]:
                for nb in v.outNeighbors:
                    if nb.color == "W":
                        nb.color = "G"
                        nb.distance = v.distance + 1
                        nb.predecessor = v
                        L[i + 1].append(nb)
        return L
    
    def BFS_queue(self, v):
        for u in self.vertices:
            u.predecessor = None
            u.color = "W"
            u.distance = None
        v.color = "G"
        v.distance = 0
        queue = [v]
        while queue:
            node = queue.pop(0)
            for nb in node.outNeighbors:
                if nb.color == "W":
                    nb.predecessor = v
                    nb.distance = v.distance + 1
                    nb.color = "G"
                    queue.append(nb)

    """
    Find shortest path from v to u, assumming that BFS has already computed a BF tree. O(V)
    """
    def find_shortest_path(self, v, u):
        if u == v:
            print(v)
        elif not u.predecessor:
            print("No path from {} to {} exists".format(v, u))
        else:
            self.find_shortest_path(v, u.predecessor)
            print(u)

    """
    Checking if the graph is bipartiteness or not
    """
    def bipartite(self):
        BF_tree = self.BFS(self.vertices[0])
        print(BF_tree)
        for i in range(len(BF_tree)):
            for v in BF_tree[i]:
                v.color = "Y" if (i % 2 == 0) else "R"
        for level in BF_tree:
            for v in level:
                for nb in v.outNeighbors:
                    if nb.color == v.color:
                        return False
        return True

    def __repr__(self):
        s = "Vertices: "
        for v in self.vertices:
            s += str(v) + ", " 
        s += "\n"
        s += "Directed: " + str(self.directed) + "\n"
        s += "Edges: "
        for v1, v2 in self.get_edge():
            s += "({}, {}), ".format(v1, v2)
        return s
    
    def __str__(self):
        return self.__repr__()

simple_tests = []
simple_tests.append({
    "graph": 1,
    "vertices": [0, 1, 2, 3, 4],
    "edges": [(0, 1), (0, 4), (1, 4), (1, 3), (1, 2), (2, 3), (3, 4)],
    "index": [(0, 1), (0, 4), (1, 4), (1, 3), (1, 2), (2, 3), (3, 4)],
    "directed": False
})

simple_tests.append({
    "graph": 2,
    "vertices": [0, 1, 2, 3, 4, 5, 6, 7],
    "edges": [(0, 1), (1, 2), (2, 3), (3, 4), (3, 5), (4, 5), (4, 6), (5, 6), (5, 7), (6, 7)],
    "index": [(0, 1), (1, 2), (2, 3), (3, 4), (3, 5), (4, 5), (4, 6), (5, 6), (5, 7), (6, 7)],
    "directed": False
})

simple_tests.append({
    "graph": 3,
    "vertices": [0, 1, 2, 3, 4, 5],
    "edges": [(0, 1), (0, 3), (1, 2), (2, 3), (3, 1), (4, 2), (4, 5), (5, 5)],
    "index": [(0, 1), (0, 3), (1, 2), (2, 3), (3, 1), (4, 2), (4, 5), (5, 5)],
    "directed": True
})

simple_tests.append({
    "graph": 4,
    "vertices": [0, 1, 2, 3, 4, 5, 6, 7],
    "edges": [(0, 1), (0, 4), (1, 2), (1, 4), (2, 3), (3, 1), (4, 3), (5, 6), 
              (5, 7), (6, 0), (6, 4), (7, 5), (7, 6)],
    "index": [(0, 1), (0, 4), (1, 2), (1, 4), (2, 3), (3, 1), (4, 3), (5, 6), 
              (5, 7), (6, 0), (6, 4), (7, 5), (7, 6)],
    "directed": True
})

simple_tests.append({
    "graph": 5,
    "vertices": ["shirt", "tie", "jacket", "belt", "watch", "undershorts", "pants", 
                 "shoes", "socks"],
    "edges": [("shirt", "tie"), ("shirt", "belt"), ("tie", "jacket"), ("belt", "jacket"),
              ("undershorts", "pants"), ("undershorts", "shoes"), ("pants", "belt"), 
              ("pants", "shoes"), ("socks", "shoes")],
    "index": [(0, 1), (0, 3), (1, 2), (3, 2), (5, 6), (5, 7), (6, 3), (6, 7), (8, 7)],
    "directed": True,
})

simple_tests.append({
    "graph": 6,
    "vertices": ["m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"],
    "edges": [("m", "q"), ("m", "r"), ("m", "x"), ("n", "o"), ("n", "q"), ("n", "u"), 
              ("o", "r"), ("o", "s"), ("o", "v"), ("p", "o"), ("p", "s"), ("p", "z"), 
              ("q", "t"), ("r", "u"), ("r", "y"), ("s", "r"), ("u", "t"), ("v", "w"), 
              ("v", "x"), ("w", "z"), ("y", "v")],
    "index": [(0, 4), (0, 5), (0, 11), (1, 2), (1, 4), (1, 8), (2, 5), (2, 6), (2, 9), 
              (3, 2), (3, 6), (3, 13), (4, 7), (5, 8), (5, 12), (6, 5), (8, 7), (9, 10), 
              (9, 11), (10, 13), (12, 9)],
    "directed": True,
})

simple_tests.append({
    "graph": 7,
    "vertices": [0, 1, 2, 3, 4, 5, 6, 7],
    "edges": [(0, 1), (0, 4), (1, 2), (1, 3), (2, 1), (3, 3), (4, 0), (4, 3), (5, 2), 
              (5, 6), (6, 2), (6, 7), (7, 5)],
    "index": [(0, 1), (0, 4), (1, 2), (1, 3), (2, 1), (3, 3), (4, 0), (4, 3), (5, 2), 
              (5, 6), (6, 2), (6, 7), (7, 5)],
    "directed": True,
})

simple_tests.append({
    "graph": 8,
    "vertices": ["A", "B", "C", "D", "E", "F", "G"],
    "edges": [("A", "B"), ("A", "E"), ("B", "C"), ("B", "D"), ("B", "F"), ("C", "D"),
              ("C", "G"), ("D", "G"), ("F", "G")],
    "index": [(0, 1), (0, 4), (1, 2), (1, 3), (1, 5), (2, 3), (2, 6), (3, 6), (5, 6)],
    "directed": False,
})

simple_tests.append({
    "graph": 9,
    "vertices": ["dpkg", "libbz2", "libselinux1", "multiarch-support", "tar", "coreutils"],
    "edges": [("dpkg", "libbz2"), 
              ("dpkg", "multiarch-support"),
              ("dpkg", "tar"), 
              ("dpkg", "coreutils"), 
              ("libbz2", "libselinux1"), 
              ("libselinux1", "multiarch-support"),
              ("coreutils", "libbz2"), 
              ("coreutils", "libselinux1")],
    "index": [(0, 1), (0, 3),(0, 4), (0, 5), (1, 2), (2, 3),(5, 1), (5, 2)],
    "directed": True,
})

simple_tests.append({
    "graph": 10,
    "vertices": ["A", "B", "C", "D", "E", "F", "G"],
    "edges": [("A", "B"), ("A", "E"), ("B", "C"), ("B", "F"), ("C", "G"), ("D", "E"), 
              ("D", "G"), ("F", "G")],
    "index": [(0, 1), (0, 4), (1, 2), (1, 5), (2, 6), (3, 4), (3, 6), (5, 6)],
    "directed": False,
})

simple_tests.append({
    "graph": 11,
    "vertices": ["Stanford", "Wikipedia", "Puppies", "Google", "NYTimes", "Berkeley"],
    "edges": [("Stanford", "Wikipedia"), ("Stanford", "Puppies"), ("Wikipedia", "Stanford"), 
              ("Wikipedia", "Puppies"), ("Wikipedia", "NYTimes"), ("Puppies", "Google"), 
              ("Google", "Puppies"), ("NYTimes", "Stanford"), ("NYTimes", "Puppies"), 
              ("Berkeley", "Stanford"), ("Berkeley", "Puppies")],
    "index": [(0, 1), (0, 2), (1, 0), (1, 2), (1, 4), (2, 3), (3, 2), (4, 0), (4, 2), 
              (5, 0), (5, 2)],
    "directed": True,
})

def simple_test():
    for test in simple_tests:
        
        G = Graph() if test["directed"] else Graph(False)
        print("====================Testing Graph {}: ====================".format(test["graph"]))
        
        print("Test 1: Graph Representation: ")
        for v in test["vertices"]:
            G.add_vertex(Vertex(v))
        V = G.vertices
        for v1, v2 in test["index"]:
            if test["directed"]:
                G.add_directed_edge(V[v1], V[v2])
            else:
                G.add_undirected_edge(V[v1], V[v2])
        print(G)
        
        print("Test 2: DFS discovery and finishing time: ")
        G.DFS(True)

        print("Test 3: DFS - TopoSort for directer graph: ")
        if test["directed"]:
            G.topo_sort()

        print("Test 4: BFS - Breadth first search tree: ")
        levels = G.BFS(G.vertices[0])
        for i in range(len(levels)):
            print("Level", i, ":")
            for j in levels[i]:
                print("\t", j)
        # Find the distance from vertex number 1 to vertex number 6
        # for i in range(len(levels)):
        #     if G.vertices[6] in levels[i]:
        #         print("distance from 1 to 6 is", i)
        #         break

        print("Test 5: DFS - Strongly connected components for directed graph: ")
        if test["directed"]:
            print(G.SCC())
        
        print("Test 6: DFS - Simple path for graph 6: ")
        if test["graph"] == 6:
            print(G.simple_path(G.vertices[3], G.vertices[9]))
            print(G.simple_path(G.vertices[9], G.vertices[6]))

        end = len(G.vertices) - 1
        print("Test 7: BFS - Shortest path from {} to {}: ".format(G.vertices[0], G.vertices[end]))
        G.find_shortest_path(G.vertices[0], G.vertices[end])

        print("Test 8: BFS - Bipartiteness testing for undirected graph: ")
        if not test["directed"]:
            if G.bipartite():
                print("This is a bipartite graph.")
            else:
                print("This is not a bipartite graph.")


simple_test()
# python3 graph_linked_list.py