# Выполнил: Бобков Егор БПМ-22-3
def swap(items, i, j):
    """Функция для обмена двух элементов в списке."""
    items[i], items[j] = items[j], items[i]

def generate_permutations(elements):
    """Функция для генерации всех перестановок элементов."""
    n = len(elements)  # Получаем количество элементов
    count = 0  # Счетчик количества перестановок

    def print_permutation():
        """Функция для вывода текущей перестановки."""
        nonlocal count
        count += 1
        print(f"{count}) {elements}")

    # Выводим исходную перестановку
    print_permutation()

    while True:
        j = n - 1
        while j > 0 and elements[j] < elements[j - 1]:
            j -= 1
        if j == 0:
            break  # Все перестановки сгенерированы

        l = n - 1
        while elements[l] < elements[j - 1]:
            l -= 1

        swap(elements, j - 1, l)
        elements[j:] = elements[j:][::-1]  # Переворачиваем элементы справа от j

        # Выводим текущую перестановку
        print_permutation()

# Пример использования
n = int(input("Введите количество чисел: "))
elements_list = list(range(1, n + 1))
print("Исходный список чисел:", elements_list)
generate_permutations(elements_list)
