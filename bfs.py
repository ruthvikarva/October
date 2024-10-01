# bfs.py
from collections import deque

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]

    # Function to add an edge to the graph
    def add_edge(self, u, v):
        self.graph[u].append(v)

    # Function to print BFS traversal from a given source
    def bfs(self, start_vertex):
        visited = [False] * self.V  # Mark all vertices as not visited
        queue = deque([start_vertex])  # Create a queue for BFS

        visited[start_vertex] = True  # Mark the source node as visited

        while queue:
            vertex = queue.popleft()  # Dequeue a vertex
            print(vertex, end=" ")  # Process the vertex

            # Get all adjacent vertices of the dequeued vertex
            # If an adjacent vertex has not been visited, mark it as visited and enqueue it
            for neighbor in self.graph[vertex]:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True


# Driver program to test BFS
g = Graph(6)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 4)
g.add_edge(3, 5)
g.add_edge(4, 5)

print("Breadth-First Search starting from vertex 0:")
g.bfs(0)
