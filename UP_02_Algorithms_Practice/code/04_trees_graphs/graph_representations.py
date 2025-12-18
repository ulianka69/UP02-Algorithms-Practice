"""
Задание 13.1: Хранение графов
Реализация различных представлений графов:
1. Матрица смежности
2. Список смежности
"""


class GraphAdjacencyMatrix:
    """Граф, представленный матрицей смежности."""

    def __init__(self, num_vertices: int, directed: bool = False):
        """Инициализация графа с n вершинами."""
        self.num_vertices = num_vertices
        self.directed = directed
        self.matrix = [[0] * num_vertices for _ in range(num_vertices)]

    def add_edge(self, u: int, v: int, weight: int = 1):
        """Добавление ребра между вершинами u и v."""
        if 0 <= u < self.num_vertices and 0 <= v < self.num_vertices:
            self.matrix[u][v] = weight
            if not self.directed:
                self.matrix[v][u] = weight

    def remove_edge(self, u: int, v: int):
        """Удаление ребра."""
        if 0 <= u < self.num_vertices and 0 <= v < self.num_vertices:
            self.matrix[u][v] = 0
            if not self.directed:
                self.matrix[v][u] = 0

    def has_edge(self, u: int, v: int) -> bool:
        """Проверка наличия ребра. Сложность: O(1)"""
        if 0 <= u < self.num_vertices and 0 <= v < self.num_vertices:
            return self.matrix[u][v] != 0
        return False

    def get_neighbors(self, vertex: int):
        """Получение соседей вершины. Сложность: O(n)"""
        neighbors = []
        if 0 <= vertex < self.num_vertices:
            for v in range(self.num_vertices):
                if self.matrix[vertex][v] != 0:
                    neighbors.append((v, self.matrix[vertex][v]))
        return neighbors

    def get_degree(self, vertex: int) -> int:
        """Степень вершины."""
        if not self.directed:
            return len(self.get_neighbors(vertex))
        else:
            degree = 0
            if 0 <= vertex < self.num_vertices:
                for v in range(self.num_vertices):
                    if self.matrix[vertex][v] != 0:
                        degree += 1
            return degree

    def __str__(self):
        """Строковое представление матрицы."""
        lines = ["Матрица смежности:"]
        lines.append("   " + " ".join(str(i) for i in range(self.num_vertices)))
        for i in range(self.num_vertices):
            row = [str(self.matrix[i][j]) for j in range(self.num_vertices)]
            lines.append(f"{i}: " + " ".join(row))
        return "\n".join(lines)


class GraphAdjacencyList:
    """Граф, представленный списком смежности."""

    def __init__(self, num_vertices: int, directed: bool = False):
        """Инициализация графа."""
        self.num_vertices = num_vertices
        self.directed = directed
        self.adj_list = [[] for _ in range(num_vertices)]

    def add_edge(self, u: int, v: int, weight: int = 1):
        """Добавление ребра."""
        if 0 <= u < self.num_vertices and 0 <= v < self.num_vertices:
            self.adj_list[u].append((v, weight))
            if not self.directed and u != v:
                self.adj_list[v].append((u, weight))

    def remove_edge(self, u: int, v: int):
        """Удаление ребра."""
        if 0 <= u < self.num_vertices and 0 <= v < self.num_vertices:
            self.adj_list[u] = [(neighbor, w) for neighbor, w in self.adj_list[u] if neighbor != v]
            if not self.directed:
                self.adj_list[v] = [(neighbor, w) for neighbor, w in self.adj_list[v] if neighbor != u]

    def has_edge(self, u: int, v: int) -> bool:
        """Проверка наличия ребра. Сложность: O(deg(u))"""
        if 0 <= u < self.num_vertices:
            for neighbor, _ in self.adj_list[u]:
                if neighbor == v:
                    return True
        return False

    def get_neighbors(self, vertex: int):
        """Получение соседей вершины."""
        if 0 <= vertex < self.num_vertices:
            return self.adj_list[vertex]
        return []

    def get_degree(self, vertex: int) -> int:
        """Степень вершины."""
        return len(self.adj_list[vertex]) if 0 <= vertex < self.num_vertices else 0

    def __str__(self):
        """Строковое представление списка смежности."""
        lines = ["Список смежности:"]
        for i in range(self.num_vertices):
            neighbors = ", ".join(f"{v}({w})" for v, w in self.adj_list[i])
            lines.append(f"  {i}: [{neighbors}]")
        return "\n".join(lines)


# ========== ФУНКЦИИ ВНЕ КЛАССОВ ==========

def compare_graph_representations():
    """Сравнение матрицы смежности и списка смежности."""
    print("=== Сравнение представлений графов ===")

    n = 6
    edges = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 4), (3, 4), (4, 5)]

    graph_matrix = GraphAdjacencyMatrix(n, directed=False)
    graph_list = GraphAdjacencyList(n, directed=False)

    for u, v in edges:
        graph_matrix.add_edge(u, v)
        graph_list.add_edge(u, v)

    print("\nМатрица смежности:")
    print(graph_matrix)
    print("\nСписок смежности:")
    print(graph_list)

    print("\nПроверка операций:")
    for u, v in [(0, 1), (0, 3)]:
        matrix_check = graph_matrix.has_edge(u, v)
        list_check = graph_list.has_edge(u, v)
        print(f"  Ребро ({u}, {v}): матрица={matrix_check}, список={list_check}")


def create_example_graphs():
    """Создание примеров графов."""
    print("\n" + "=" * 50)
    print("ПРИМЕРЫ ГРАФОВ")
    print("=" * 50)

    graph = GraphAdjacencyList(4, directed=False)
    graph.add_edge(0, 1)
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    print("Простой граф:")
    print(graph)


def test_graph_operations():
    """Тестирование операций с графами."""
    print("\n" + "=" * 50)
    print("ТЕСТИРОВАНИЕ ОПЕРАЦИЙ")
    print("=" * 50)

    graph = GraphAdjacencyList(3, directed=False)
    graph.add_edge(0, 1)
    graph.add_edge(1, 2)
    print("После добавления ребер:")
    print(graph)

    graph.remove_edge(0, 1)
    print("После удаления ребра (0,1):")
    print(graph)


# ========== ЗАПУСК ПРОГРАММЫ ==========
if __name__ == "__main__":
    print("\n" + "=" * 80)
    print("ЗАДАНИЕ 13.1: ГРАФЫ (ПРЕДСТАВЛЕНИЯ)")
    print("=" * 80)

    compare_graph_representations()
    create_example_graphs()
    test_graph_operations()

    print("\n" + "=" * 80)
    print("РАБОТА ЗАВЕРШЕНА УСПЕШНО")
    print("=" * 80)