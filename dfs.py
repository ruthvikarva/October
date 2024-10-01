# dfs.py

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]

    # Function to add an edge to the graph
    def add_edge(self, u, v):
        self.graph[u].append(v)

    # Recursive function to print DFS traversal
    def dfs_util(self, vertex, visited):
        visited[vertex] = True  # Mark the vertex as visited
        print(vertex, end=" ")  # Process the vertex

        # Recur for all adjacent vertices
        for neighbor in self.graph[vertex]:
            if not visited[neighbor]:
                self.dfs_util(neighbor, visited)

    # The DFS function that uses the above utility
    def dfs(self, start_vertex):
        visited = [False] * self.V  # Mark all vertices as not visited
        self.dfs_util(start_vertex, visited)


# Driver program to test DFS
g = Graph(6)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 4)
g.add_edge(3, 5)
g.add_edge(4, 5)

print("Depth-First Search starting from vertex 0:")
g.dfs(0)
