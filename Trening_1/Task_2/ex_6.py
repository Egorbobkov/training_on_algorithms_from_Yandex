def find_min_addition(n, sequence):
    if sequence == sequence[::-1]:
        return 0, []

    for i in range(n):
        new_sequence = sequence + sequence[:i][::-1]
        if new_sequence == new_sequence[::-1]:
            return i, sequence[:i][::-1]

    return n - 1, sequence[:-1][::-1]


n = int(input())
sequence = list(map(int, input().split()))
m, to_add = find_min_addition(n, sequence)

print(m)
if m > 0:
    print(' '.join(map(str, to_add)))
