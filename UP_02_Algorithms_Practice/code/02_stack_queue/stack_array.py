"""
Задание 5.1: Стек на массиве
Реализация стека (LIFO) с использованием массива/списка.
"""


class StackArray:
    """
    Стек на основе массива (списка Python).

    Принцип LIFO (Last In, First Out):
    - Последний добавленный элемент извлекается первым
    - Операции только с вершиной стека

    Сложности:
    - push: O(1) амортизированно
    - pop: O(1)
    - peek: O(1)
    """

    def __init__(self, capacity=None):
        """
        Инициализация стека.

        Args:
            capacity: максимальный размер (None = динамический)
        """
        self.items = []
        self.capacity = capacity

    def push(self, item):
        """
        Добавление элемента на вершину стека.

        Сложность: O(1) амортизированно
        """
        if self.capacity is not None and len(self.items) >= self.capacity:
            raise OverflowError("Stack is full")
        self.items.append(item)

    def pop(self):
        """
        Удаление и возврат элемента с вершины стека.

        Сложность: O(1)
        """
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self.items.pop()

    def peek(self):
        """
        Просмотр элемента на вершине стека без удаления.

        Сложность: O(1)
        """
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.items[-1]

    def is_empty(self):
        """Проверка пустоты стека. Сложность: O(1)"""
        return len(self.items) == 0

    def size(self):
        """Текущий размер стека. Сложность: O(1)"""
        return len(self.items)

    def __str__(self):
        """Строковое представление стека."""
        return f"StackArray({self.items})"

    def clear(self):
        """Очистка стека. Сложность: O(1)"""
        self.items.clear()


def is_balanced_parentheses(expression: str) -> bool:
    """
    Проверка корректности скобочной последовательности.

    Использует стек для проверки:
    - Открывающие скобки кладем в стек
    - Закрывающие скобки проверяем с вершиной стека
    - В конце стек должен быть пуст

    Поддерживаемые скобки: (), [], {}

    Сложность: O(n), где n = длина выражения
    """
    stack = StackArray()
    matching = {')': '(', ']': '[', '}': '{'}

    for char in expression:
        if char in '([{':  # Открывающая скобка
            stack.push(char)
        elif char in ')]}':  # Закрывающая скобка
            if stack.is_empty() or stack.pop() != matching[char]:
                return False

    return stack.is_empty()  # Все скобки должны быть закрыты


def test_stack_and_parentheses():
    """Тестирование стека и проверки скобок."""
    print("=== Стек на массиве и проверка скобок ===")

    # 1. Тестирование стека
    stack = StackArray()
    print("1. Тестирование стека:")

    stack.push(10)
    stack.push(20)
    stack.push(30)
    print(f"   После push(10, 20, 30): {stack}")
    print(f"   peek(): {stack.peek()}")
    print(f"   pop(): {stack.pop()}")
    print(f"   После pop: {stack}")
    print(f"   Размер: {stack.size()}")
    print(f"   Пустой? {stack.is_empty()}")

    # 2. Проверка скобочных последовательностей
    print("\n2. Проверка скобочных последовательностей:")

    test_cases = [
        ("([])", True),
        ("([{}])", True),
        ("({[]})", True),
        ("([)]", False),
        ("((())", False),
        ("())", False),
        ("", True),
        ("abc", True),
    ]

    for expr, expected in test_cases:
        result = is_balanced_parentheses(expr)
        status = "✓" if result == expected else "✗"
        print(f"   {status} '{expr}' -> {result} (ожидалось: {expected})")

    # 3. Стек с ограниченной емкостью
    print("\n3. Стек с ограниченной емкостью (capacity=3):")
    limited_stack = StackArray(3)

    limited_stack.push(1)
    limited_stack.push(2)
    limited_stack.push(3)
    print(f"   После push 1, 2, 3: {limited_stack}")

    try:
        limited_stack.push(4)
        print("   Ошибка: должно было быть исключение!")
    except OverflowError as e:
        print(f"   ✓ Ожидаемое исключение: {e}")

    # 4. Сравнение сложности
    print("\n4. Сводка сложности операций стека на массиве:")
    print("   push(item):  O(1) амортизированно")
    print("   pop():       O(1)")
    print("   peek():      O(1)")
    print("   is_empty():  O(1)")
    print("   size():      O(1)")


# ЗАПУСК ПРОГРАММЫ
if __name__ == "__main__":
    print("\n" + "=" * 80)
    print("ЗАДАНИЕ 5.1: СТЕК НА МАССИВЕ")
    print("=" * 80)

    test_stack_and_parentheses()

    print("\n" + "=" * 80)
    print("РАБОТА ЗАВЕРШЕНА УСПЕШНО")
    print("=" * 80)