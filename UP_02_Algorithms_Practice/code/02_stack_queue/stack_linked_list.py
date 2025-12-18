"""
Задание 5.2: Стек на связном списке
Альтернативная реализация стека с использованием связного списка.
"""


class StackNode:
    """Узел для стека на связном списке."""
    def __init__(self, value):
        self.value = value
        self.next = None


class StackLinkedList:
    """
    Стек на основе односвязного списка.

    Особенности:
    - Вершина стека = голова списка
    - Все операции работают с головой
    - Неограниченный размер (пока есть память)
    """

    def __init__(self):
        """Инициализация пустого стека. Сложность: O(1)"""
        self.top = None  # Вершина стека
        self._size = 0   # Количество элементов

    def push(self, item):
        """
        Добавление элемента на вершину стека.
        Сложность: O(1)
        """
        new_node = StackNode(item)
        new_node.next = self.top
        self.top = new_node
        self._size += 1

    def pop(self):
        """
        Удаление и возврат элемента с вершины стека.
        Сложность: O(1)
        """
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        item = self.top.value
        self.top = self.top.next
        self._size -= 1
        return item

    def peek(self):
        """
        Просмотр вершины стека без удаления.
        Сложность: O(1)
        """
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.top.value

    def is_empty(self):
        """Проверка пустоты стека. Сложность: O(1)"""
        return self.top is None

    def size(self):
        """Размер стека. Сложность: O(1)"""
        return self._size

    def __str__(self):
        """Строковое представление стека (снизу вверх)."""
        values = []
        current = self.top
        while current:
            values.append(str(current.value))
            current = current.next
        # Стек читается снизу вверх, поэтому переворачиваем
        return "StackLinkedList([" + ", ".join(reversed(values)) + "])"

    def clear(self):
        """Очистка стека. Сложность: O(1)"""
        self.top = None
        self._size = 0


# Минимальная реализация StackArray для сравнения (из задания 5.1)
class StackArray:
    def __init__(self, capacity=None):
        self.items = []
        self.capacity = capacity

    def push(self, item):
        if self.capacity is not None and len(self.items) >= self.capacity:
            raise OverflowError("Stack is full")
        self.items.append(item)

    def pop(self):
        if not self.items:
            raise IndexError("Pop from empty stack")
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0


def test_stack_linked_list():
    """Тестирование стека на связном списке."""
    print("=== Стек на связном списке ===")

    stack = StackLinkedList()

    # 1. Базовые операции
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print(f"1. После push(10, 20, 30): {stack}")

    print(f"   peek(): {stack.peek()}")
    print(f"   pop(): {stack.pop()}")
    print(f"   После pop: {stack}")

    # 2. Проверка скобок с использованием стека на списке
    def is_balanced_with_list_stack(expr):
        stack = StackLinkedList()
        matching = {')': '(', ']': '[', '}': '{'}
        for char in expr:
            if char in '([{':
                stack.push(char)
            elif char in ')]}':
                if stack.is_empty() or stack.pop() != matching[char]:
                    return False
        return stack.is_empty()

    print("\n2. Проверка скобок стеком на списке:")
    test_cases = ["({[]})", "([)]", "((())", ""]
    for expr in test_cases:
        result = is_balanced_with_list_stack(expr)
        print(f"   '{expr}' → {result}")

    # 3. Очистка
    stack.clear()
    print(f"\n3. После clear(): {stack}")
    print(f"   is_empty? {stack.is_empty()}")
    print(f"   size: {stack.size()}")


def compare_stack_implementations():
    """Сравнение стека на массиве и на связном списке."""
    print("\n" + "=" * 70)
    print("СРАВНЕНИЕ РЕАЛИЗАЦИЙ СТЕКА")
    print("=" * 70)

    import time
    n = 10000

    # Стек на массиве
    start = time.time()
    stack_array = StackArray()
    for i in range(n):
        stack_array.push(i)
    for _ in range(n):
        stack_array.pop()
    array_time = time.time() - start

    # Стек на связном списке
    start = time.time()
    stack_list = StackLinkedList()
    for i in range(n):
        stack_list.push(i)
    for _ in range(n):
        stack_list.pop()
    list_time = time.time() - start

    print(f"\nПроизводительность (n = {n:,}):")
    print(f"  Стек на массиве:   {array_time:.6f} сек")
    print(f"  Стек на списке:    {list_time:.6f} сек")
    if array_time > 0:
        print(f"  Отношение (список/массив): {list_time / array_time:.2f}x")

    print("\nПреимущества:")
    print("• Массив: быстрее, лучше локальность памяти")
    print("• Список: неограниченный размер, нет перевыделения памяти")

    print("\nСложность всех операций: O(1) в обеих реализациях")


# ЗАПУСК ПРОГРАММЫ
if __name__ == "__main__":
    print("\n" + "=" * 80)
    print("ЗАДАНИЕ 5.2: СТЕК НА СВЯЗНОМ СПИСКЕ")
    print("=" * 80)

    test_stack_linked_list()
    compare_stack_implementations()

    print("\n" + "=" * 80)
    print("РАБОТА ЗАВЕРШЕНА УСПЕШНО")
    print("=" * 80)