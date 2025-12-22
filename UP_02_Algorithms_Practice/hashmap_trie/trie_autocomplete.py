"""
Задание 10: Trie + HashMap для автодополнения
Реализация Trie для хранения слов с поддержкой автодополнения.
"""


class TrieNode:
    """Узел префиксного дерева (Trie)."""
    def __init__(self):
        self.children = {}  # HashMap для дочерних узлов
        self.is_end_of_word = False
        self.frequency = 0
        self.word = None


class TrieAutocomplete:
    """Префиксное дерево (Trie) с поддержкой автодополнения."""

    def __init__(self):
        self.root = TrieNode()
        self.total_words = 0

    def insert(self, word: str, frequency: int = 1):
        """Вставка слова в Trie."""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        if not node.is_end_of_word:
            node.is_end_of_word = True
            node.word = word
            self.total_words += 1
        node.frequency += frequency

    def search(self, word: str) -> bool:
        """Поиск точного совпадения слова."""
        node = self._get_node(word)
        return node is not None and node.is_end_of_word

    def starts_with(self, prefix: str) -> bool:
        """Проверка наличия слов с заданным префиксом."""
        return self._get_node(prefix) is not None

    def autocomplete(self, prefix: str, limit: int = 10):
        """Автодополнение по префиксу."""
        node = self._get_node(prefix)
        if node is None:
            return []

        words = []
        self._collect_words(node, words)
        words.sort(key=lambda x: x[1], reverse=True)
        return words[:limit]

    def _get_node(self, prefix: str):
        """Вспомогательный метод: находит узел по префиксу."""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node

    def _collect_words(self, node: TrieNode, words: list):
        """Рекурсивный сбор всех слов из поддерева."""
        if node.is_end_of_word:
            words.append((node.word, node.frequency))
        for child in node.children.values():
            self._collect_words(child, words)

    def get_word_frequency(self, word: str) -> int:
        """Получение частоты слова."""
        node = self._get_node(word)
        if node and node.is_end_of_word:
            return node.frequency
        return 0

    def __len__(self):
        return self.total_words

    def visualize(self, node=None, prefix="", depth=0, max_depth=3):
        """Визуализация Trie (для отладки)."""
        if node is None:
            node = self.root
            print("Trie визуализация:")
            print("  Корень")

        if depth >= max_depth:
            print("  " * depth + "...")
            return

        for char, child in sorted(node.children.items()):
            marker = "★" if child.is_end_of_word else "├"
            freq_info = f" [{child.frequency}]" if child.is_end_of_word else ""
            print("  " * depth + f"{marker} '{char}'{freq_info}")
            self.visualize(child, prefix + char, depth + 1, max_depth)


# ========== ТЕСТЫ ВНЕ КЛАССА ==========

def test_trie_autocomplete():
    """Тестирование Trie с автодополнением."""
    print("=== Trie с автодополнением ===")

    trie = TrieAutocomplete()
    word_frequencies = [
        ("apple", 50), ("application", 30), ("app", 100),
        ("banana", 40), ("band", 25), ("bandana", 10),
        ("cat", 60), ("category", 20), ("catalog", 15),
        ("dog", 70), ("document", 35), ("domain", 25),
    ]

    for word, freq in word_frequencies:
        trie.insert(word, freq)

    print(f"1. Добавлено слов: {len(trie)}")
    print("\n2. Визуализация Trie (первые 3 уровня):")
    trie.visualize(max_depth=3)

    print("\n3. Автодополнение для 'app':")
    for word, freq in trie.autocomplete("app", limit=5):
        print(f"   '{word}': частота {freq}")

    print("\n4. Точный поиск:")
    for word in ["apple", "app", "xyz"]:
        found = trie.search(word)
        freq = trie.get_word_frequency(word)
        print(f"   '{word}': {'найдено' if found else 'не найдено'} (частота: {freq})")


def trie_performance_comparison():
    """Сравнение производительности."""
    print("\n" + "=" * 70)
    print("СРАВНЕНИЕ ПРОИЗВОДИТЕЛЬНОСТИ TRIE")
    print("=" * 70)
    print("  Trie эффективен для префиксного поиска")
    print("  Обычный список: O(n*m), Trie: O(k+m)")


def trie_real_world_applications():
    """Примеры применения."""
    print("\n" + "=" * 70)
    print("РЕАЛЬНЫЕ ПРИМЕНЕНИЯ TRIE")
    print("=" * 70)
    print("  1. Автодополнение в поисковиках")
    print("  2. Проверка орфографии")
    print("  3. Маршрутизация IP-адресов")


# ========== ЗАПУСК ПРОГРАММЫ ==========
if __name__ == "__main__":
    print("\n" + "=" * 80)
    print("ЗАДАНИЕ 10: TRIE ДЛЯ АВТОДОПОЛНЕНИЯ")
    print("=" * 80)

    test_trie_autocomplete()
    trie_performance_comparison()
    trie_real_world_applications()

    print("\n" + "=" * 80)
    print("РАБОТА ЗАВЕРШЕНА УСПЕШНО")
    print("=" * 80)