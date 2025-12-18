"""
Задание 13.2: Алгоритмы на графах
Реализация алгоритмов обхода графов:
1. Поиск в ширину (BFS)
2. Поиск в глубину (DFS)
3. Поиск кратчайшего пути в невзвешенном графе (BFS)
"""

from collections import deque


class GraphAlgorithms:
    """Класс с алгоритмами на графах."""

    @staticmethod
    def bfs(graph, start_vertex):
        """Поиск в ширину (BFS)."""
        if not hasattr(graph, 'adj_list') or start_vertex >= len(graph.adj_list):
            return []

        visited = [False] * len(graph.adj_list)
        result = []
        queue = deque([start_vertex])
        visited[start_vertex] = True

        while queue:
            current = queue.popleft()
            result.append(current)
            for neighbor, _ in graph.adj_list[current]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        return result

    @staticmethod
    def dfs(graph, start_vertex):
        """Поиск в глубину (DFS) - рекурсивный."""
        if not hasattr(graph, 'adj_list') or start_vertex >= len(graph.adj_list):
            return []

        visited = [False] * len(graph.adj_list)
        result = []

        def dfs_recursive(vertex):
            visited[vertex] = True
            result.append(vertex)
            for neighbor, _ in graph.adj_list[vertex]:
                if not visited[neighbor]:
                    dfs_recursive(neighbor)

        dfs_recursive(start_vertex)
        return result

    @staticmethod
    def dfs_iterative(graph, start_vertex):
        """Поиск в глубину (DFS) - итеративный."""
        if not hasattr(graph, 'adj_list') or start_vertex >= len(graph.adj_list):
            return []

        visited = [False] * len(graph.adj_list)
        result = []
        stack = [start_vertex]

        while stack:
            current = stack.pop()
            if not visited[current]:
                visited[current] = True
                result.append(current)
                for neighbor, _ in reversed(graph.adj_list[current]):
                    if not visited[neighbor]:
                        stack.append(neighbor)
        return result

    @staticmethod
    def shortest_path_unweighted(graph, start_vertex, end_vertex):
        """Кратчайший путь в невзвешенном графе."""
        if (not hasattr(graph, 'adj_list') or
            start_vertex >= len(graph.adj_list) or
            end_vertex >= len(graph.adj_list)):
            return []

        if start_vertex == end_vertex:
            return [start_vertex]

        visited = [False] * len(graph.adj_list)
        parent = [-1] * len(graph.adj_list)
        queue = deque([start_vertex])
        visited[start_vertex] = True

        while queue:
            current = queue.popleft()
            if current == end_vertex:
                path = []
                while current != -1:
                    path.append(current)
                    current = parent[current]
                return path[::-1]

            for neighbor, _ in graph.adj_list[current]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    parent[neighbor] = current
                    queue.append(neighbor)
        return []

    @staticmethod
    def connected_components(graph):
        """Поиск компонент связности."""
        if not hasattr(graph, 'adj_list'):
            return []

        visited = [False] * len(graph.adj_list)
        components = []

        for vertex in range(len(graph.adj_list)):
            if not visited[vertex]:
                component = []
                queue = deque([vertex])
                visited[vertex] = True

                while queue:
                    current = queue.popleft()
                    component.append(current)
                    for neighbor, _ in graph.adj_list[current]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            queue.append(neighbor)
                components.append(component)
        return components


# ========== ВСПОМОГАТЕЛЬНЫЙ КЛАСС ==========
class GraphAdjacencyList:
    """Простая реализация списка смежности для тестов."""
    def __init__(self, num_vertices: int, directed: bool = False):
        self.num_vertices = num_vertices
        self.directed = directed
        self.adj_list = [[] for _ in range(num_vertices)]

    def add_edge(self, u: int, v: int, weight: int = 1):
        if 0 <= u < self.num_vertices and 0 <= v < self.num_vertices:
            self.adj_list[u].append((v, weight))
            if not self.directed and u != v:
                self.adj_list[v].append((u, weight))


# ========== ТЕСТЫ ==========
def test_graph_algorithms():
    """Тестирование алгоритмов на графах."""
    print("=== Алгоритмы на графах ===")

    graph = GraphAdjacencyList(7, directed=False)
    edges = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (2, 6), (3, 4), (5, 6)]
    for u, v in edges:
        graph.add_edge(u, v)

    print("1. BFS от вершины 0:", GraphAlgorithms.bfs(graph, 0))
    print("2. DFS от вершины 0:", GraphAlgorithms.dfs(graph, 0))

    path = GraphAlgorithms.shortest_path_unweighted(graph, 0, 6)
    print(f"3. Кратчайший путь 0→6: {path}")


def visualize_graph_traversal():
    """Визуализация обходов."""
    print("\n=== Визуализация обходов ===")
    print("Граф 'домик': вершины 0-4")
    # Простая демонстрация
    graph = GraphAdjacencyList(5, directed=False)
    edges = [(0,1), (0,2), (1,2), (1,3), (2,3), (2,4), (3,4)]
    for u, v in edges:
        graph.add_edge(u, v)

    print("BFS от 0:", GraphAlgorithms.bfs(graph, 0))
    print("DFS от 0:", GraphAlgorithms.dfs(graph, 0))


def benchmark_graph_algorithms():
    """Бенчмарк алгоритмов."""
    print("\n=== Бенчмарк (упрощенный) ===")
    print("BFS и DFS: O(n + m) время")
    print("Память: BFS использует очередь, DFS - стек")


# ========== ЗАПУСК ПРОГРАММЫ ==========
if __name__ == "__main__":
    print("\n" + "=" * 80)
    print("ЗАДАНИЕ 13.2: АЛГОРИТМЫ НА ГРАФАХ")
    print("=" * 80)

    test_graph_algorithms()
    visualize_graph_traversal()
    benchmark_graph_algorithms()

    print("\n" + "=" * 80)
    print("РАБОТА ЗАВЕРШЕНА УСПЕШНО")
    print("=" * 80)