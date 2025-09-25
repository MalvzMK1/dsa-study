from typing import overload
from abc import ABC, abstractmethod

class BaseGraph(ABC):
    def __init__(self, size) -> None:
        self._size = size
        self._vertex_data = [''] * size
        self._adj_matrix = [[0] * size for _ in range(size)]

    @overload
    def add_edge(self, x: int, y: int) -> None: ...
    @overload
    def add_edge(self, x: int, y: int, weight: int) -> None: ...

    @abstractmethod
    def add_edge(self, x, y, weight=None):
        ...

    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self._size:
            self._vertex_data[vertex] = data

    def print_data(self):
        for idx, vertex in enumerate(self._vertex_data):
            print(f'Vertex {idx}: {vertex}')
        print("\nAdjacency Matrix")
        for row in self._adj_matrix:
            print(' '.join(map(str, row)))


class UndirectedGraph(BaseGraph):
    def __init__(self, size) -> None:
        super().__init__(size)

    def add_edge(self, x, y, weight=None):
        if 0 <= x < self._size and 0 <= y < self._size:
            self._adj_matrix[x][y] = 1
            self._adj_matrix[y][x] = 1


class DirectedWeightedGraph(BaseGraph):
    def __init__(self, size) -> None:
        super().__init__(size)

    def add_edge(self, x, y, weight=None):
        if 0 <= x < self._size and 0 <= y < self._size:
            self._adj_matrix[x][y] = weight if weight is not None else 1


# Teste
print("Undirected:")
ug = UndirectedGraph(4)
ug.add_vertex_data(0, 'A')
ug.add_vertex_data(1, 'B')
ug.add_vertex_data(2, 'C')
ug.add_vertex_data(3, 'D')

ug.add_edge(0, 1)
ug.add_edge(1, 2)
ug.add_edge(0, 2)
ug.add_edge(0, 3)

ug.print_data()

print("\nDirected Weighted:")
dg = DirectedWeightedGraph(4)
dg.add_vertex_data(0, 'A')
dg.add_vertex_data(1, 'B')
dg.add_vertex_data(2, 'C')
dg.add_edge(0, 1, 5)
dg.add_edge(0, 2, 7)
dg.print_data()
