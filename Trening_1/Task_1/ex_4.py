def min_size_table(a, b, c, d):
    parametrs = [
        (a + c, max(b, d)),
        (b + d, max(a, c)),
        (max(a, c), b + d),
        (max(b, d), a + c),
        (a + d, max(b, c)),
        (b + c, max(a, d))
    ]

    best_widht, best_height = min(parametrs, key=lambda x: x[0] * x[1])
    print(best_widht, best_height)

a, b, c, d = map(int, input().split())

min_size_table(a, b, c, d)