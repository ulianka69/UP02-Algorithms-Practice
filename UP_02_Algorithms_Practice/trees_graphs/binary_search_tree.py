"""
Задание 11: Бинарное дерево поиска (BST)
Реализация BST с операциями вставки, поиска, удаления.
Реализация обходов: in-order, pre-order, post-order.
Проверка сбалансированности дерева.
"""


class TreeNode:
    """Узел бинарного дерева поиска."""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    """Бинарное дерево поиска (Binary Search Tree)."""

    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, value):
        """Вставка значения в дерево."""
        if self.root is None:
            self.root = TreeNode(value)
            self.size = 1
            return True

        current = self.root
        parent = None

        while current:
            parent = current
            if value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
            else:
                return False  # Дубликат

        new_node = TreeNode(value)
        if value < parent.value:
            parent.left = new_node
        else:
            parent.right = new_node

        self.size += 1
        return True

    def search(self, value):
        """Поиск значения в дереве."""
        current = self.root
        while current:
            if value == current.value:
                return current
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return None

    def delete(self, value):
        """Удаление значения из дерева."""
        if self.root is None:
            return False

        current = self.root
        parent = None

        while current and current.value != value:
            parent = current
            if value < current.value:
                current = current.left
            else:
                current = current.right

        if current is None:
            return False

        # Случай 1: Нет детей
        if current.left is None and current.right is None:
            if parent is None:
                self.root = None
            elif parent.left == current:
                parent.left = None
            else:
                parent.right = None

        # Случай 2: Один ребенок
        elif current.left is None:  # Только правый
            if parent is None:
                self.root = current.right
            elif parent.left == current:
                parent.left = current.right
            else:
                parent.right = current.right

        elif current.right is None:  # Только левый ← ИСПРАВЛЕНО: правильный отступ!
            if parent is None:
                self.root = current.left
            elif parent.left == current:
                parent.left = current.left
            else:
                parent.right = current.left

        # Случай 3: Два ребенка
        else:
            # Находим преемника (минимум в правом поддереве)
            successor_parent = current
            successor = current.right
            while successor.left:
                successor_parent = successor
                successor = successor.left

            current.value = successor.value

            # Удаляем преемника
            if successor_parent.left == successor:
                successor_parent.left = successor.right
            else:
                successor_parent.right = successor.right

        self.size -= 1
        return True

    def inorder_traversal(self):
        """Центрированный обход (in-order)."""
        result = []
        def traverse(node):
            if node:
                traverse(node.left)
                result.append(node.value)
                traverse(node.right)
        traverse(self.root)
        return result

    def preorder_traversal(self):
        """Прямой обход (pre-order)."""
        result = []
        def traverse(node):
            if node:
                result.append(node.value)
                traverse(node.left)
                traverse(node.right)
        traverse(self.root)
        return result

    def postorder_traversal(self):
        """Обратный обход (post-order)."""
        result = []
        def traverse(node):
            if node:
                traverse(node.left)
                traverse(node.right)
                result.append(node.value)
        traverse(self.root)
        return result

    def is_balanced(self):
        """Проверка сбалансированности дерева."""
        def check_balance(node):
            if node is None:
                return (True, 0)

            left_balanced, left_height = check_balance(node.left)
            right_balanced, right_height = check_balance(node.right)

            current_height = max(left_height, right_height) + 1
            height_diff = abs(left_height - right_height)
            is_balanced = (left_balanced and right_balanced and height_diff <= 1)

            return (is_balanced, current_height)

        balanced, _ = check_balance(self.root)
        return balanced

    def get_height(self):
        """Высота дерева."""
        def height(node):
            if node is None:
                return 0
            return max(height(node.left), height(node.right)) + 1
        return height(self.root)

    def find_min(self):
        """Минимальное значение."""
        if self.root is None:
            return None
        current = self.root
        while current.left:
            current = current.left
        return current.value

    def find_max(self):
        """Максимальное значение."""
        if self.root is None:
            return None
        current = self.root
        while current.right:
            current = current.right
        return current.value

    def __len__(self):
        return self.size

    def contains(self, value):
        return self.search(value) is not None

    def print_tree(self):
        """Визуализация дерева."""
        lines = []
        def build_tree_string(node, prefix="", is_left=True):
            if node is None:
                return
            if node.right:
                build_tree_string(node.right, prefix + ("│   " if is_left else "    "), False)
            lines.append(prefix + ("└── " if is_left else "┌── ") + str(node.value))
            if node.left:
                build_tree_string(node.left, prefix + ("    " if is_left else "│   "), True)

        if self.root:
            build_tree_string(self.root, "", False)
            return "\n".join(lines)
        else:
            return "Empty tree"


# ========== ТЕСТЫ ==========

def test_binary_search_tree():
    """Тестирование BST."""
    print("=== Бинарное дерево поиска (BST) ===")
    bst = BinarySearchTree()
    values = [50, 30, 70, 20, 40, 60, 80]
    for value in values:
        bst.insert(value)

    print("1. Вставка значений:", values)
    print("   Размер дерева:", len(bst))
    print("\n   Визуализация:\n", bst.print_tree())

    print("\n2. Обходы:")
    print(f"   In-order:  {bst.inorder_traversal()}")
    print(f"   Pre-order: {bst.preorder_traversal()}")
    print(f"   Post-order:{bst.postorder_traversal()}")

    print("\n3. Удаление:")
    bst.delete(20)  # лист
    bst.delete(30)  # один ребенок
    bst.delete(50)  # два ребенка
    print(f"   После удалений: {bst.inorder_traversal()}")
    print(f"   Сбалансировано? {bst.is_balanced()}")


def compare_bst_operations():
    """Сравнение операций."""
    print("\n" + "="*70)
    print("СРАВНЕНИЕ: СБАЛАНСИРОВАННОЕ VS ВЫРОЖДЕННОЕ ДЕРЕВО")
    print("="*70)
    print("  Сбалансированное: O(log n)")
    print("  Вырожденное: O(n)")


def bst_applications():
    """Примеры применения."""
    print("\n" + "="*70)
    print("ПРИМЕНЕНИЕ BST")
    print("="*70)

    # Пример с классом Task
    class Task:
        def __init__(self, start_time, name):
            self.start_time = start_time
            self.name = name

        def __lt__(self, other):
            return self.start_time < other.start_time

        def __gt__(self, other):
            return self.start_time > other.start_time

        def __eq__(self, other):
            return self.start_time == other.start_time

        def __str__(self):
            return f"{self.name} @ {self.start_time}"

    tasks_bst = BinarySearchTree()
    tasks = [
        Task(9, "Совещание"),
        Task(10, "Код ревью"),
    ]
    for task in tasks:
        tasks_bst.insert(task)

    print("Задачи:")
    for task in tasks_bst.inorder_traversal():
        print(f"  {task}")


# ========== ЗАПУСК ==========
if __name__ == "__main__":
    print("\n" + "="*80)
    print("ЗАДАНИЕ 11: БИНАРНОЕ ДЕРЕВО ПОИСКА (BST)")
    print("="*80)

    test_binary_search_tree()
    compare_bst_operations()
    bst_applications()

    print("\n" + "="*80)
    print("РАБОТА ЗАВЕРШЕНА УСПЕШНО")
    print("="*80)