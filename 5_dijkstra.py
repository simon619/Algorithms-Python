class Dijkstra:

    def __init__(self, graph):
        self.graph = graph
        self.visited = []

    def __dijkstra__(self):
        self.visited.append([False, 0])
        for vertex in range(len(self.graph[0]) - 1):
            self.visited.append([False, 99999])

        def __find_next_vertex__():
            current_vertex = None
            for vertex in range(len(self.graph[0])):
                if not self.visited[vertex][0] and (current_vertex is None or self.visited[current_vertex][1] >= self.visited[vertex][1]):
                    current_vertex = vertex
            return current_vertex

        node = 0
        while node < len(self.graph[0]):
            current_node = __find_next_vertex__()
            for neighbor_vertex in range(len(self.graph[0])):
                if self.graph[current_node][neighbor_vertex] and not self.visited[neighbor_vertex][0]:
                    new_cost = self.visited[current_node][1] + self.graph[current_node][neighbor_vertex]
                    if new_cost < self.visited[neighbor_vertex][1]:
                        self.visited[neighbor_vertex][1] = new_cost
                self.visited[current_node][0] = True
            node += 1

    def __print__(self):
        for vertex in range(len(self.visited)):
            print(f'0 -> {vertex}, Cost: {self.visited[vertex][1]}')


if __name__ == "__main__":
    G = [[0, 0, 1, 2, 0, 0, 0],
         [0, 0, 2, 0, 0, 3, 0],
         [1, 2, 0, 1, 3, 0, 0],
         [2, 0, 1, 0, 0, 0, 1],
         [0, 0, 3, 0, 0, 2, 0],
         [0, 3, 0, 0, 2, 0, 1],
         [0, 0, 0, 1, 0, 1, 0]]
    dk = Dijkstra(G)
    dk.__dijkstra__()
    print("Shortest Path: ")
    dk.__print__()

