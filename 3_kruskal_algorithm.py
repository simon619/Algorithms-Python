class Kruskal:

    def __init__(self, number):
        self.vertex = number
        self.graph = []

    def __add_vertex__(self, root, node, weight):
        self.graph.append([root, node, weight])

    def __parent_finding__(self, parent, node):
        if parent[node] == node:
            return node
        return self.__parent_finding__(parent, parent[node])

    def __union__(self, parents, rank, x, y):
        x_root = self.__parent_finding__(parents, x)
        y_root = self.__parent_finding__(parents, y)
        if rank[x_root] > rank[y_root]:
            parents[y_root] = x_root
        elif rank[x_root] < rank[y_root]:
            parents[x_root] = y_root
        else:
            rank[x_root] += 1
            parents[y_root] = x_root

    def __kruskal__(self):
        def __merge_sort__(list):
            if len(list) < 2:
                return list[:]
            else:
                mid = len(list) // 2
                left = __merge_sort__(list[:mid])
                right = __merge_sort__(list[mid:])
                return __merge__(left, right)

        def __merge__(left, right):
            merged = []
            i, j = 0, 0
            while i < len(left) and j < len(right):
                if left[i][2] < right[j][2]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1

            while i < len(left):
                merged.append(left[i])
                i += 1

            while j < len(right):
                merged.append(right[j])
                j += 1

            return merged

        self.graph = __merge_sort__(self.graph)
        print(f'Sorted graph: {self.graph}')
        result = []
        i, j = 0, 0
        parents = []
        rank = [0] * self.vertex
        for k in range(self.vertex):
            parents.append(k)
        while j < self.vertex - 1:
            u, v, w = self.graph[i]
            if i < len(self.graph):
                i += 1
            x = self.__parent_finding__(parents, u)
            y = self.__parent_finding__(parents, v)

            if x != y:
                j += 1
                result.append([u, v, w])
                self.__union__(parents, rank, x, y)

        print(f'Rank: {rank}')
        print(f'Parents: {parents}')
        for i, j, k in result:
            print(f'{i} -> {j}, weight: {k}')


if __name__ == '__main__':
    graph = Kruskal(6)
    graph.__add_vertex__(0, 1, 4)
    graph.__add_vertex__(0, 2, 4)
    graph.__add_vertex__(1, 2, 2)
    graph.__add_vertex__(1, 0, 4)
    graph.__add_vertex__(2, 0, 4)
    graph.__add_vertex__(2, 1, 2)
    graph.__add_vertex__(2, 3, 3)
    graph.__add_vertex__(2, 5, 2)
    graph.__add_vertex__(2, 4, 4)
    graph.__add_vertex__(3, 2, 3)
    graph.__add_vertex__(3, 4, 3)
    graph.__add_vertex__(4, 2, 4)
    graph.__add_vertex__(4, 3, 3)
    graph.__add_vertex__(5, 2, 2)
    graph.__add_vertex__(5, 4, 3)
    graph.__kruskal__()
