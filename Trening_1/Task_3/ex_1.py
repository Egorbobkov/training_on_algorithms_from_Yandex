def uniq_value(sequence):
    space = set()
    for num in sequence:
        space.add(num)

    return len(space)


sequence = list(map(int, input().split()))
print(uniq_value(sequence))
