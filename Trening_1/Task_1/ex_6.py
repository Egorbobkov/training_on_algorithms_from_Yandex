def waiting_time(a, b, n, m):
    min_time = max(a * (n - 1) + n, b * (m - 1) + m)
    max_time = min((n - 1) * (a + 1) + 1 + 2 * a, (m - 1) * (b + 1) + 1 + 2 * b)

    if min_time > max_time:
        return -1
    return min_time, max_time

a = int(input())
b = int(input())
n = int(input())
m = int(input())

result = waiting_time(a, b, n, m)
if result == -1:
    print(-1)
else:
    print(*result)
