"""
Задание 2: Динамический массив
Реализация динамического массива с автоматическим расширением (стратегия ×2).
"""

import time


class StaticArray:
    """Статический массив из задания 1 (нужен для сравнения)"""

    def init(self, capacity: int):
        if capacity <= 0:
            raise ValueError("Capacity must be positive")
        self.capacity = capacity
        self.data = [None] * capacity
        self.size = 0

    def pushBack(self, value) -> None:
        if self.size >= self.capacity:
            raise IndexError(f"Array overflow: capacity={self.capacity}, size={self.size}")
        self.data[self.size] = value
        self.size += 1

    def len(self):
        return self.size

    def str(self):
        elements = []
        for i in range(self.size):
            elements.append(str(self.data[i]))
        return "[" + ", ".join(elements) + "]" + f" (size={self.size}, capacity={self.capacity})"


class DynamicArray:
    """
    Динамический массив с автоматическим расширением.

    Особенности:
    - Начинается с малой емкости (например, 1)
    - При заполнении увеличивает емкость в 2 раза
    - Амортизированная сложность pushBack: O(1)
    """

    def __init__(self, initial_capacity: int = 1):
        """
        Инициализация динамического массива.

        Сложность: O(1)
        """
        if initial_capacity <= 0:
            initial_capacity = 1

        self.capacity = initial_capacity
        self.data = [None] * self.capacity
        self.size = 0

    def _resize(self, new_capacity: int) -> None:
        """
        Изменение размера массива.

        Сложность: O(n), где n = текущий размер
        """
        new_data = [None] * new_capacity

        for i in range(self.size):
            new_data[i] = self.data[i]

        self.data = new_data
        self.capacity = new_capacity

    def pushBack(self, value) -> None:
        """
        Добавление элемента в конец с автоматическим расширением.

        Амортизированная сложность: O(1)
        """
        if self.size == self.capacity:
            self._resize(self.capacity * 2)

        self.data[self.size] = value
        self.size += 1

    def pushFront(self, value) -> None:
        """
        Добавление элемента в начало.

        Сложность: O(n)
        """
        if self.size == self.capacity:
            self._resize(self.capacity * 2)

        for i in range(self.size, 0, -1):
            self.data[i] = self.data[i - 1]

        self.data[0] = value
        self.size += 1

    def __str__(self) -> str:
        """Строковое представление."""
        elements = []
        for i in range(self.size):
            elements.append(str(self.data[i]))
        return "[" + ", ".join(elements) + "]" + f" (size={self.size}, capacity={self.capacity})"

    def __len__(self) -> int:
        return self.size

    def __getitem__(self, index: int):
        if index < 0 or index >= self.size:
            raise IndexError(f"Index {index} out of bounds")
        return self.data[index]


