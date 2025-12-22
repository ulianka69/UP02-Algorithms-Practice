import sys
import os


code_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'code')
sys.path.insert(0, code_path)

print(f"Добавлен в sys.path: {code_path}")


def display_menu():
    print("\n" + "=" * 70)
    print("ПРАКТИЧЕСКАЯ РАБОТА УП.02 - АЛГОРИТМЫ И ВЫЧИСЛИТЕЛЬНАЯ СЛОЖНОСТЬ")
    print("=" * 70)
    print("\nВыберите раздел для демонстрации:")
    print("1.  Массивы и связные списки (Задания 1-4)")
    print("2.  Стек и очередь (Задания 5-7)")
    print("3.  Map, HashMap, хэш-функции (Задания 8-10)")
    print("4.  Деревья и графы (Задания 11-14)")
    print("5.  Куча и приоритетные очереди (Задания 15-16)")
    print("6.  Запустить все тесты")
    print("7.  Выход")
    print("\n" + "-" * 70)


def run_arrays_linked_lists():
    print("\nРАЗДЕЛ 1: МАССИВЫ И СВЯЗНЫЕ СПИСКИ")
    try:
        from arrays_linked_lists.static_array import test_static_array
        from arrays_linked_lists.dynamic_array import test_dynamic_array, benchmark_insertion
        from arrays_linked_lists.singly_linked_list import test_singly_linked_list
        from arrays_linked_lists.doubly_linked_list import test_doubly_linked_list

        test_static_array()
        test_dynamic_array()
        benchmark_insertion(10000)
        test_singly_linked_list()
        test_doubly_linked_list()
    except Exception as e:
        print(f"Ошибка: {e}")


def run_stack_queue():
    print("\nРАЗДЕЛ 2: СТЕК И ОЧЕРЕДЬ")
    try:
        from stack_queue.stack_array import test_stack_and_parentheses
        from stack_queue.stack_linked_list import test_stack_linked_list
        from stack_queue.circular_queue import test_circular_queue
        from stack_queue.queue_two_stacks import test_queue_two_stacks
        from stack_queue.calculator_rpn import test_calculator

        test_stack_and_parentheses()
        test_stack_linked_list()
        test_circular_queue()
        test_queue_two_stacks()
        test_calculator()
    except Exception as e:
        print(f"Ошибка: {e}")


def run_hashmap_trie():
    print("\nРАЗДЕЛ 3: HASHMAP, TRIE И ХЭШ-ФУНКЦИИ")
    try:
        from hashmap_trie.hash_table import test_hash_table
        from hashmap_trie.frequency_dictionary import test_frequency_dictionary, analyze_real_text
        from hashmap_trie.trie_autocomplete import test_trie_autocomplete

        test_hash_table()
        test_frequency_dictionary()
        analyze_real_text()
        test_trie_autocomplete()
    except Exception as e:
        print(f"Ошибка: {e}")


def run_trees_graphs():
    print("\nРАЗДЕЛ 4: ДЕРЕВЬЯ И ГРАФЫ")
    try:
        from trees_graphs.binary_search_tree import test_binary_search_tree
        from trees_graphs.trie_advanced import test_trie_advanced
        from trees_graphs.graph_representations import compare_graph_representations
        from trees_graphs.graph_algorithms import test_graph_algorithms
        from trees_graphs.islands_problem import test_islands

        test_binary_search_tree()
        test_trie_advanced()
        compare_graph_representations()
        test_graph_algorithms()
        test_islands()
    except Exception as e:
        print(f"Ошибка: {e}")


def run_heap_priority_queue():
    print("\nРАЗДЕЛ 5: КУЧА И ПРИОРИТЕТНЫЕ ОЧЕРЕДИ")
    try:
        from heap_priority_queue.binary_heap import test_min_heap
        from heap_priority_queue.priority_queue import test_priority_queue, task_scheduling

        test_min_heap()
        test_priority_queue()
        task_scheduling()
    except Exception as e:
        print(f"Ошибка: {e}")


def run_all_tests():
    run_arrays_linked_lists()
    run_stack_queue()
    run_hashmap_trie()
    run_trees_graphs()
    run_heap_priority_queue()
    print("\n✅ ВСЕ ТЕСТЫ УСПЕШНО ЗАВЕРШЕНЫ!")


def main():
    print("Добро пожаловать в практическую работу по алгоритмам!")

    while True:
        display_menu()
        try:
            choice = input("\nВаш выбор (1-7): ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nВыход.")
            return

        if choice == "1":
            run_arrays_linked_lists()
        elif choice == "2":
            run_stack_queue()
        elif choice == "3":
            run_hashmap_trie()
        elif choice == "4":
            run_trees_graphs()
        elif choice == "5":
            run_heap_priority_queue()
        elif choice == "6":
            run_all_tests()
        elif choice == "7":
            print("До свидания!")
            break
        else:
            print("Неверный выбор. Введите число от 1 до 7.")


if __name__ == "__main__":
    main()