def sequence(number_: list) -> str:
    if not number_:  # Если нет чисел (ввод сразу -2000000000)
        return 'RANDOM'

    if len(set(number_)) == 1:
        return 'CONSTANT'

    is_ascending = True           # Строго возрастающая
    is_weakly_ascending = True    # Нестрого возрастающая (можно равные)
    is_descending = True          # Строго убывающая
    is_weakly_descending = True   # Нестрого убывающая (можно равные)

    for i in range(1, len(number_)):
        prev, curr = number_[i - 1], number_[i]
        if curr > prev:
            is_descending = False
            is_weakly_descending = False
        elif curr < prev:
            is_ascending = False
            is_weakly_ascending = False
        else:  # curr == prev
            is_ascending = False
            is_descending = False

    if is_ascending:
        return 'ASCENDING'
    elif is_weakly_ascending:
        return 'WEAKLY ASCENDING'
    elif is_descending:
        return 'DESCENDING'
    elif is_weakly_descending:
        return 'WEAKLY DESCENDING'

    return 'RANDOM'


number = []
while True:
    num = int(input())
    if num == -2000000000:
        break
    number.append(num)

print(sequence(number))