def benchmark_insertion(n_elements: int = 100000):
    """
    Сравнение времени вставки N элементов в статический и динамический массивы.
    """
    print(f"\n{'=' * 70}")
    print(f"БЕНЧМАРК: Вставка {n_elements:,} элементов".replace(',', ' '))
    print('=' * 70)

    # ========== СТАТИЧЕСКИЙ МАССИВ ==========
    print("\n1. СТАТИЧЕСКИЙ МАССИВ (емкость = N):")
    print("-" * 40)

    try:
        static_arr = StaticArray(n_elements)
        start_time = time.time()

        for i in range(n_elements):
            static_arr.pushBack(i)

        static_time = time.time() - start_time
        print(f"   ✓ Успешно! Время: {static_time:.6f} секунд")
        print(f"   ✓ Размер: {len(static_arr)}, Емкость: {static_arr.capacity}")

    except Exception as e:
        print(f"   ✗ Ошибка: {e}")
        static_time = None

    # ========== СТАТИЧЕСКИЙ МАССИВ (малая емкость) ==========
    print("\n2. СТАТИЧЕСКИЙ МАССИВ (емкость = N/10 для демонстрации ошибки):")
    print("-" * 40)

    try:
        small_capacity = max(1, n_elements // 10)
        static_arr_small = StaticArray(small_capacity)
        start_time = time.time()

        inserted = 0
        for i in range(n_elements):
            try:
                static_arr_small.pushBack(i)
                inserted += 1
            except IndexError:
                break

        small_time = time.time() - start_time
        print(f"   ✗ Ожидаемая ошибка при переполнении")
        print(f"   ✗ Время до ошибки: {small_time:.6f} секунд")
        print(f"   ✗ Успешно добавлено: {inserted} элементов из {n_elements}")

    except Exception as e:
        print(f"   Ошибка: {e}")

    # ========== ДИНАМИЧЕСКИЙ МАССИВ ==========
    print("\n3. ДИНАМИЧЕСКИЙ МАССИВ (начальная емкость = 1):")
    print("-" * 40)

    dynamic_arr = DynamicArray(initial_capacity=1)
    start_time = time.time()

    for i in range(n_elements):
        dynamic_arr.pushBack(i)

    dynamic_time = time.time() - start_time

    print(f"   ✓ Успешно! Время: {dynamic_time:.6f} секунд")
    print(f"   ✓ Размер: {len(dynamic_arr):,}".replace(',', ' '))
    print(f"   ✓ Финальная емкость: {dynamic_arr.capacity:,}".replace(',', ' '))

    # Подсчет количества расширений
    expansions = 0
    capacity = 1
    while capacity < dynamic_arr.capacity:
        capacity *= 2
        expansions += 1

    print(f"   ✓ Количество расширений: {expansions}")

    # ========== СРАВНЕНИЕ ==========
    print("\n" + "=" * 70)
    print("СРАВНИТЕЛЬНАЯ ТАБЛИЦА:")
    print("=" * 70)

    if static_time is not None and dynamic_time is not None:
        print(f"{'Параметр':<30} {'Статический':<15} {'Динамический':<15}")
        print(f"{'-' * 30} {'-' * 15} {'-' * 15}")
        print(f"{'Время (сек)':<30} {static_time:<15.6f} {dynamic_time:<15.6f}")
        print(f"{'Относительная скорость':<30} {'1.0x':<15} {static_time / dynamic_time:<15.2f}x")
        print(f"{'Успешных операций':<30} {n_elements:<15} {n_elements:<15}")
        print(f"{'Память (емкость)':<30} {n_elements:<15} {dynamic_arr.capacity:<15}")

        print("\nВЫВОДЫ:")
        print("1. Динамический массив медленнее из-за периодического копирования")
        print("2. Но динамический массив ГИБКИЙ - не нужно знать размер заранее")
        print("3. Амортизированная сложность pushBack: O(1) у обоих")

# ========== ВИЗУАЛИЗАЦИЯ РАСШИРЕНИЙ ==========
print("\n" + "=" * 70)
print("ПРОЦЕСС РАСШИРЕНИЯ ДИНАМИЧЕСКОГО МАССИВА:")
print("=" * 70)

demo_n = 20
demo_arr = DynamicArray(1)
print(f"\nДемонстрация для {demo_n} элементов:")
print(f"{'Операция':<10} {'Значение':<10} {'Размер':<10} {'Емкость':<10} {'Расширение?'}")
print("-" * 60)

for i in range(demo_n):
    old_capacity = demo_arr.capacity
    demo_arr.pushBack(i)
    expanded = "ДА" if demo_arr.capacity > old_capacity else "нет"
    print(f"pushBack({i:<8}) {i:<10} {demo_arr.size:<10} {demo_arr.capacity:<10} {expanded}")


def test_dynamic_array():
    """Тестирование динамического массива."""
    print("=== Тестирование динамического массива ===")

    arr = DynamicArray(2)
    print(f"1. Создан массив: {arr}")

    # Добавление элементов с расширением
    for i in range(10):
        arr.pushBack(i * 10)
        print(f"   pushBack({i * 10:3d}) → {arr}")

    # Добавление в начало
    arr.pushFront(-10)
    print(f"\n2. После pushFront(-10): {arr}")

    print(f"\n3. Доступ по индексу:")
    print(f"   arr[0] = {arr[0]}")
    print(f"   arr[5] = {arr[5]}")
    print(f"   arr[{len(arr) - 1}] = {arr[len(arr) - 1]}")


# ЗАПУСК ПРОГРАММЫ
print("\n" + "=" * 80)
print("ЗАДАНИЕ 2: ДИНАМИЧЕСКИЙ МАССИВ")
print("=" * 80)
test_dynamic_array()
benchmark_insertion(100000)

# Дополнительный бенчмарк с разными размерами
print("\n" + "=" * 70)
print("ДОПОЛНИТЕЛЬНЫЙ БЕНЧМАРК (разные размеры):")
print("=" * 70)

sizes = [1000, 10000, 100000, 1000000]

print(f"\n{'Кол-во элементов':<15} {'Время (сек)':<15} {'Емкость':<15}")
print("-" * 45)

for size in sizes:
    if size <= 1000000:
        arr = DynamicArray(1)
        start = time.time()

        for i in range(size):
            arr.pushBack(i)

        elapsed = time.time() - start
        print(f"{size:<15,} {elapsed:<15.6f} {arr.capacity:<15,}".replace(',', ' '))