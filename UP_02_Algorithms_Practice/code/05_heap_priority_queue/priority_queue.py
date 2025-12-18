"""
Задание 16: Приоритетная очередь
Используя heap, реализовать:
push(value, priority),
pop() — всегда возвращает элемент с минимальным приоритетом.
Применить к задаче:
планирование задач (task scheduling),
поиск k минимальных элементов массива.
"""

import heapq


class PriorityQueue:
    """
    Приоритетная очередь на основе мин-кучи heapq.
    """

    def __init__(self):  # ← ИСПРАВЛЕНО: было init
        self._heap = []
        self._counter = 0

    def push(self, value, priority):
        """Добавление элемента с приоритетом."""
        heapq.heappush(self._heap, (priority, self._counter, value))
        self._counter += 1

    def pop(self):
        """Извлечение элемента с наименьшим приоритетом."""
        if not self._heap:
            raise IndexError("Priority queue is empty")
        priority, _, value = heapq.heappop(self._heap)
        return value

    def is_empty(self):
        return len(self._heap) == 0

    def size(self):
        return len(self._heap)


def task_scheduling():
    """Планирование задач по приоритету."""
    print("=== Планирование задач ===")

    pq = PriorityQueue()
    tasks = [
        ("Отправить email", 3),
        ("Срочный багфикс", 1),
        ("Митинг команды", 2),
        ("Обед", 5),
        ("Код-ревью", 2)
    ]

    print("Задачи в порядке добавления:")
    for task, priority in tasks:
        pq.push(task, priority)
        print(f"  Добавлена: '{task}' (приоритет: {priority})")

    print("\nВыполнение в порядке приоритета:")
    while not pq.is_empty():
        task = pq.pop()
        print(f"  → Выполняется: '{task}'")


def find_k_smallest_elements(arr, k):
    """
    Поиск k минимальных элементов массива.
    Сложность: O(n log k)
    """
    if k >= len(arr):
        return sorted(arr)

    # Используем макс-кучу (через отрицание)
    heap = []
    for num in arr:
        if len(heap) < k:
            heapq.heappush(heap, -num)
        elif -heap[0] > num:
            heapq.heapreplace(heap, -num)

    return sorted(-x for x in heap)


def test_priority_queue():
    """Тестирование приоритетной очереди."""
    print("=== Приоритетная очередь ===")

    pq = PriorityQueue()
    pq.push("низкий", 10)
    pq.push("высокий", 1)
    pq.push("средний", 5)

    print("Извлечение по приоритету:")
    while not pq.is_empty():
        print(f"  {pq.pop()}")

    print("\nПоиск 3 наименьших элементов:")
    arr = [10, 4, 2, 8, 1, 9, 3]
    k = 3
    result = find_k_smallest_elements(arr, k)
    print(f"  Массив: {arr}")
    print(f"  {k} наименьших: {result}")


if __name__ == "__main__":
    print("\n" + "=" * 80)
    print("ЗАДАНИЕ 16: ПРИОРИТЕТНАЯ ОЧЕРЕДЬ")
    print("=" * 80)
    test_priority_queue()
    task_scheduling()
    print("\n" + "=" * 80)
    print("РАБОТА ЗАВЕРШЕНА УСПЕШНО")
    print("=" * 80)