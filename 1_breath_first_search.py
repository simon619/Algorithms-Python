class AVL:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1


class BFSOnAVLTree:
    def __creation__(self, node, data):
        if node is None:
            return AVL(data)
        elif node.data > data:
            node.left = self.__creation__(node.left, data)
        elif node.data < data:
            node.right = self.__creation__(node.right, data)

        node.height = self.__height__(node)
        balance = self.__height__(node.left) - self.__height__(node.right)

        if balance > 1:
            if node.left.data > data:
                return self.__right_rotation__(node)
            else:
                node.left = self.__left_rotation__(node.left)
                return self.__right_rotation__(node)
        elif balance < -1:
            if node.right.data < data:
                return self.__left_rotation__(node)
            else:
                node.right = self.__right_rotation__(node.left)
                return self.__left_rotation__(node)

        return node

    def __height__(self, node):
        if node is None:
            return 0
        else:
            left = self.__height__(node.left)
            right = self.__height__(node.right)
            return 1 + max(left, right)

    def __right_rotation__(self, node):
        temp1 = node.left
        temp2 = temp1.right
        temp1.right = node
        node.left = temp2
        node.height = self.__height__(node)
        temp1.height = self.__height__(temp1)
        return temp1

    def __left_rotation__(self, node):
        temp1 = node.right
        temp2 = temp1.left
        temp1.left = node
        node.right = temp2
        node.height = self.__height__(node)
        temp1.height = self.__height__(temp1)
        return temp1

    def __noorder_traversal__(self, node):
        current_node = node
        q = [current_node]

        def __traversal__(q, traversal):
            if q:
                info = q.pop(0)
                traversal += str(info.data) + '->'
                if info.left:
                    q.append(info.left)
                if info.right:
                    q.append(info.right)
                traversal = __traversal__(q, traversal)
            return traversal

        result = __traversal__(q, '')
        return result

    def __breath_first_search__(self, node):
        queue = []
        visited = []
        queue.append(node)
        visited.append(node.data)

        while queue:
            x = queue.pop(0)
            print(x.data)

            if x.left:
                queue.append(x.left)
                if x.left.data not in visited:
                    visited.append(x.left.data)
            if x.right:
                queue.append(x.right)
                if x.right.data not in visited:
                    visited.append(x.right.data)

        return visited


if __name__ == '__main__':
    avl = BFSOnAVLTree()
    root = None
    list = [60, 50, 70, 40, 35, 45, 55, 65, 75]
    #                      50
    #                    /    \
    #                 40        60                     This is after applying AVL
    #               /    \    /    \
    #            35      45  55     70
    #                             /    \
    #                            65    75

    for i in list:
        root = avl.__creation__(root, i)
    result = avl.__noorder_traversal__(root)
    print(f'Traversed: {result}')
    print('Breath First Search:')
    result = avl.__breath_first_search__(root)
    print(f'Traversed in  Breath First Search: {result}')
