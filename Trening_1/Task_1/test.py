def domino_game(K, N, dominoes):
    lena_score = 0
    sasha_score = 0

    for value in dominoes:
        is_div_3 = value % 3 == 0
        is_div_5 = value % 5 == 0

        if is_div_3 and is_div_5:
            continue
        elif is_div_5:
            lena_score += 1
        elif is_div_3:
            sasha_score += 1

        if lena_score >= K:
            return "Lena"
        if sasha_score >= K:
            return "Sasha"

    if lena_score > sasha_score:
        return "Lena"
    elif sasha_score > lena_score:
        return "Sasha"
    else:
        return "Draw"

K, N = map(int, input().split())
dominoes = list(map(int, input().split()))

print(domino_game(K, N, dominoes))
