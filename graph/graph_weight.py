from random import random
from random import choice
import heapdict as heapdict
import time
import matplotlib
import numpy as np
import matplotlib.pyplot as plt


class Vertex:
    def __init__(self, vertex):
        self.value = vertex
        self.inNeighbors = []
        self.outNeighbors = []
        self.inWeight = []
        self.outWeight = []

        self.reWeight = []
        self.preDistance = None
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
    def __init__(self, directed=True):
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

    def get_weight_matrix(self):
        n = len(self.vertices)
        W = [[None for _ in range(n)] for _ in range(n)]
        for i in range(n):
            v = self.vertices[i]
            W[i][i] = 0
            for nb, w in list(zip(v.outNeighbors, v.outWeight)):
                j = self.vertices.index(nb)
                W[i][j] = w
        return W

    """
    Bellman-Ford algorithm: solves the single-source shortest-paths problem in the
    general case in which edges can have negative weight O(VE)
    - Returns true if it is a negative-weight cycle so that no solution exists
    - Returns false if it doesn't have a negative-weight cycle, then produces shortest
    paths and their weights
    """

    def initialize_single_source(self, s):  # O(V)
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

    def Disjkstra_heap(self, s):
        self.initialize_single_source(s)
        Q = heapdict.heapdict()
        for v in self.vertices:
            Q[v] = v.distance
        while Q:
            v, pos = Q.popitem()
            if v.distance == float("inf"):
                return
            for nb, w in list(zip(v.outNeighbors, v.outWeight)):
                if v.distance + w < nb.distance:
                    nb.distance = v.distance + w
                    nb.predecessor = v
                    Q[nb] = v.distance + w  # update the key in heapdict
        print(self.get_distance())

    def Disjkstra_heap_reweight(self, s):
        self.initialize_single_source(s)
        Q = heapdict.heapdict()
        for v in self.vertices:
            Q[v] = v.distance
        while Q:
            v, pos = Q.popitem()
            if v.distance == float("inf"):
                return
            for nb, w in list(zip(v.outNeighbors, v.reWeight)):
                if v.distance + w < nb.distance:
                    nb.distance = v.distance + w
                    nb.predecessor = v
                    Q[nb] = v.distance + w  # update the key in heapdict
        print(self.get_distance())

    """
    All pairs shortest paths (APSP) are based on the similarities of matrix in graph
    and matrix multiplication in dynamic programming:
    - Slow all pairs shortest paths: O(V^4) times
    - Faster all pairs shortest paths: take advantages of positive graph O(V^3logV)
    """

    def faster_all_pairs_shortest_paths(self):
        W = self.get_weight_matrix()
        L = [W]
        n = len(self.vertices)
        i = 1
        while i < n - 1:
            L.append(self.extend_shortest_paths(W, L[-1]))
            i *= 2
        return L[-1]

    def slow_all_pairs_shortest_paths(self):
        W = self.get_weight_matrix()
        L = [W]
        n = len(self.vertices)
        for _ in range(1, n - 1):
            L.append(self.extend_shortest_paths(W, L[-1]))
        return L[-1]

    def extend_shortest_paths(self, W, L):
        n = len(self.vertices)
        L_next = [[L[r][c] for c in range(n)] for r in range(n)]
        for r in range(n):
            for c in range(n):
                if r != c:
                    for k in range(n):
                        compare = L_next[r][c]
                        if not compare:
                            compare = float("inf")
                        if W[k][c] and L[r][k]:
                            L_next[r][c] = min(compare, L[r][k] + W[k][c])
        return L_next

    """
    Floyd-Warshall algorithm O(V^3): APSP
    """

    def FLOYD_WARSHALL(self):
        D = [self.get_weight_matrix()]
        n = len(self.vertices)
        for k in range(n):
            # D.append(D[-1])
            D_next = [[D[-1][r][c] for c in range(n)] for r in range(n)]
            D.append(D_next)
            for i in range(n):
                for j in range(n):
                    if i != j:
                        compare = D[k][i][j]
                        if not D[k][i][j]:
                            compare = float("inf")
                        if D[k][i][k] and D[k][k][j]:
                            D[k + 1][i][j] = min(compare, D[k][i][k] + D[k][k][j])
        return D[-1]

    """
    Transitive closure: check if there is a path from vertex i to j in the graph, 
    then construct a reach-ability matrix O(V^3)
    """

    def transitive_closure(self):
        n = len(self.vertices)
        t = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i == j or (self.vertices[j] in self.vertices[i].outNeighbors):
                    t[i][j] = 1
        T = [t]
        for k in range(n):
            t = [[T[-1][r][c] for c in range(n)] for r in range(n)]
            for i in range(n):
                for j in range(n):
                    t[i][j] = 1 if (t[i][j] or (t[i][k] and t[k][j])) else 0
            T.append(t)
        return T

    """
    Johnson's algorithm (APSP) O(V^2logV + VE), which is faster than Floyd Warshall
    - Returns a matrix of shortest path weights for all pairs of vertices
    - Reports if the input graph contains a negative cycles
    
    1. Add a new single source, then find the shortest path by Bellman Ford, the shortest
    path to any source must be equal or smaller than 0
    2. Reweighting the graph so that there is no negative edges: 
        new_edge = old_edge + tail_shortest_path - head_shortest_path
    3. Compute all the shortest path using Disjkstra
    4. Return the shortest path matrix:
        shortest_path = shortest_path_Disjkstra - tail_shortest_path + head_shortest_path
    """

    def Johnson(self):
        self.vertices.append(Vertex("source"))
        n = len(self.vertices)
        source = self.vertices[n - 1]
        for i in range(n - 1):
            self.add_directed_edge(source, self.vertices[i], 0)
        if not self.Bellman_Ford(source):
            print("The graph contains a negative weight cycles!")
        else:
            self.vertices.pop()
            for v in self.vertices:
                v.preDistance = v.distance
                for nb, w in list(zip(v.outNeighbors, v.outWeight)):
                    v.reWeight.append(w + v.distance - nb.distance)
                print(v.reWeight)
            D = []
            for v in self.vertices:
                self.Disjkstra_heap_reweight(v)
                D_next = []
                for u in self.vertices:
                    D_next.append(u.distance - v.preDistance + u.preDistance)
                D.append(D_next)
            return D

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
tests.append(
    {
        "graph": 0,
        "vertices": ["s", "t", "x", "y", "z"],
        "edges": [
            ("s", "t", 6),
            ("s", "y", 7),
            ("t", "x", 5),
            ("t", "y", 8),
            ("t", "z", -4),
            ("x", "t", -2),
            ("y", "x", -3),
            ("y", "z", 9),
            ("z", "s", 2),
            ("z", "x", 7),
        ],
        "index": [
            (0, 1, 6),
            (0, 3, 7),
            (1, 2, 5),
            (1, 3, 8),
            (1, 4, -4),
            (2, 1, -2),
            (3, 2, -3),
            (3, 4, 9),
            (4, 0, 2),
            (4, 2, 7),
        ],
        "DAG": False,
        "negative": True,
    }
)

