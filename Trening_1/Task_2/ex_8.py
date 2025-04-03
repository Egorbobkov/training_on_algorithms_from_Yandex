def max_product_of_three(sequence):
    max_1 = max_2 = max_3 = float('-inf')
    min_1 = min_2 = float('inf')

    for i in range(len(sequence)):
        if sequence[i] > max_1:
            max_3 = max_2
            max_2 = max_1
            max_1 = sequence[i]
        elif sequence[i] > max_2:
            max_3 = max_2
            max_2 = sequence[i]
        elif sequence[i] > max_3:
            max_3 = sequence[i]

        if sequence[i] < min_1:
            min_2 = min_1
            min_1 = sequence[i]
        elif sequence[i] < min_2:
            min_2 = sequence[i]

    if max_1 * max_2 * max_3 >= min_1 * min_2 * max_1:
        return max_1, max_2, max_3
    else:
        return min_1, min_2, max_1


sequence = list(map(int, input().split()))
print(*max_product_of_three(sequence))
