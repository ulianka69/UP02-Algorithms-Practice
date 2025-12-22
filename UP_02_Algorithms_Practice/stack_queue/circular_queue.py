"""
Задание 6.1: Очередь на циклическом массиве
Реализация FIFO структуры с использованием кольцевого буфера.
"""


class CircularQueue:
    """
    Очередь на основе циклического массива (кольцевого буфера).

    Принцип FIFO (First In, First Out):
    - Первый добавленный элемент извлекается первым
    - Элементы добавляются в конец, извлекаются из начала
    """

    def __init__(self, capacity: int):
        """
        Инициализация очереди.

        Args:
            capacity: максимальный размер очереди
        """
        if capacity <= 0:
            raise ValueError("Capacity must be positive")

        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0   # Индекс начала очереди
        self.rear = -1   # Индекс конца очереди (-1 = пусто)
        self.size = 0    # Текущее количество элементов

    def enqueue(self, item):
        """
        Добавление элемента в конец очереди.
        Сложность: O(1)
        """
        if self.is_full():
            raise OverflowError("Queue is full")

        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item
        self.size += 1

    def dequeue(self):
        """
        Удаление и возврат элемента из начала очереди.
        Сложность: O(1)
        """
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")

        item = self.queue[self.front]
        self.queue[self.front] = None  # Опционально: очистка для отладки
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return item

    def peek(self):
        """
        Просмотр первого элемента без удаления.
        Сложность: O(1)
        """
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        return self.queue[self.front]

    def is_empty(self):
        """Проверка пустоты очереди. Сложность: O(1)"""
        return self.size == 0

    def is_full(self):
        """Проверка заполненности очереди. Сложность: O(1)"""
        return self.size == self.capacity

    def get_size(self):
        """Текущий размер очереди. Сложность: O(1)"""
        return self.size

    def __str__(self):
        """Строковое представление очереди."""
        if self.is_empty():
            return "CircularQueue([])"

        items = []
        for i in range(self.size):
            idx = (self.front + i) % self.capacity
            items.append(str(self.queue[idx]))

        return f"CircularQueue([{', '.join(items)}])"

    def clear(self):
        """Очистка очереди. Сложность: O(1)"""
        self.front = 0
        self.rear = -1
        self.size = 0


class SimpleQueueList:
    """Простая очередь на списке (для сравнения)."""
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.items:
            raise IndexError("Dequeue from empty queue")
        return self.items.pop(0)  # O(n) — медленно!


def test_circular_queue():
    """Тестирование циклической очереди."""
    print("=== Очередь на циклическом массиве ===")

    # 1. Создание и базовые операции
    queue = CircularQueue(5)
    print(f"1. Создана очередь емкостью 5: {queue}")

    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    print(f"   После enqueue(10, 20, 30): {queue}")
    print(f"   peek(): {queue.peek()}")
    print(f"   dequeue(): {queue.dequeue()}")
    print(f"   После dequeue: {queue}")

    # 2. Кольцевое поведение
    print("\n2. Демонстрация кольцевого поведения:")

    # После dequeue у нас 2 элемента (20, 30) → можно добавить ещё 3
    for i in range(3):  # ← БЫЛО 4, СТАЛО 3
        queue.enqueue(i * 100)
        print(f"   enqueue({i * 100}): {queue}")

    # Очередь: [20, 30, 0, 100, 200] — заполнена полностью

    queue.dequeue()  # Удаляем 20 → теперь свободно 1 место
    queue.dequeue()  # Удаляем 30 → теперь свободно 2 места
    print(f"   После двух dequeue: {queue}")

    queue.enqueue(500)  # Теперь есть место!
    print(f"   enqueue(500): {queue}")

    # 3. Переполнение
    print("\n3. Проверка переполнения:")
    try:
        queue.enqueue(600)
        print("   Ошибка: должно было быть исключение!")
    except OverflowError as e:
        print(f"   ✓ Ожидаемое исключение: {e}")

    # 4. Очистка
    print("\n4. Очистка и переиспользование:")
    queue.clear()
    print(f"   После clear(): {queue}")

    queue.enqueue(999)
    print(f"   enqueue(999): {queue}")
    print(f"   is_empty? {queue.is_empty()}")
    print(f"   is_full? {queue.is_full()}")
    print(f"   size: {queue.get_size()}")

    # 5. Сводка сложности
    print("\n5. Сводка сложности операций:")
    print("   enqueue(item): O(1)")
    print("   dequeue():     O(1)")
    print("   peek():        O(1)")
    print("   is_empty():    O(1)")
    print("   is_full():     O(1)")
    print("   size():        O(1)")


def compare_with_regular_queue():
    """Сравнение циклической очереди с очередью на списке."""
    print("\n" + "=" * 70)
    print("СРАВНЕНИЕ ОЧЕРЕДЕЙ: ЦИКЛИЧЕСКИЙ МАССИВ VS СПИСОК")
    print("=" * 70)

    import time
    n = 5000  # уменьшено для быстроты

    # Циклическая очередь
    start = time.time()
    circ_queue = CircularQueue(n + 10)
    for i in range(n):
        circ_queue.enqueue(i)
    for _ in range(n):
        circ_queue.dequeue()
    circ_time = time.time() - start

    # Очередь на списке
    start = time.time()
    list_queue = SimpleQueueList()
    for i in range(n):
        list_queue.enqueue(i)
    for _ in range(n):
        list_queue.dequeue()
    list_time = time.time() - start

    print(f"\nПроизводительность (n={n}):")
    print(f"  Циклическая очередь: {circ_time:.6f} сек")
    print(f"  Очередь на списке:   {list_time:.6f} сек")
    if circ_time > 0:
        print(f"  Ускорение:           {list_time / circ_time:.1f}x")

    print("\nВывод:")
    print("  Циклическая очередь — O(1) на все операции")
    print("  Очередь на списке — O(n) на dequeue из-за pop(0)")


# ЗАПУСК ПРОГРАММЫ
if __name__ == "__main__":
    print("\n" + "=" * 80)
    print("ЗАДАНИЕ 6.1: ОЧЕРЕДЬ НА ЦИКЛИЧЕСКОМ МАССИВЕ")
    print("=" * 80)

    test_circular_queue()
    compare_with_regular_queue()

    print("\n" + "=" * 80)
    print("РАБОТА ЗАВЕРШЕНА УСПЕШНО")
    print("=" * 80)