tests.append(
    {
        "graph": 1,
        "vertices": ["r", "s", "t", "x", "y", "z"],
        "edges": [
            ("r", "s", 5),
            ("r", "t", 3),
            ("s", "t", 2),
            ("s", "x", 6),
            ("t", "x", 7),
            ("t", "y", 4),
            ("t", "z", 2),
            ("x", "y", -1),
            ("x", "z", 1),
            ("y", "z", -2),
        ],
        "index": [
            (0, 1, 5),
            (0, 2, 3),
            (1, 2, 2),
            (1, 3, 6),
            (2, 3, 7),
            (2, 4, 4),
            (2, 5, 2),
            (3, 4, -1),
            (3, 5, 1),
            (4, 5, -2),
        ],
        "DAG": True,
        "negative": True,
    }
)

tests.append(
    {
        "graph": 2,
        "vertices": ["s", "t", "x", "y", "z"],
        "edges": [
            ("s", "t", 10),
            ("s", "y", 5),
            ("t", "x", 1),
            ("t", "y", 2),
            ("x", "z", 4),
            ("y", "t", 3),
            ("y", "x", 9),
            ("y", "z", 2),
            ("z", "s", 7),
            ("z", "x", 6),
        ],
        "index": [
            (0, 1, 10),
            (0, 3, 5),
            (1, 2, 1),
            (1, 3, 2),
            (2, 4, 4),
            (3, 1, 3),
            (3, 2, 9),
            (3, 4, 2),
            (4, 0, 7),
            (4, 2, 6),
        ],
        "DAG": False,
        "negative": False,
    }
)

