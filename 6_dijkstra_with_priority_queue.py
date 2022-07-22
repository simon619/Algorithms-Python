class Vertex:

    def __init__(self, vertex, weight=0):
        self.vertex = vertex
        self.weight = weight


class Dijkstra:

    def __init__(self, graph, n):
        self.adj_list = [[] for i in range(n)]
        self.priority_que = []
        for (source, destination, weight) in graph:
            self.adj_list[source].append((destination, weight))
        print(f'Adjacency List: {self.adj_list}')
        print('')

    def __dijkstra__(self, source):

        def __heapify__(priority_que, n, pointer):  # Min Heap
            minimum = pointer
            left, right = 2 * pointer + 1, 2 * pointer + 2

            if left < n and priority_que[left].weight < priority_que[minimum].weight:
                minimum = left

            if right < n and priority_que[right].weight < priority_que[minimum].weight:
                minimum = right

            if minimum != pointer:
                priority_que[minimum], priority_que[pointer] = priority_que[pointer], priority_que[minimum]
                __heapify__(priority_que, n, minimum)

        def __insert__(node):
            if not self.priority_que:
                self.priority_que.append(node)

            else:
                self.priority_que.append(node)
                for i in range(len(self.priority_que) // 2 - 1, -1, -1):
                    __heapify__(self.priority_que, len(self.priority_que), i)

        def __delete__():
            if not self.priority_que:
                print("Not Possible")
                return None

            else:
                self.priority_que[0], self.priority_que[len(self.priority_que) - 1] = self.priority_que[len(self.priority_que) - 1], self.priority_que[0]
                temp = self.priority_que[len(self.priority_que) - 1]
                del self.priority_que[-1]
                for i in range(len(self.priority_que) // 2 - 1, -1, -1):
                    __heapify__(self.priority_que, len(self.priority_que), i)
                return temp

        __insert__(Vertex(source))
        distance = [9999] * len(self.adj_list)
        distance[source] = 0
        visited = [False] * len(self.adj_list)
        visited[source] = True
        previous_vertex = [-1] * len(self.adj_list)

        while self.priority_que:
            current_vertex = __delete__()
            current_vertex = current_vertex.vertex
            for (neighbor, weight) in self.adj_list[current_vertex]:
                if not visited[neighbor] and (distance[current_vertex] + weight) < distance[neighbor]:
                    distance[neighbor] = distance[current_vertex] + weight
                    previous_vertex[neighbor] = current_vertex
                    __insert__(Vertex(neighbor, weight))
            visited[current_vertex] = True

        def __traversal__(prev, i, n):
            if i >= 0:
                __traversal__(prev, prev[i], n)
                path.append(i)

        path = []
        for neighbor in range(len(self.adj_list)):
            if neighbor != source and distance[neighbor] != 9999:
                __traversal__(previous_vertex, neighbor, len(self.adj_list))
                print(f'Source: {source} -> Destination: {neighbor}, Cost: {distance[neighbor]}, Route: {path}')
                path.clear()


if __name__ == '__main__':
    G = [[0, 1, 10], [0, 4, 3], [1, 2, 2], [1, 4, 4], [2, 3, 9], [3, 2, 7], [4, 1, 1], [4, 2, 8], [4, 3, 2]]
    number_of_vertices = 5
    dk = Dijkstra(G, number_of_vertices)
    for source in range(number_of_vertices):
        print(f'Current Source: {source}')
        dk.__dijkstra__(source)
        print('')
