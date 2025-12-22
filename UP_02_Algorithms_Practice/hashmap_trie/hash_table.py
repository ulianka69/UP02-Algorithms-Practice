"""
Задание 8: Хэш-таблица
Реализация хэш-таблицы с разрешением коллизий методом цепочек.
"""


class HashTable:
    """
    Хэш-таблица с методом цепочек (separate chaining).

    Особенности:
    - Каждая "корзина" — список (цепочка)
    - Поддерживает динамическое рехеширование
    - Контролирует коэффициент заполнения
    """

    def __init__(self, capacity=8, load_factor=0.75):
        """
        Инициализация хэш-таблицы.

        Args:
            capacity: начальная ёмкость (рекомендуется степень двойки)
            load_factor: порог для рехеширования (по умолчанию 0.75)
        """
        self.capacity = capacity
        self.load_factor = load_factor
        self.size = 0
        self.buckets = [[] for _ in range(capacity)]  # Список списков

    def _hash(self, key):
        """Встроенная хэш-функция Python + модуль."""
        return abs(hash(key)) % self.capacity

    def put(self, key, value):
        """Добавление/обновление пары ключ-значение."""
        if self.size >= self.load_factor * self.capacity:
            self._resize()

        bucket_index = self._hash(key)
        bucket = self.buckets[bucket_index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)  # Обновление
                return

        bucket.append((key, value))  # Новая пара
        self.size += 1

    def get(self, key):
        """Получение значения по ключу."""
        bucket_index = self._hash(key)
        bucket = self.buckets[bucket_index]

        for k, v in bucket:
            if k == key:
                return v
        raise KeyError(key)

    def remove(self, key):
        """Удаление пары по ключу."""
        bucket_index = self._hash(key)
        bucket = self.buckets[bucket_index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.size -= 1
                return v
        raise KeyError(key)

    def contains(self, key):
        """Проверка наличия ключа."""
        try:
            self.get(key)
            return True
        except KeyError:
            return False

    def _resize(self):
        """Рехеширование (удвоение размера)."""
        old_buckets = self.buckets
        self.capacity *= 2
        self.size = 0
        self.buckets = [[] for _ in range(self.capacity)]

        for bucket in old_buckets:
            for key, value in bucket:
                self.put(key, value)

    def visualize(self, title="Хэш-таблица"):
        """Визуализация состояния таблицы."""
        print(f"\n{title}:")
        print("=" * 50)
        for i, bucket in enumerate(self.buckets):
            if bucket:
                entries = [f"{k}:{v}" for k, v in bucket]
                print(f"  [{i:2}] → " + " → ".join(entries))
            else:
                print(f"  [{i:2}] → (пусто)")

    def __str__(self):
        items = []
        for bucket in self.buckets:
            for k, v in bucket:
                items.append(f"{k}: {v}")
        return "{" + ", ".join(items) + "}"


def test_hash_table():
    """Тестирование хэш-таблицы."""
    print("=== Тестирование хэш-таблицы ===")

    # 1. Создание и базовые операции
    ht = HashTable(capacity=4, load_factor=0.75)
    print("1. Создана хэш-таблица (емкость=4, load_factor=0.75)")
    ht.put("a", 1)
    ht.put("b", 2)
    ht.put("c", 3)
    print(f"   После добавления a:1, b:2, c:3")
    ht.visualize("Начальное состояние")

    # 2. Обновление значения
    ht.put("a", 10)
    print(f"2. Обновление ключа 'a' → 10")
    print(f"   get('a') = {ht.get('a')}")

    # 3. Удаление
    removed = ht.remove("b")
    print(f"4. Удаление ключа 'b' → {removed}")
    ht.visualize("После удаления 'b'")

    # 4. Проверка содержимого
    print(f"5. contains('c'): {ht.contains('c')}")
    print(f"   contains('b'): {ht.contains('b')}")

    # 5. Рехеширование
    ht.put("d", 4)
    ht.put("e", 5)
    ht.visualize("После рехеширования")

    # 6. Коллизии (демонстрация)
    print("\n6. Демонстрация коллизий:")
    small_ht = HashTable(capacity=3, load_factor=1.0)
    collision_keys = ["ab", "ba", "cd", "dc", "ef", "fe"]
    for key in collision_keys:
        small_ht.put(key, f"value_{key}")
    small_ht.visualize("Демонстрация коллизий (емкость=3)")

    # 7. Сводка сложности
    print("\n7. Сводка сложности (в среднем):")
    print("   put(key, value):    O(1)")
    print("   get(key):           O(1)")
    print("   remove(key):        O(1)")
    print("   contains(key):      O(1)")
    print("\n   В худшем случае: O(n) (все ключи в одной корзине)")
    print("   Рехеширование: O(n), но редко")


def compare_hash_functions():
    """Сравнение качества хэш-функций."""
    print("\n" + "=" * 70)
    print("СРАВНЕНИЕ ХЭШ-ФУНКЦИЙ")
    print("=" * 70)

    words = ["apple", "banana", "orange", "grape", "kiwi",
             "mango", "pear", "peach", "melon", "berry"]

    def bad_hash(key, capacity):
        return 0

    def simple_hash(key, capacity):
        return sum(ord(c) for c in key) % capacity

    def polynomial_hash(key, capacity):
        hash_val = 0
        for char in key:
            hash_val = (hash_val * 31 + ord(char)) % capacity
        return hash_val

    def python_hash(key, capacity):
        return abs(hash(key)) % capacity

    hash_functions = [
        ("Плохая (всегда 0)", bad_hash),
        ("Простая (сумма)", simple_hash),
        ("Полиномиальная", polynomial_hash),
        ("Python hash()", python_hash),
    ]

    capacity = 10
    print(f"\nРаспределение для {len(words)} слов (емкость={capacity}):")
    print("-" * 50)

    for name, hash_func in hash_functions:
        distribution = [0] * capacity
        for word in words:
            idx = hash_func(word, capacity)
            distribution[idx] += 1

        empty_buckets = sum(1 for x in distribution if x == 0)
        max_count = max(distribution)
        # ИСПРАВЛЕНА ОШИБКА: добавлены ** для возведения в степень
        std_dev = (sum((count - 1) ** 2 for count in distribution) / capacity) ** 0.5

        print(f"\n{name}:")
        print(f"  Распределение: {distribution}")
        print(f"  Пустых корзин: {empty_buckets}/{capacity}")
        print(f"  Макс. коллизия: {max_count}")
        print(f"  Станд. откл.: {std_dev:.2f}")

        print("  Визуально: ", end="")
        for count in distribution:
            if count == 0:
                print("_", end=" ")
            elif count == 1:
                print(".", end=" ")
            elif count == 2:
                print(":", end=" ")
            else:
                print("#", end=" ")
        print()

    print("\nВЫВОДЫ:")
    print("• Плохая хэш-функция → все в одной корзине → O(n)")
    print("• Хорошая хэш-функция → равномерное распределение → O(1)")


# ЗАПУСК ПРОГРАММЫ
if __name__ == "__main__":
    print("\n" + "=" * 80)
    print("ЗАДАНИЕ 8: ХЭШ-ТАБЛИЦА")
    print("=" * 80)

    test_hash_table()
    compare_hash_functions()

    print("\n" + "=" * 80)
    print("РАБОТА ЗАВЕРШЕНА УСПЕШНО")
    print("=" * 80)