"""
Задание 15: Куча
Реализовать бинарную мин-кучу:
вставку,
извлечение минимума,
построение кучи из массива.
Проверить корректность свойств кучи после каждой операции.
"""


class MinHeap:
    """
    Бинарная мин-куча на основе списка.
    """

    def __init__(self):  # ← ИСПРАВЛЕНО: было init
        self.heap = []

    def _parent(self, i):
        return (i - 1) // 2

    def _left_child(self, i):
        return 2 * i + 1

    def _right_child(self, i):
        return 2 * i + 2

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _heapify_up(self, i):
        """Восстановление свойства кучи вверх."""
        while i > 0 and self.heap[self._parent(i)] > self.heap[i]:
            self._swap(i, self._parent(i))
            i = self._parent(i)

    def _heapify_down(self, i):
        """Восстановление свойства кучи вниз."""
        smallest = i
        left = self._left_child(i)
        right = self._right_child(i)

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != i:
            self._swap(i, smallest)
            self._heapify_down(smallest)

    def insert(self, value):
        """Вставка значения. Сложность: O(log n)"""
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def extract_min(self):
        """Извлечение минимума. Сложность: O(log n)"""
        if not self.heap:
            raise IndexError("Heap is empty")

        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def build_heap(self, array):
        """Построение кучи из массива. Сложность: O(n)"""
        self.heap = array[:]
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self._heapify_down(i)

    def is_valid(self):
        """Проверка корректности свойств кучи."""
        for i in range(len(self.heap)):
            left = self._left_child(i)
            right = self._right_child(i)
            if left < len(self.heap) and self.heap[i] > self.heap[left]:
                return False
            if right < len(self.heap) and self.heap[i] > self.heap[right]:
                return False
        return True

    def __str__(self):  # ← ИСПРАВЛЕНО: было str
        return f"MinHeap({self.heap})"


def test_min_heap():
    """Тестирование мин-кучи."""
    print("=== Мин-куча ===")

    # 1. Вставка
    heap = MinHeap()
    values = [5, 3, 8, 1, 4, 6]
    print("1. Вставка значений:", values)
    for v in values:
        heap.insert(v)
        print(f"   После вставки {v}: {heap}")
        assert heap.is_valid(), "Нарушено свойство кучи!"

    # 2. Извлечение минимума
    print("\n2. Извлечение минимумов:")
    while heap.heap:
        min_val = heap.extract_min()
        print(f"   Извлечено: {min_val}, остаток: {heap}")
        if heap.heap:
            assert heap.is_valid(), "Нарушено свойство кучи после извлечения!"

    # 3. Построение кучи из массива
    print("\n3. Построение кучи из массива:")
    array = [10, 5, 3, 8, 1, 9]
    heap.build_heap(array)
    print(f"   Исходный массив: {array}")
    print(f"   Куча: {heap}")
    assert heap.is_valid(), "Нарушено свойство кучи при построении!"


if __name__ == "__main__":
    print("\n" + "=" * 80)
    print("ЗАДАНИЕ 15: КУЧА")
    print("=" * 80)
    test_min_heap()
    print("\n" + "=" * 80)
    print("РАБОТА ЗАВЕРШЕНА УСПЕШНО")
    print("=" * 80)