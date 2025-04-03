def color(color_ann, color_bor):
    set_1 = set(color_ann)
    set_2 = set(color_bor)

    first = sorted(set_1 & set_2)
    second = sorted(set_1 - set_2)
    third = sorted(set_2 - set_1)

    print(len(first))
    print(*first)
    print(len(second))
    print(*second)
    print(len(third))
    print(*third)


n, m = map(int, input().split())
color_ann = [int(input()) for _ in range(n)]
color_bor = [int(input()) for _ in range(m)]
color(color_ann, color_bor)