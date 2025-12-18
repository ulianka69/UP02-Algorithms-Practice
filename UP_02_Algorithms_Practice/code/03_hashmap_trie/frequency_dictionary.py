"""
Задание 9: Частотный словарь
Построение HashMap частот встречаемости слов в тексте.
Вывод топ-10 самых частых слов.
"""

import re
import time
from collections import defaultdict


class FrequencyDictionary:
    """
    Частотный словарь на основе хэш-таблицы.
    """

    def __init__(self):
        """Инициализация частотного словаря."""
        self.word_counts = defaultdict(int)
        self.total_words = 0

    def process_text(self, text: str):
        """Обработка текста: извлечение слов и подсчет частот."""
        words = re.findall(r"\b[a-zA-Zа-яА-Я']+\b", text.lower())
        for word in words:
            self.word_counts[word] += 1
        self.total_words += len(words)

    def get_top_words(self, n: int = 10):
        """Получение топ-N самых частых слов."""
        sorted_words = sorted(
            self.word_counts.items(),
            key=lambda x: x[1],
            reverse=True
        )
        top_words = []
        for word, count in sorted_words[:n]:
            percentage = (count / self.total_words * 100) if self.total_words > 0 else 0
            top_words.append((word, count, percentage))
        return top_words

    def get_stats(self):
        """Статистика словаря."""
        unique_words = len(self.word_counts)
        return {
            'total_words': self.total_words,
            'unique_words': unique_words,
            'avg_frequency': self.total_words / unique_words if unique_words > 0 else 0,
            'lexical_diversity': unique_words / self.total_words if self.total_words > 0 else 0,
        }


def test_frequency_dictionary():
    """Тестирование частотного словаря."""
    print("=== Частотный словарь ===")
    text = "the cat and the dog and the mouse"
    freq_dict = FrequencyDictionary()
    freq_dict.process_text(text)
    print("1. Простой тест:")
    print(f"   Текст: '{text}'")
    print(f"   Результат: {dict(freq_dict.word_counts)}")
    top = freq_dict.get_top_words(2)
    print(f"   Топ-2: {top}")
    stats = freq_dict.get_stats()
    print(f"   Статистика: {stats}")


def analyze_real_text():
    """Анализ реального текста (фрагмент 'Войны и мира')."""
    print("\n" + "=" * 70)
    print("АНАЛИЗ РЕАЛЬНОГО ТЕКСТА (ФРАГМЕНТ 'ВОЙНЫ И МИРА')")
    print("=" * 70)

    sample_text = """
    Все счастливые семьи похожи друг на друга, каждая несчастливая 
    семья несчастлива по-своему. Все смешалось в доме Облонских. 
    Жена узнала, что муж был в связи с бывшею в их доме француженкою-гувернанткой, 
    и объявила мужу, что не может жить с ним в одном доме. 
    Положение это продолжалось уже третий день и мучительно чувствовалось 
    и самими супругами, и всеми членами семьи, и домочадцами. 
    Все члены семьи и домочадцы чувствовали, что нет смысла в их 
    сожительстве и что на каждом постоялом дворе случайно сошедшиеся 
    люди более связаны между собой, чем они, члены семьи и домочадцы Облонских. 
    Жена не выходила из своих комнат, мужа третий день не было дома. 
    Дети бегали по всему дому, как потерянные; англичанка поссорилась 
    с экономкой и написала записку приятельнице, прося приискать ей новое место; 
    повар ушел еще вчера со двора, во время обеда; черная кухарка и кучер просили расчета.
    """

    print("Обработка текста...")
    freq_dict = FrequencyDictionary()
    freq_dict.process_text(sample_text)
    stats = freq_dict.get_stats()
    top_words = freq_dict.get_top_words(10)

    print(f"\nСтатистика текста:")
    print(f"  Всего слов: {stats['total_words']}")
    print(f"  Уникальных слов: {stats['unique_words']}")
    print(f"  Средняя частота: {stats['avg_frequency']:.2f}")
    print(f"  Лексическое разнообразие: {stats['lexical_diversity']:.4f}")

    print(f"\nТоп-10 самых частых слов:")
    print("-" * 40)
    print(f"{'Слово':<15} {'Частота':<10} {'%':<8}")
    print("-" * 40)
    for word, count, percent in top_words:
        print(f"{word:<15} {count:<10} {percent:<8.2f}%")

    # Распределение частот
    freq_groups = defaultdict(int)
    for count in freq_dict.word_counts.values():
        if count == 1:
            freq_groups["1 раз"] += 1
        elif count <= 3:
            freq_groups["2-3 раза"] += 1
        elif count <= 10:
            freq_groups["4-10 раз"] += 1
        else:
            freq_groups[">10 раз"] += 1

    print(f"\nРаспределение частот:")
    for group, count in sorted(freq_groups.items()):
        percentage = count / stats['unique_words'] * 100
        print(f"  {group}: {count} слов ({percentage:.1f}%)")


def benchmark_hash_functions():
    """Бенчмарк построения частотного словаря."""
    print("\n" + "=" * 70)
    print("БЕНЧМАРК: ПОСТРОЕНИЕ ЧАСТОТНОГО СЛОВАРЯ")
    print("=" * 70)

    lorem_ipsum = """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
    Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
    Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
    nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in 
    reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
    Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia 
    deserunt mollit anim id est laborum.
    """
    test_text = lorem_ipsum * 1000
    print(f"Длина текста: {len(test_text):,} символов")

    start_time = time.time()
    freq_dict = FrequencyDictionary()
    freq_dict.process_text(test_text)
    stats = freq_dict.get_stats()
    top_words = freq_dict.get_top_words(5)
    elapsed = time.time() - start_time

    print(f"\nРезультаты:")
    print(f"  Время обработки: {elapsed:.4f} секунд")
    print(f"  Всего слов: {stats['total_words']:,}")
    print(f"  Уникальных слов: {stats['unique_words']}")
    print(f"  Топ-5 слов:")
    for word, count, percent in top_words:
        print(f"    '{word}': {count:,} ({percent:.2f}%)")


# ========== ЗАПУСК ПРОГРАММЫ ==========
if __name__ == "__main__":
    print("\n" + "=" * 80)
    print("ЗАДАНИЕ 9: ЧАСТОТНЫЙ СЛОВАРЬ")
    print("=" * 80)

    test_frequency_dictionary()
    analyze_real_text()
    benchmark_hash_functions()

    print("\n" + "=" * 80)
    print("РАБОТА ЗАВЕРШЕНА УСПЕШНО")
    print("=" * 80)