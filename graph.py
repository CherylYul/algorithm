# class Vertex:
#     def __init__(self, start, key, color = "W", distance = None, predecessor = None):
#         self.start = start
#         self.key = key
#         self.color = color
#         self.distance = distance
#         self.predecessor = predecessor

class Graph:
    def __init__(self, num_vertices, edges, directed = False, vertex_name = None):
        self.bfs = None
        self.dfs = None
        self.topo_sort = []
        if vertex_name:
            self.data = {name:[] for name in vertex_name}
        else:
            self.data = {i:[] for i in range(num_vertices)}

        if directed:
            for n1, n2 in edges:
                self.data[n1].append(n2)
        else:
            for n1, n2 in edges:
                self.data[n1].append(n2)
                self.data[n2].append(n1)

    """
    Breadth_first_search (BFS): search through the graph from the starting vertex input
    and then spread through its neighbors to other nodes until go through all the node
    in the graph.
    1. Mark all the vertex's color to white, distance and predecessor to None, after:
    - Change the node to gray when discover it
    - Change the node to black when finishing checking its neihgbors
    2. Mark the starting vertex to gray and distance to 0, predecessor to None and using
    a list to queue the next node, which we want to check its neighbor
    3. Iterates as long as there remain gray vertices, which are discovered vertices
    that have not yet had their adjacency lists fully examined. 

    Each vertex is enqueued O(1) and dequeued O(1) at most 1 time, so total O(V)
    Total time spent in scanning adjacency lists is O(E)
    => BFS run in O(V + E)
    
    Shortest path from starting vertex to some vertex v δ(s, v) = v.d, which is
    track[v]["distance"]
    """
    def breadth_first_search(self, start):

        track = {i: {"color": "W",
                     "distance": None,
                     "predecessor": None} for i in self.data}
        track[start]["color"] = "G"
        track[start]["distance"] = 0
        track[start]["predecessor"] = None
        queue = [start]
        
        while queue:
            node = queue.pop(0)
            for neighbor in self.data[node]:
                if track[neighbor]["color"] == "W":
                    track[neighbor]["color"] = "G"
                    track[neighbor]["distance"] = track[node]["distance"] + 1
                    track[neighbor]["predecessor"] = node
                    queue.append(neighbor)
                track[node]["color"] = "B"
        self.bfs = track
        print(track)

    """
    Print out the vertices on a shortest path from s to v, assumming that BFS has
    already computed a breadth-first tree. O(V)
    """
    def print_path(self, start, v):
        if v == start:
            print(start)
        elif self.bfs[v]["predecessor"] == None:
            print("No path from {} to {} exists".format(start, v))
        else:
            self.print_path(start, self.bfs[v]["predecessor"])
            print(v)

    """
    Depth_first_search (DFS): once vertex's edges have been explored, the search will
    backtrack to explore edges leaving the vertex from which was discovered. The process
    continues until we have discovered all the vertices from the original source vertex
    O(V+E)
    """
    def depth_first_search(self): 
        track = {i: {"color": "W",
                     "predecessor": None,
                     "discovery": None,
                     "finish": None} for i in self.data}
        time = 0
        for i in self.data:
            if track[i]["color"] == "W":
                time = self.dfs_visit(i, track, time)
        self.dfs = track

    # nb is neighbor, v is vertex
    def dfs_visit(self, v, track, time):
        time += 1
        track[v]["discovery"] = time
        track[v]["color"] = "G"
        print(v, " discovery time: ", time)

        for nb in self.data[v]:
            if track[nb]["color"] == "W":
                track[nb]["predecessor"] = v
                time = self.dfs_visit(nb, track, time)
        
        time += 1
        track[v]["color"] = "B"
        track[v]["finish"] = time
        self.topo_sort.insert(0, v)
        print(v, " finish time: ", time)
        return time

    """
    There are 4 types of edges in depth-first forests:
    1. Tree edges: an edge from predecessor vertex to successor neighbor, say in 
    (v, n), n was first discovered from v
    2. Back edges: connect vertex to its ancestor neighbor (neighbor should be gray
    which was discovered before by other node)
    3. Forward edges: a non-tree edge connect vertex to descendant neighbor in a dfs
    (neighbor's discovery time must after vertex's discovery time)
    4. Cross edges: other edges
    """
    def depth_first_search_print(self):
        track = {i: {"color": "W",
                     "predecessor": None,
                     "discovery": None,
                     "finish": None} for i in self.data}
        time = 0
        for i in self.data:
            if track[i]["color"] == "W":
                time = self.dfs_visit_print(i, track, time)

    # nb is neighbor, v is vertex
    def dfs_visit_print(self, v, track, time):
        time += 1
        track[v]["discovery"] = time
        track[v]["color"] = "G"

        for nb in self.data[v]:
            if track[nb]["color"] == "W":
                print("{} and {} is a tree edge".format(v, nb))
                track[nb]["predecessor"] = v
                time = self.dfs_visit_print(nb, track, time)
            elif track[nb]["color"] == "G":
                print("{} and {} is a back edge".format(v, nb))
            elif (track[nb]["discovery"] > track[v]["discovery"]): 
                print("{} and {} is a forward edge".format(v, nb))
            else:
                print("{} and {} is a cross edge".format(v, nb))

        time += 1
        track[v]["color"] = "B"
        track[v]["finish"] = time
        return time

    """
    Topological_sort: a linear ordering of all its vertices such that if graph
    contains an edge (u, v) then u appears before v in the ordering.
    It takes O(V+E) for depth first search and O(1) to insert the |V| vertices onto
    the front of linked list, so total O(V+E)
    """
    def topological_sort(self):
        if not self.dfs:
            self.depth_first_search()
        for i in self.topo_sort:
            print(i)
    
    """
    Simple_path: O(V+E): returns the number of simple paths from u to v. We can do it
    by rechecking the vertices spreading to v, until reach vertex u. To avoid subproblems
    we can take the advantage of topo-sort, since there is only possible path from u to v 
    """
    def simple_path(self, u, v):
        try:
            start = self.topo_sort.index(u)
            end = self.topo_sort.index(v)
        except ValueError:
            print("{} or {} is not the name of vertices".format(u, v))
        if end <= start:
            return 0
        path = {self.topo_sort[i]: None for i in range(start, end + 1)}
        path[v] = 1
        #print("path: ", path)
        return self.simple_path_aid(path, start, end)

    def simple_path_aid(self, path, index, end):
        if index > end:
            return 0
        elif path[self.topo_sort[index]]:
            return path[self.topo_sort[index]]
        else:
            path[self.topo_sort[index]] = 0
            for nb in self.data[self.topo_sort[index]]:
                i = self.topo_sort.index(nb)
                path[self.topo_sort[index]] += self.simple_path_aid(path, i, end)
                #print(nb, ": ", path[self.topo_sort[index]])
            return path[self.topo_sort[index]]

    def __repr__(self):
        return "\n".join(["{}: {}".format(i, self.data[i]) for i in self.data])
    
    def __str__(self):
        return self.__repr__()
    

