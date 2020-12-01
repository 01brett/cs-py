"""
Simple graph implementation
"""
from util import Stack, Queue


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Non-existent vertex")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue()
        visited = set()

        q.enqueue(starting_vertex)  # init

        while q.size() > 0:  # while our queue isn't empty
            vertex = q.dequeue()

            if vertex not in visited:
                print(vertex)  # "visit" the vertex (node)
                visited.add(vertex)

                for neighbor in self.get_neighbors(vertex):
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack()
        visited = set()

        s.push(starting_vertex)

        while s.size() > 0:
            vertex = s.pop()

            if vertex not in visited:
                print(vertex)  # "visit" the vertex (node)
                visited.add(vertex)

                for neighbor in self.get_neighbors(vertex):
                    s.push(neighbor)

    def dft_recursive(self, vertex, visited=set()):
        if vertex in visited:
            return

        print(vertex)
        visited.add(vertex)

        for neighbor in self.get_neighbors(vertex):
            self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        q = Queue()
        q.enqueue([starting_vertex])

        visited = set()

        while q.size() > 0:
            path = q.dequeue()
            last_vertex = path[-1]

            if last_vertex == destination_vertex:
                return path

            visited.add(last_vertex)

            for neighbor in self.get_neighbors(last_vertex):
                # don't even add the neighbor if we've been there
                if neighbor not in visited:
                    next_path = path.copy()
                    next_path.append(neighbor)
                    q.enqueue(next_path)

    def dfs(self, starting_vertex, destination_vertex):
        s = Stack()
        s.push([starting_vertex])

        visited = set()

        while s.size() > 0:
            path = s.pop()
            last_vertex = path[-1]

            if last_vertex == destination_vertex:
                return path

            visited.add(last_vertex)

            for neighbor in self.get_neighbors(last_vertex):
                if neighbor not in visited:
                    next_path = path.copy()
                    next_path.append(neighbor)
                    s.push(next_path)

    def dfs_recursive(self, vertex, target, visited=None, path=None):
        if visited is None:
            visited = set()

        if path is None:
            path = []

        visited.add(vertex)
        path = path + [vertex]

        if vertex == target:
            return path

        for neighbor in self.get_neighbors(vertex):
            if neighbor not in visited:
                print("~", path)
                found = self.dfs_recursive(neighbor, target, visited, path)
                if found:
                    return found


if __name__ == "__main__":
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    """
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    """
    # print(graph.vertices)

    """
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7 -
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    """
    # graph.bft(1)

    """
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7 -recursive
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5 -
        1, 2, 4, 6, 3, 5, 7
    """
    # graph.dft(1)
    # graph.dft_recursive(1)

    """
    Valid BFS path:
        [1, 2, 4, 6]
    """
    # print(graph.bfs(1, 6))

    """
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    """
    # print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
