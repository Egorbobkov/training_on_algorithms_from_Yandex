def count_detail(N, K, M):
    if M > K:
        return 0

    total = 0
    metal = N

    while metal >= K:
        count_blank = metal // K
        remains_metal = metal % K

        count_details = (K // M) * count_blank
        remains_metal_details = (K % M) * count_blank

        total += count_details
        metal = remains_metal + remains_metal_details

    return total

N, K, M = map(int, input().split())

print(count_detail(N, K, M))


