"""
Задание 3: Односвязный список
Реализация односвязного списка с основными операциями.
Сравнение с массивами по трудоемкости.
"""


class SinglyLinkedList:
    """Односвязный список."""

    class Node:
        """Внутренний класс узла списка."""
        def __init__(self, value):
            self.value = value
            self.next = None

    def __init__(self):
        """Инициализация пустого списка."""
        self.head = None
        self.length = 0

    def insert_front(self, value) -> None:
        """Вставка в начало. Сложность: O(1)"""
        new_node = self.Node(value)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def insert_back(self, value) -> None:
        """Вставка в конец. Сложность: O(n)"""
        new_node = self.Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.length += 1

    def find(self, value) -> int:
        """
        Поиск значения в списке.
        Возвращает индекс (0-based) или -1, если не найдено.
        Сложность: O(n)
        """
        current = self.head
        index = 0
        while current:
            if current.value == value:
                return index
            current = current.next
            index += 1
        return -1

    def remove(self, value) -> bool:
        """
        Удаление первого вхождения значения.
        Возвращает True, если удалено, иначе False.
        Сложность: O(n)
        """
        if self.head is None:
            return False

        if self.head.value == value:
            self.head = self.head.next
            self.length -= 1
            return True

        current = self.head
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                self.length -= 1
                return True
            current = current.next
        return False

    def reverse(self) -> None:
        """Разворот списка. Сложность: O(n)"""
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def __str__(self) -> str:
        """Строковое представление списка. Сложность: O(n)"""
        if self.head is None:
            return "Empty list"
        values = []
        current = self.head
        while current:
            values.append(str(current.value))
            current = current.next
        return " → ".join(values)

    def __len__(self) -> int:
        """Длина списка. Сложность: O(1)"""
        return self.length

    def to_list(self) -> list:
        """Преобразование в Python list. Сложность: O(n)"""
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result


def test_singly_linked_list():
    """Тестирование односвязного списка."""
    print("=== Тестирование односвязного списка ===")

    sll = SinglyLinkedList()

    # 1. Вставка в конец
    sll.insert_back(10)
    sll.insert_back(20)
    sll.insert_back(30)
    print(f"1. После insert_back 10, 20, 30: {sll}")

    # 2. Вставка в начало
    sll.insert_front(5)
    sll.insert_front(1)
    print(f"2. После insert_front 5, 1: {sll}")

    # 3. Поиск элементов
    print(f"3. Поиск 20: индекс = {sll.find(20)}")
    print(f"   Поиск 99: индекс = {sll.find(99)}")

    # 4. Удаление элементов
    removed_20 = sll.remove(20)
    print(f"4. Удаление 20 (успешно: {removed_20}): {sll}")

    removed_1 = sll.remove(1)
    print(f"   Удаление 1 (успешно: {removed_1}): {sll}")

    # 5. Разворот списка
    sll.reverse()
    print(f"5. После reverse(): {sll}")

    # 6. Длина и преобразование
    print(f"6. Длина списка: {len(sll)}")
    print(f"   В виде Python list: {sll.to_list()}")


def compare_with_arrays():
    """Сравнение односвязного списка и массива."""
    print("\n" + "="*70)
    print("СРАВНЕНИЕ ОДНОСВЯЗНОГО СПИСКА И МАССИВА")
    print("="*70)

    print("\n1. ВСТАВКА В НАЧАЛО:")
    print("   Список: O(1) — меняем ссылку")
    print("   Массив: O(n) — сдвиг всех элементов")

    print("\n2. ВСТАВКА В КОНЕЦ:")
    print("   Список (без tail): O(n) — проход до конца")
    print("   Динамический массив: O(1) амортизированно")

    print("\n3. УДАЛЕНИЕ ПО ЗНАЧЕНИЮ:")
    print("   Список: O(n) — поиск + O(1) удаление")
    print("   Массив: O(n) — поиск + O(n) сдвиг → O(n)")

    print("\n4. ДОСТУП ПО ИНДЕКСУ:")
    print("   Список: O(n) — обход от головы")
    print("   Массив: O(1) — прямой доступ")

    print("\n5. ПАМЯТЬ:")
    print("   Список: значение + указатель на каждый узел (накладные расходы)")
    print("   Массив: только значения (плотная упаковка)")

    print("\nВЫВОДЫ:")
    print("• Список выгоден при частых вставках/удалениях в начале")
    print("• Массив выгоден при частом доступе по индексу")
    print("• Выбор структуры зависит от сценария использования")


# ЗАПУСК ПРОГРАММЫ
if __name__ == "__main__":
    print("\n" + "="*80)
    print("ЗАДАНИЕ 3: ОДНОСВЯЗНЫЙ СПИСОК")
    print("="*80)

    test_singly_linked_list()
    compare_with_arrays()

    print("\n" + "="*80)
    print("РАБОТА ЗАВЕРШЕНА УСПЕШНО")
    print("="*80)