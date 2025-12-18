"""
Задание 12: Trie (углубление)
"""


print("DEBUG: Файл начал выполняться")

class AdvancedTrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.word_count = 0
        self.word = None
        self.data = {}

class AdvancedTrie:
    def __init__(self):
        self.root = AdvancedTrieNode()
        self.total_words = 0

    def insert(self, word: str, **kwargs):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = AdvancedTrieNode()
            node = node.children[char]
            node.word_count += 1

        if not node.is_end_of_word:
            node.is_end_of_word = True
            node.word = word
            self.total_words += 1
        node.data.update(kwargs)

    def search(self, word: str):
        node = self.root
        for char in word:
            if char not in node.children:
                return None
            node = node.children[char]
        return node if node.is_end_of_word else None

    def count_words_with_prefix(self, prefix: str) -> int:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return 0
            node = node.children[char]
        return node.word_count

    def __len__(self):
        return self.total_words

def test_advanced_trie():
    print("=== Тест AdvancedTrie ===")
    trie = AdvancedTrie()
    trie.insert("hello", freq=10)
    trie.insert("world", freq=5)
    print(f"Слов в дереве: {len(trie)}")
    print(f"Слов с префиксом 'he': {trie.count_words_with_prefix('he')}")


if __name__ == "__main__":
    print("DEBUG: Запуск основной программы")
    test_advanced_trie()
    print("DEBUG: Программа завершена")