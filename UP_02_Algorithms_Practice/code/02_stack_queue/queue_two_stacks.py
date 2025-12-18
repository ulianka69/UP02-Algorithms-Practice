"""
Задание 6.2: Очередь на двух стеках
Реализация очереди FIFO с использованием двух стеков LIFO.
"""


class QueueTwoStacks:
    """
    Очередь, реализованная с использованием двух стеков.

    Принцип работы:
    - stack_in: для добавления элементов (enqueue)
    - stack_out: для извлечения элементов (dequeue)

    Когда stack_out пуст, перекидываем все из stack_in в stack_out.
    Это инвертирует порядок (LIFO → FIFO).
    """

    def __init__(self):
        """Инициализация очереди. Сложность: O(1)"""
        self.stack_in = []   # Стек для добавления
        self.stack_out = []  # Стек для извлечения

    def enqueue(self, item):
        """
        Добавление элемента в очередь.
        Сложность: O(1)
        """
        self.stack_in.append(item)

    def dequeue(self):
        """
        Извлечение элемента из очереди.
        Амортизированная сложность: O(1)
        """
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")

        if not self.stack_out:
            self._transfer()

        return self.stack_out.pop()

    def _transfer(self):
        """
        Перемещение всех элементов из stack_in в stack_out.
        Сложность: O(n), но редко вызывается.
        """
        while self.stack_in:
            self.stack_out.append(self.stack_in.pop())

    def peek(self):
        """
        Просмотр первого элемента без удаления.
        Сложность: O(1) амортизированно
        """
        if self.is_empty():
            raise IndexError("Peek from empty queue")

        if not self.stack_out:
            self._transfer()

        return self.stack_out[-1]

    def is_empty(self):
        """Проверка пустоты очереди. Сложность: O(1)"""
        return not self.stack_in and not self.stack_out

    def size(self):
        """Размер очереди. Сложность: O(1)"""
        return len(self.stack_in) + len(self.stack_out)

    def __str__(self):
        """Строковое представление очереди."""
        return f"QueueTwoStacks(in={self.stack_in}, out={self.stack_out})"


# Минимальная реализация CircularQueue для сравнения
class CircularQueue:
    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("Capacity must be positive")
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0
        self.rear = -1
        self.size_val = 0

    def enqueue(self, item):
        if self.size_val == self.capacity:
            raise OverflowError("Queue is full")
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item
        self.size_val += 1

    def dequeue(self):
        if self.size_val == 0:
            raise IndexError("Dequeue from empty queue")
        item = self.queue[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size_val -= 1
        return item

    def is_empty(self):
        return self.size_val == 0


def test_queue_two_stacks():
    """Тестирование очереди на двух стеках."""
    print("=== Очередь на двух стеках ===")

    queue = QueueTwoStacks()

    # 1. Базовые операции
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    print(f"1. После enqueue(10, 20, 30): {queue}")

    print(f"   peek(): {queue.peek()}")
    print(f"   dequeue(): {queue.dequeue()}")
    print(f"   После dequeue: {queue}")

    # 2. Последовательность операций
    print("\n2. Последовательность операций:")
    print(f"   Исходное состояние: {queue}")

    queue.enqueue(40)
    print(f"   enqueue(40): {queue}")

    print(f"   dequeue(): {queue.dequeue()}")  # 20
    print(f"   Состояние: {queue}")

    print(f"   dequeue(): {queue.dequeue()}")  # 30
    print(f"   Состояние: {queue}")

    print(f"   dequeue(): {queue.dequeue()}")  # 40
    print(f"   Состояние: {queue}")
    print(f"   is_empty? {queue.is_empty()}")

    # 3. Чередование операций
    print("\n3. Чередование операций:")
    queue2 = QueueTwoStacks()
    for i in range(5):
        queue2.enqueue(i * 100)
        if i % 2 == 0:
            dequeued = queue2.dequeue()
            print(f"   enqueue({i * 100}), dequeue()={dequeued}: {queue2}")


def compare_queue_implementations():
    """Сравнение реализаций очереди."""
    print("\n" + "=" * 70)
    print("СРАВНЕНИЕ РЕАЛИЗАЦИЙ ОЧЕРЕДИ")
    print("=" * 70)

    import time
    n = 5000

    # Циклическая очередь
    start = time.time()
    circ_queue = CircularQueue(n + 10)
    for i in range(n):
        circ_queue.enqueue(i)
    for _ in range(n):
        circ_queue.dequeue()
    circ_time = time.time() - start

    # Очередь на двух стеках
    start = time.time()
    stack_queue = QueueTwoStacks()
    for i in range(n):
        stack_queue.enqueue(i)
    for _ in range(n):
        stack_queue.dequeue()
    stack_time = time.time() - start

    # Очередь на списке (плохая)
    start = time.time()
    simple_queue = []
    for i in range(n):
        simple_queue.append(i)
    for _ in range(n):
        simple_queue.pop(0)
    simple_time = time.time() - start

    print(f"\nПроизводительность (n={n}):")
    print(f"  Циклическая очередь:     {circ_time:.6f} сек")
    print(f"  Очередь на двух стеках:  {stack_time:.6f} сек")
    print(f"  Очередь на списке:       {simple_time:.6f} сек")

    print("\nВывод:")
    print("  • Очередь на двух стеках — гибкая и простая реализация")
    print("  • Циклическая очередь — самая быстрая при известном размере")
    print("  • НИКОГДА не используйте pop(0) в реальном коде!")


# ЗАПУСК ПРОГРАММЫ
if __name__ == "__main__":
    print("\n" + "=" * 80)
    print("ЗАДАНИЕ 6.2: ОЧЕРЕДЬ НА ДВУХ СТЕКАХ")
    print("=" * 80)

    test_queue_two_stacks()
    compare_queue_implementations()

    print("\n" + "=" * 80)
    print("РАБОТА ЗАВЕРШЕНА УСПЕШНО")
    print("=" * 80)