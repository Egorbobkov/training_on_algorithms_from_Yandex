def max_product(sequence):
    max_1 = max_2 = float('-inf')
    min_1 = min_2 = float('inf')

    for i in range(len(sequence)):
        if sequence[i] > max_1:
            max_2 = max_1
            max_1 = sequence[i]
        elif sequence[i] > max_2:
            max_2 = sequence[i]

        if sequence[i] < min_1:
            min_2 = min_1
            min_1 = sequence[i]
        elif sequence[i] < min_2:
            min_2 = sequence[i]

    if max_1 * max_2 >= min_1 * min_2:
        return max_2, max_1
    else:
        return min_1, min_2


sequence = list(map(int, input().split()))
print(*max_product(sequence))