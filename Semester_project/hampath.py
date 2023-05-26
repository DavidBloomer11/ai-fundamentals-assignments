class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.edge_list = []

    def append_edge(self, edge_node):
        self.edge_list.append(edge_node)

    def get_edges(self):
        return self.edge_list


class Grid:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.grid = []
        self.__create_grid()


    def __create_grid(self):
        for x in range(self.x):
            for y in range(self.y):
                node = Node(x, y)
                if x > 0:
                    node.append_edge(self.grid[(x - 1) * self.y + y])  # Left edge
                if y > 0:
                    node.append_edge(self.grid[x * self.y + (y - 1)])  # Top edge
                if x < self.x - 1:
                    node.append_edge(self.grid[(x + 1) * self.y + y])  # Right edge
                if y < self.y - 1:
                    node.append_edge(self.grid[x * self.y + (y + 1)])  # Bottom edge
                self.grid.append(node)


grid = Grid(5,5)

print(grid.grid)