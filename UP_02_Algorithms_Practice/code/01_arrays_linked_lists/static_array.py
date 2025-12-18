"""
Задание 1: Статический массив
Реализация статического массива фиксированного размера с основными операциями.
Оценка трудоемкости в Big O нотации.
"""


class StaticArray:
    """
    Класс статического массива с фиксированной емкостью.

    Особенности:
    - Емкость задается при создании и не меняется
    - Все операции имеют предсказуемую сложность
    - При переполнении выбрасывается исключение
    """

    def __init__(self, capacity: int):
        """
        Инициализация статического массива.

        Сложность: O(1) (с учётом O(capacity) на выделение памяти)
        """
        if capacity <= 0:
            raise ValueError("Capacity must be positive")

        self.capacity = capacity  # Максимальное количество элементов
        self.data = [None] * capacity  # Память под элементы
        self.size = 0  # Текущее количество элементов

    def pushBack(self, value) -> None:
        """
        Добавление элемента в конец массива.
        Сложность: O(1)
        """
        if self.size >= self.capacity:
            raise IndexError(f"Array overflow: capacity={self.capacity}, size={self.size}")

        self.data[self.size] = value
        self.size += 1

    def pushFront(self, value) -> None:
        """
        Добавление элемента в начало массива.
        Сложность: O(n)
        """
        if self.size >= self.capacity:
            raise IndexError(f"Array overflow: capacity={self.capacity}")

        for i in range(self.size, 0, -1):
            self.data[i] = self.data[i - 1]

        self.data[0] = value
        self.size += 1

    def insert(self, index: int, value) -> None:
        """
        Вставка элемента по указанному индексу.
        Сложность: O(n)
        """
        if self.size >= self.capacity:
            raise IndexError("Array is full")
        if index < 0 or index > self.size:
            raise IndexError(f"Index {index} out of bounds [0, {self.size}]")

        if index == self.size:
            self.pushBack(value)
            return

        for i in range(self.size, index, -1):
            self.data[i] = self.data[i - 1]

        self.data[index] = value
        self.size += 1

    def remove(self, index: int):
        """
        Удаление элемента по индексу.
        Сложность: O(n)
        Возвращает: удаленный элемент
        """
        if index < 0 or index >= self.size:
            raise IndexError(f"Index {index} out of bounds [0, {self.size - 1}]")

        removed_value = self.data[index]

        for i in range(index, self.size - 1):
            self.data[i] = self.data[i + 1]

        self.data[self.size - 1] = None
        self.size -= 1

        return removed_value

    def find(self, value) -> int:
        """
        Поиск элемента по значению.
        Сложность: O(n)
        Возвращает: индекс или -1
        """
        for i in range(self.size):
            if self.data[i] == value:
                return i
        return -1

    def __str__(self) -> str:
        """Строковое представление массива."""
        elements = [str(self.data[i]) for i in range(self.size)]
        return "[" + ", ".join(elements) + "]" + f" (size={self.size}, capacity={self.capacity})"

    def __len__(self) -> int:
        """Текущий размер массива."""
        return self.size

    def __getitem__(self, index: int):
        """Доступ к элементу по индексу. Сложность: O(1)."""
        if index < 0 or index >= self.size:
            raise IndexError(f"Index {index} out of bounds")
        return self.data[index]

    def __setitem__(self, index: int, value):
        """Изменение элемента по индексу. Сложность: O(1)."""
        if index < 0 or index >= self.size:
            raise IndexError(f"Index {index} out of bounds")
        self.data[index] = value


def test_static_array():
    """Тестирование статического массива."""
    print("=== Тестирование статического массива ===")

    # 1. Создание массива
    arr = StaticArray(5)
    print(f"1. Создан массив: {arr}")

    # 2. Добавление в конец
    arr.pushBack(10)
    arr.pushBack(20)
    arr.pushBack(30)
    print(f"2. После pushBack 10, 20, 30: {arr}")

    # 3. Добавление в начало
    arr.pushFront(5)
    print(f"3. После pushFront 5: {arr}")

    # 4. Вставка по индексу
    arr.insert(2, 15)
    print(f"4. После insert(2, 15): {arr}")

    # 5. Поиск элемента
    index = arr.find(20)
    print(f"5. Поиск 20: индекс = {index}")

    # 6. Удаление элемента
    removed = arr.remove(1)
    print(f"6. Удален элемент с индексом 1: {removed}")
    print(f"   Массив после удаления: {arr}")

    # 7. Доступ по индексу
    print(f"7. Элемент с индексом 0: {arr[0]}")
    arr[0] = 1
    print(f"   После arr[0] = 1: {arr}")

    # 8. Попытка переполнения
    try:
        arr.pushBack(40)
        arr.pushBack(50)
        arr.pushBack(60)  # Должно вызвать ошибку
    except IndexError as e:
        print(f"8. Ожидаемая ошибка при переполнении: {e}")

    print(f"   Финальный массив: {arr}")


# ЗАПУСК ПРОГРАММЫ
if __name__ == "__main__":
    print("\n" + "=" * 80)
    print("ЗАДАНИЕ 1: СТАТИЧЕСКИЙ МАССИВ")
    print("=" * 80)

    test_static_array()

    print("\n" + "=" * 60)
    print("СВОДКА ПО ТРУДОЕМКОСТИ ОПЕРАЦИЙ СТАТИЧЕСКОГО МАССИВА:")
    print("=" * 60)
    print("pushBack(value)      : O(1)  - добавление в конец")
    print("pushFront(value)     : O(n)  - добавление в начало")
    print("insert(index, value) : O(n)  - вставка по индексу")
    print("remove(index)        : O(n)  - удаление по индексу")
    print("find(value)          : O(n)  - поиск по значению")
    print("__getitem__[index]   : O(1)  - доступ по индексу")
    print("__setitem__[index]   : O(1)  - изменение по индексу")
    print("=" * 60)