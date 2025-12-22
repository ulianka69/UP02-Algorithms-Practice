"""
Задание 14: Задача "Острова"
Дан двумерный массив 0/1. Найти количество "островов" (компонент связности).
Использовать DFS или BFS.
"""


def count_islands(grid):
    """
    Подсчет количества островов в двумерной сетке.

    Остров — группа смежных 1 (по горизонтали/вертикали).
    Используется DFS для "затопления" острова.

    Сложность: O(m * n), где m, n — размеры сетки
    """
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    islands = 0

    def dfs(r, c):
        """DFS для затопления острова."""
        if (r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0):
            return
        grid[r][c] = 0  # "затопляем" клетку
        # Рекурсивно затапливаем соседей
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                islands += 1
                dfs(r, c)  # Затопляем весь остров

    return islands


def test_islands():
    """Тестирование задачи островов."""
    print("=== Задача 'Острова' ===")

    # Тест 1: базовый случай
    grid1 = [
        [1, 1, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 1]
    ]
    print("1. Тестовая сетка 1:")
    for row in grid1:
        print("   " + " ".join(str(x) for x in row))
    result1 = count_islands([row[:] for row in grid1])  # копия
    print(f"   Количество островов: {result1}")

    # Тест 2: один большой остров
    grid2 = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]
    result2 = count_islands([row[:] for row in grid2])
    print(f"\n2. Единый остров с озером: {result2} остров")

    # Тест 3: все вода
    grid3 = [[0, 0, 0], [0, 0, 0]]
    result3 = count_islands(grid3)
    print(f"\n3. Только вода: {result3} островов")

    # Тест 4: все суша
    grid4 = [[1, 1], [1, 1]]
    result4 = count_islands(grid4)
    print(f"\n4. Только суша: {result4} остров")

    print("\nСложность:")
    print("  Время: O(m * n) — посещаем каждую клетку 1 раз")
    print("  Память: O(m * n) — в худшем случае (рекурсия для полного острова)")


if __name__ == "__main__":
    print("\n" + "=" * 80)
    print("ЗАДАНИЕ 14: ЗАДАЧА 'ОСТРОВА'")
    print("=" * 80)
    test_islands()
    print("\n" + "=" * 80)
    print("РАБОТА ЗАВЕРШЕНА УСПЕШНО")
    print("=" * 80)