tests.append(
    {
        "graph": 3,
        "vertices": [1, 2, 3, 4, 5],
        "edges": [
            (1, 2, 3),
            (1, 3, 8),
            (1, 5, -4),
            (2, 4, 1),
            (2, 5, 7),
            (3, 2, 4),
            (4, 1, 2),
            (4, 3, -5),
            (5, 4, 6),
        ],
        "index": [
            (0, 1, 3),
            (0, 2, 8),
            (0, 4, -4),
            (1, 3, 1),
            (1, 4, 7),
            (2, 1, 4),
            (3, 0, 2),
            (3, 2, -5),
            (4, 3, 6),
        ],
        "DAG": False,
        "negative": True,
    }
)

tests.append(
    {
        "graph": 4,
        "vertices": [0, 1, 2, 3],
        "edges": [(1, 2), (1, 3), (2, 1), (3, 0), (3, 2)],
        "index": [(1, 2), (1, 3), (2, 1), (3, 0), (3, 2)],
        "DAG": False,
        "negative": False,
    }
)

tests.append(
    {
        "graph": 5,
        "vertices": [1, 2, 3, 4, 5],
        "edges": [
            (1, 2, 3),
            (1, 3, 8),
            (1, 5, -4),
            (2, 4, 1),
            (2, 5, 7),
            (3, 2, 4),
            (4, 1, 2),
            (4, 3, -5),
            (5, 4, 6),
        ],
        "index": [
            (0, 1, 3),
            (0, 2, 8),
            (0, 4, -4),
            (1, 3, 1),
            (1, 4, 7),
            (2, 1, 4),
            (3, 0, 2),
            (3, 2, -5),
            (4, 3, 6),
        ],
        "DAG": False,
        "negative": False,
    }
)


# n vertices with p probability and set of weights
def random_graph(n, p, weights=[1]):
    G = Graph()
    V = [Vertex(x) for x in range(n)]
    for v in V:
        G.add_vertex(v)
    for v1 in V:
        for v2 in V:
            if v1 != v2:
                if random() < p:
                    G.add_directed_edge(v1, v2, w=choice(weights))
    return G


def run_trials(fn, n_vertices, p, numTrials=25):
    nValues = []
    tValues = []
    for n in n_vertices:
        # run fn several times and average to get a decent idea.
        runtime = 0
        for t in range(numTrials):
            G = random_graph(n, p)  # Random graph on n vertices with p
            start = time.time()
            if fn == "dijkstra_array":
                G.Dijkstra(G.vertices[0])
            if fn == "dijkstrac_heap":
                G.Disjkstra_heap(G.vertices[0])
            end = time.time()
            runtime += (end - start) * 1000  # measure in milliseconds
        runtime = runtime / numTrials
        nValues.append(n)
        tValues.append(runtime)
    return nValues, tValues


def test_plot():
    n_vertices = [10, 50, 100, 150, 200, 300]
    nDijkstraArray, tDijkstraArray = run_trials("dijkstra_array", n_vertices, 0.2)
    nDijkstraHeap, tDijkstraHeap = run_trials("dijkstra_heap", n_vertices, 0.2)
    plt.plot(
        nDijkstraArray,
        tDijkstraArray,
        "-.",
        color="blue",
        label="Dijkstra with an array",
    )
    plt.plot(
        nDijkstraHeap, tDijkstraHeap, "--", color="orange", label="Dijkstra with a heap"
    )
    plt.xlabel("n")
    plt.ylabel("Time(ms)")
    plt.legend()
    plt.title("Shortest paths on a graph with n vertices and about 5n edges")
    plt.show()


def simple_test():
    for test in tests:
        if test["graph"] != 4:
            print(
                "===============Testing Graph {} ===============".format(test["graph"])
            )
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

            print("Test 5: Matrix Weight")
            print(G.get_weight_matrix())

            print("Test 6: Slow All Pairs Shortest Paths")
            result = G.slow_all_pairs_shortest_paths()
            for i in result:
                print(i)

            print("Test 7: APSP Floyd Warshall")
            result = G.FLOYD_WARSHALL()
            for i in result:
                print(i)

            print("Test 8: Johnson")
            if test["negative"]:
                print(G.Johnson())


def transitive_closure():
    G = Graph()
    for v in tests[4]["vertices"]:
        G.add_vertex(Vertex(v))
    for (
        v1,
        v2,
    ) in tests[
        4
    ]["index"]:
        G.add_directed_edge(G.vertices[v1], G.vertices[v2])
    print(G.transitive_closure())


simple_test()
# transitive_closure()
# python3 graph/graph_weight.py