tests = []
tests.append({
    "vertices": 5,
    "edges": [(0, 1), (0, 4), (1, 4), (1, 3), (1, 2), (2, 3), (3, 4)],
    "directed": False
})

tests.append({
    "vertices": 8,
    "edges": [(0, 1), (1, 2), (2, 3), (3, 4), (3, 5), (4, 5), (4, 6), (5, 6), (5, 7), (6, 7)],
    "directed": False
})

tests.append({
    "vertices": 6,
    "edges": [(0, 1), (0, 3), (3, 1), (1, 2), (2, 3), (4, 2), (4, 5), (5, 5)],
    "directed": True
})

tests.append({
    "vertices": 8,
    "edges": [(0, 1), (0, 4), (1, 2), (1, 4), (2, 3), (3, 1), 
              (4, 3), (5, 6), (5, 7), (6, 0), (6, 4), (7, 5), (7, 6)],
    "directed": True
})

tests.append({
    "vertices": 9,
    "edges": [("undershorts", "pants"), ("pants", "belt"), ("undershorts", "shoes"), 
              ("pants", "shoes"), ("socks", "shoes"), ("shirt", "tie"), ("shirt", "belt"),
              ("tie", "jacket"), ("belt", "jacket")],
    "directed": True,
    "vertex_name": ["shirt", "tie", "jacket", "belt", "watch", 
                    "undershorts", "pants", "shoes", "socks"]
})

tests.append({
    "vertices": 14,
    "edges": [("m", "q"), ("m", "r"), ("m", "x"), ("n", "o"), ("n", "q"), ("n", "u"), ("o", "r"),
              ("o", "s"), ("o", "v"), ("p", "o"), ("p", "s"), ("p", "z"), ("q", "t"), ("r", "u"), 
              ("r", "y"), ("s", "r"), ("u", "t"), ("v", "w"), ("v", "x"), ("w", "z"), ("y", "v")],
    "directed": True,
    "vertex_name": ["m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
})

graph1 = Graph(tests[0]["vertices"], tests[0]["edges"])
graph2 = Graph(tests[1]["vertices"], tests[1]["edges"])
graph3 = Graph(tests[2]["vertices"], tests[2]["edges"], tests[2]["directed"])
graph4 = Graph(tests[3]["vertices"], tests[3]["edges"], tests[3]["directed"])
graph5 = Graph(tests[4]["vertices"], tests[4]["edges"], tests[4]["directed"], tests[4]["vertex_name"])
graph6 = Graph(tests[5]["vertices"], tests[5]["edges"], tests[5]["directed"], tests[5]["vertex_name"])

# print(graph1)
# print(graph2)
# print("bfs: ")
# graph2.breadth_first_search(2)
# print("print bfs path: ")
# graph2.print_path(7, 4)
# print("test dfs print: ")
# graph3.depth_first_search_print()
# print("test dfs print: ")
# graph4.depth_first_search_print()

# print("objects graph: ")
# print(graph5)
# print("Topological sort: ")
# graph5.topological_sort()

print(graph6)
graph6.topological_sort()
print(graph6.topo_sort)
print(graph6.simple_path('p', 'v'))