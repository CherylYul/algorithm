# class Vertex:
#     def __init__(self, start, key, color = "W", distance = None, predecessor = None):
#         self.start = start
#         self.key = key
#         self.color = color
#         self.distance = distance
#         self.predecessor = predecessor

class Graph:
    def __init__(self, num_vertices, edges):
        self.num_vertices = num_vertices
        self.data = [[] for _ in range(num_vertices)]
        for n1, n2 in edges:
            self.data[n1].append(n2)
            self.data[n2].append(n1)
        self.bfs = None
        self.dfs = None
    
    """
    Depth_first_search (DFS): once vertex's edges have been explored, the search will
    backtrack to explore edges leaving the vertex from which was discovered. The process
    continues until we have discovered all the vertices from the original source vertex
    """
    def depth_first_search(self):
        track = [{"color": "W",
                  "predecessor": None,
                  "discovery": None,
                  "finish": None} for _ in range(self.num_vertices)]
        time = 0
        for i in range(self.num_vertices):
            if track[i]["color"] == "W":
                self.depth_first_search_visit(i, track, time)

    def depth_first_search_visit(self, vertex, track, time):
        time += 1
        track[vertex]["discovery"] = time
        track[vertex]["color"] = "G"
        for neighbor in self.data[vertex]:
            if track[neighbor]["color"] == "W":
                track[neighbor]["predecessor"] = vertex
                self.depth_first_search_visit(neighbor, track, time)
        time += 1
        track[vertex]["color"] = "B"
        track[vertex]["finish"] = time

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
        track = [{"color": "W", 
                  "distance": None,
                  "predecessor": None} for _ in range(self.num_vertices)]
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
                    print(neighbor)
                    queue.append(neighbor)
                track[node]["color"] = "B"
        self.bfs = track

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

    def __repr__(self):
        return "\n".join(["{}: {}".format(v, neighbor) for v, neighbor in enumerate(self.data)])
    
    def __str__(self):
        return self.__repr__()
    

tests = []
tests.append({
    "vertices": 5,
    "edges": [(0, 1), (0, 4), (1, 4), (1, 3), (1, 2), (2, 3), (3, 4)]
})

tests.append({
    "vertices": 8,
    "edges": [(0, 1), (1, 2), (2, 3), (3, 4), (3, 5), (4, 5), (4, 6), (5, 6), (5, 7), (6, 7)]
})

# graph1 = Graph(tests[0]["vertices"], tests[0]["edges"])
# print(graph1)
graph2 = Graph(tests[1]["vertices"], tests[1]["edges"])
print(graph2)
print("bfs: ")
graph2.breadth_first_search(2)
print("print path: ")
graph2.print_path(7, 4)