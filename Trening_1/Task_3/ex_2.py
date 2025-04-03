def dub_value(a, b):
    return sorted(set(a) & set(b))


a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(*dub_value(a, b))