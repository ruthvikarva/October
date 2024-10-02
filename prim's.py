# prims.py

import sys

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    # Function to find the vertex with minimum key value from the set of vertices not yet included in the MST
    def min_key(self, key, mst_set):
        min = sys.maxsize
        min_index = -1

        for v in range(self.V):
            if key[v] < min and not mst_set[v]:
                min = key[v]
                min_index = v

        return min_index

    # Function to construct and print the MST using Prim's algorithm
    def prim_mst(self):
        key = [sys.maxsize] * self.V  # Initialize keys with infinity
        parent = [None] * self.V  # Array to store the constructed MST
        key[0] = 0  # Start from the first vertex
        mst_set = [False] * self.V  # Vertices not yet included in MST

        parent[0] = -1  # The first node is always the root of the MST

        for _ in range(self.V):
            u = self.min_key(key, mst_set)
            mst_set[u] = True  # Add the picked vertex to the MST set

            # Update key values and parent index of the adjacent vertices
            for v in range(self.V):
                if self.graph[u][v] > 0 and not mst_set[v] and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        self.print_mst(parent)

    # Utility function to print the constructed MST
    def print_mst(self, parent):
        print("Edge \tWeight")
        for i in range(1, self.V):
            print(parent[i], "-", i, "\t", self.graph[i][parent[i]])


# Driver code
g = Graph(5)
g.graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

g.prim_mst()
