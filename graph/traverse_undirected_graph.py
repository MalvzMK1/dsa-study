class Graph:
    def __init__(self, size) -> None:
        self._size = size
        self._vertex_data = [''] * size
        self._adj_matrix = [[0] * size for _ in range(size)]

    def add_edge(self, x, y):
        if 0 <= x < self._size and 0 <= y < self._size:
            self._adj_matrix[x][y] = 1
            self._adj_matrix[y][x] = 1

    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self._size:
            self._vertex_data[vertex] = data

    def print_data(self):
        for idx, vertex in enumerate(self._vertex_data):
            print(f'Vertex {idx}: {vertex}')
        print("\nAdjacency Matrix")
        for row in self._adj_matrix:
            print(' '.join(map(str, row)))

    def __dfs_util(self, vertex, visited):
        visited[vertex] = True
        print(self._vertex_data[vertex], end=' ')

        for i in range(self._size):
            if self._adj_matrix[vertex][i] == 1 and not visited[i]:
                self.__dfs_util(i, visited)

    def dfs(self, starter_vertex: str):
        visited = [False] * self._size
        vertex = self._vertex_data.index(starter_vertex)
        self.__dfs_util(vertex, visited)
        print()

    def bfs(self, starter_vertex: str):
        queue = [self._vertex_data.index(starter_vertex)]
        visited = [False] * self._size
        visited[queue[0]] = True

        while queue:
            current_node = queue.pop(0)
            print(self._vertex_data[current_node], end=' ')

            for i in range(self._size):
                if self._adj_matrix[current_node][i] == 1 and not visited[i]:
                    queue.append(i)
                    visited[i] = True

def main():
    g = Graph(7)
    
    g.add_vertex_data(0, 'A')
    g.add_vertex_data(1, 'B')
    g.add_vertex_data(2, 'C')
    g.add_vertex_data(3, 'D')
    g.add_vertex_data(4, 'E')
    g.add_vertex_data(5, 'F')
    g.add_vertex_data(6, 'G')
    
    g.add_edge(3, 0)  # D - A
    g.add_edge(0, 2)  # A - C
    g.add_edge(0, 3)  # A - D
    g.add_edge(0, 4)  # A - E
    g.add_edge(4, 2)  # E - C
    g.add_edge(2, 5)  # C - F
    g.add_edge(2, 1)  # C - B
    g.add_edge(2, 6)  # C - G
    g.add_edge(1, 5)  # B - F
    
    g.print_data()

    print('\nTraversing DFS')
    g.dfs('D')

    print('\nTraversing BFS')
    g.bfs('D')
    print()

if __name__ == "__main__":
    main()

