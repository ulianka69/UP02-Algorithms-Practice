"""
Задание 4: Двусвязный список
Реализация с операциями вставки после узла и удаления без поиска.
Итератор по списку.
"""


class DoublyNode:
    """Узел двусвязного списка."""
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    """Двусвязный список."""

    def __init__(self):
        """Инициализация пустого списка. Сложность: O(1)"""
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value) -> DoublyNode:
        """Добавление в конец. Сложность: O(1). Возвращает узел."""
        new_node = DoublyNode(value)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return new_node

    def insert_after(self, node: DoublyNode, value) -> DoublyNode:
        """Вставка после заданного узла. Сложность: O(1)"""
        if node is None:
            raise ValueError("Node cannot be None")
        new_node = DoublyNode(value)
        new_node.prev = node
        new_node.next = node.next

        if node.next:
            node.next.prev = new_node
        else:
            self.tail = new_node

        node.next = new_node
        self.length += 1
        return new_node

    def remove_node(self, node: DoublyNode) -> None:
        """Удаление узла (без поиска). Сложность: O(1)"""
        if node is None:
            return
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

        node.prev = None
        node.next = None
        self.length -= 1

    def find(self, value) -> DoublyNode:
        """Поиск узла по значению. Сложность: O(n)"""
        current = self.head
        while current:
            if current.value == value:
                return current
            current = current.next
        return None

    def __str__(self) -> str:
        """Строковое представление."""
        values = []
        current = self.head
        while current:
            values.append(str(current.value))
            current = current.next
        return " ⇄ ".join(values) if values else "Empty list"

    def __len__(self) -> int:
        return self.length

    def to_list(self) -> list:
        """Преобразование в Python list (прямой порядок)."""
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result

    def to_reverse_list(self) -> list:
        """Преобразование в Python list (обратный порядок)."""
        result = []
        current = self.tail
        while current:
            result.append(current.value)
            current = current.prev
        return result

    # ========== ИТЕРАТОРЫ ==========

    class _ForwardIterator:
        def __init__(self, head):
            self.current = head

        def __iter__(self):
            return self

        def __next__(self):
            if self.current is None:
                raise StopIteration
            value = self.current.value
            self.current = self.current.next
            return value

    class _ReverseIterator:
        def __init__(self, tail):
            self.current = tail

        def __iter__(self):
            return self

        def __next__(self):
            if self.current is None:
                raise StopIteration
            value = self.current.value
            self.current = self.current.prev
            return value

    def __iter__(self):
        """Поддержка for x in dll."""
        return self._ForwardIterator(self.head)

    def reverse_iter(self):
        """Обратный итератор."""
        return self._ReverseIterator(self.tail)


# ========== ТЕСТЫ ВНЕ КЛАССА ==========

def test_doubly_linked_list():
    """Тестирование двусвязного списка."""
    print("=== Тестирование двусвязного списка ===")

    dll = DoublyLinkedList()

    # 1. Добавление элементов
    node1 = dll.append(10)
    node2 = dll.append(20)
    node3 = dll.append(30)
    print(f"1. После append 10, 20, 30: {dll}")

    # 2. Вставка после узла
    node_x = dll.insert_after(node2, 25)
    print(f"2. После insert_after(node20, 25): {dll}")

    # 3. Итерация вперед
    print(f"3. Итерация (вперед): {[x for x in dll]}")

    # 4. Итерация назад
    print(f"4. Итерация (назад): {dll.to_reverse_list()}")

    # 5. Удаление узла
    dll.remove_node(node2)
    print(f"5. После remove_node(node20): {dll}")

    # 6. Поиск узла
    found_node = dll.find(25)
    print(f"6. Поиск узла со значением 25: {'найден' if found_node else 'не найден'}")

    # 7. Различные представления
    print(f"7. Длина списка: {len(dll)}")
    print(f"   to_list(): {dll.to_list()}")
    print(f"   to_reverse_list(): {dll.to_reverse_list()}")

    # 8. Демонстрация преимуществ
    print("\n8. Преимущества двусвязного списка:")
    print("   - Удаление узла O(1) (при известном узле)")
    print("   - Обход в обе стороны")
    print("   - Быстрое удаление из конца (знаем tail)")


def compare_with_singly_list():
    """Сравнение двусвязного и односвязного списков."""
    print("\n" + "=" * 70)
    print("СРАВНЕНИЕ ДВУСВЯЗНОГО И ОДНОСВЯЗНОГО СПИСКОВ")
    print("=" * 70)

    print("\n1. ПАМЯТЬ:")
    print("   Односвязный: данные + 1 указатель (next)")
    print("   Двусвязный: данные + 2 указателя (prev, next)")
    print("   Двусвязный занимает ~ в 1.5 раза больше памяти")

    print("\n2. УДАЛЕНИЕ УЗЛА:")
    print("   Односвязный: O(1) если известен предыдущий узел, иначе O(n)")
    print("   Двусвязный: O(1) всегда (знаем и prev, и next)")

    print("\n3. ВСТАВКА ПЕРЕД УЗЛОМ:")
    print("   Односвязный: O(n) (нужно найти предыдущий)")
    print("   Двусвязный: O(1) (знаем prev)")

    print("\n4. ОБХОД:")
    print("   Односвязный: только вперед")
    print("   Двусвязный: вперед и назад")

    print("\n5. ДОСТУП К КОНЦУ:")
    print("   Оба: O(1) с tail")

    print("\nВЫВОДЫ:")
    print("- Двусвязный список гибче, но требует больше памяти")
    print("- Выбор зависит от операций: если нужно часто удалять/вставлять")
    print("  в середине — двусвязный лучше")
    print("- Если важен минимальный расход памяти — односвязный")


# ========== ЗАПУСК ПРОГРАММЫ ==========

if __name__ == "__main__":
    print("\n" + "=" * 80)
    print("ЗАДАНИЕ 4: ДВУСВЯЗНЫЙ СПИСОК")
    print("=" * 80)

    test_doubly_linked_list()
    compare_with_singly_list()

    print("\n" + "=" * 80)
    print("РАБОТА ЗАВЕРШЕНА УСПЕШНО")
    print("=" * 80)