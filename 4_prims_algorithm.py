class Prims:

    def __init__(self, graph, total_nodes):
        self.nodes = total_nodes
        self.graph = graph
        self.visited = [0] * total_nodes

    def __prims__(self):
        self.visited[0] = True
        edge = 0
        x, y = 0, 0
        inf = 1000
        result = []
        while edge < self.nodes - 1:
            minimum = inf
            for i in range(self.nodes):
                if self.visited[i]:
                    for j in range(self.nodes):
                        if not self.visited[j] and self.graph[i][j]:
                            if minimum > self.graph[i][j]:
                                minimum = self.graph[i][j]
                                x, y = i, j
            self.visited[y] = True
            edge += 1
            result.append([x, y, minimum])

        for i, j, k in result:
            print(f'{i} -> {j}, weight: {k}')


if __name__ == "__main__":
    g = [[0, 9, 75, 0, 0], [9, 0, 95, 19, 42], [75, 95, 0, 51, 66], [0, 19, 51, 0, 31], [0, 42, 66, 31, 0]]
    prims = Prims(g, len(g))
    prims.__prims__()
