"""
Задание 7: Задача "Калькулятор"
Преобразование инфиксной записи в обратную польскую нотацию (ОПН/RPN)
и вычисление результата с использованием стека.
"""


class CalculatorRPN:
    """
    Калькулятор, работающий с обратной польской нотацией (RPN).
    Все методы — статические.
    """

    # Приоритет операторов (чем больше, тем выше приоритет)
    PRECEDENCE = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        '^': 3,  # возведение в степень
    }

    @staticmethod
    def infix_to_rpn(expression: str) -> list:
        """Преобразование инфиксной записи в RPN (алгоритм Дейкстры)."""
        output = []
        operators_stack = []
        tokens = CalculatorRPN.tokenize(expression)

        for token in tokens:
            if CalculatorRPN.is_number(token):
                output.append(token)
            elif token == '(':
                operators_stack.append(token)
            elif token == ')':
                while operators_stack and operators_stack[-1] != '(':
                    output.append(operators_stack.pop())
                if operators_stack:
                    operators_stack.pop()  # удаляем '('
            elif token in CalculatorRPN.PRECEDENCE:
                while (operators_stack and
                       operators_stack[-1] != '(' and
                       CalculatorRPN.PRECEDENCE.get(operators_stack[-1], 0) >=
                       CalculatorRPN.PRECEDENCE[token]):
                    output.append(operators_stack.pop())
                operators_stack.append(token)

        while operators_stack:
            output.append(operators_stack.pop())
        return output

    @staticmethod
    def evaluate_rpn(rpn_tokens: list) -> float:
        """Вычисление RPN-выражения."""
        stack = []
        for token in rpn_tokens:
            if CalculatorRPN.is_number(token):
                stack.append(float(token))
            else:
                if len(stack) < 2:
                    raise ValueError("Недостаточно операндов")
                b = stack.pop()
                a = stack.pop()
                result = CalculatorRPN.apply_operator(token, a, b)
                stack.append(result)
        if len(stack) != 1:
            raise ValueError("Неверное выражение")
        return stack[0]

    @staticmethod
    def tokenize(expression: str) -> list:
        """Разбиение выражения на токены."""
        expression = expression.replace(' ', '')
        for op in "()+-*/^":
            expression = expression.replace(op, f' {op} ')
        return [t for t in expression.split() if t]

    @staticmethod
    def is_number(token: str) -> bool:
        """Проверка, является ли токен числом."""
        try:
            float(token)
            return True
        except ValueError:
            return False

    @staticmethod
    def apply_operator(operator: str, a: float, b: float) -> float:
        """Применение оператора."""
        if operator == '+': return a + b
        if operator == '-': return a - b
        if operator == '*': return a * b
        if operator == '/':
            if b == 0:
                raise ZeroDivisionError("Деление на ноль")
            return a / b
        if operator == '^': return a ** b
        raise ValueError(f"Неизвестный оператор: {operator}")


# ========== ТЕСТЫ ВНЕ КЛАССА ==========

def test_calculator():
    """Тестирование калькулятора."""
    print("=== Калькулятор с RPN ===")

    test_cases = [
        ("3 + 4", 7),
        ("10 - 3", 7),
        ("3 * 4", 12),
        ("10 / 2", 5),
        ("3 + 4 * 2", 11),
        ("(3 + 4) * 2", 14),
        ("10 - 2 * 3", 4),
        ("(10 - 2) * 3", 24),
        ("3 + 4 * 2 / (1 - 5)", 1),
        ("2 ^ 3", 8),
        ("3 + 4 * 2 ^ 2", 19),
    ]

    print("1. Тестирование:")
    for expr, expected in test_cases:
        try:
            rpn = CalculatorRPN.infix_to_rpn(expr)
            result = CalculatorRPN.evaluate_rpn(rpn)
            status = "✓" if abs(result - expected) < 1e-9 else "✗"
            print(f"{status} {expr:20} -> {' '.join(rpn):20} = {result}")
        except Exception as e:
            print(f"✗ {expr:20} -> Ошибка: {e}")

    # Демонстрация
    print("\n2. Демонстрация для '3 + 4 * 2':")
    expr = "3 + 4 * 2"
    rpn = CalculatorRPN.infix_to_rpn(expr)
    print(f"   RPN: {' '.join(rpn)}")
    result = CalculatorRPN.evaluate_rpn(rpn)
    print(f"   Результат: {result}")


def interactive_calculator():
    """Интерактивный режим."""
    print("\n" + "=" * 50)
    print("ИНТЕРАКТИВНЫЙ КАЛЬКУЛЯТОР")
    print("Введите выражение или 'quit' для выхода")
    print("=" * 50)

    while True:
        try:
            user_input = input("\n> ").strip()
            if user_input.lower() in ['quit', 'exit', 'q']:
                break
            if not user_input:
                continue

            rpn = CalculatorRPN.infix_to_rpn(user_input)
            result = CalculatorRPN.evaluate_rpn(rpn)
            print(f"RPN: {' '.join(rpn)}")
            print(f"Результат: {result}")

        except Exception as e:
            print(f"Ошибка: {e}")


# ========== ЗАПУСК ПРОГРАММЫ ==========

if __name__ == "__main__":
    print("\n" + "=" * 80)
    print("ЗАДАНИЕ 7: КАЛЬКУЛЯТОР (RPN)")
    print("=" * 80)

    test_calculator()

    # Раскомментируйте для интерактивного режима:
    # interactive_calculator()

    print("\n" + "=" * 80)
    print("РАБОТА ЗАВЕРШЕНА")
    print("=" * 80)