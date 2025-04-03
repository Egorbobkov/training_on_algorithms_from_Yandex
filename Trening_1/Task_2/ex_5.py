n = int(input())
arr = list(map(int, input().split()))
res = n - 1
winner = arr[0]
possible_vasya = 0

for i in range(1, n - 1):
    cur = arr[i]
    if winner < cur:
        winner = cur
        possible_vasya = 0
    else:
        if cur % 10 != 0 and cur % 5 == 0 and possible_vasya < cur and cur > arr[i + 1]:
            possible_vasya = cur

# крайний не рассмотренный случай
if winner < arr[n - 1] or possible_vasya == 0:
    res = 0
else:
    arr.sort(reverse=True)
    for i in range(n):
        if arr[i] == possible_vasya:
            res = i + 1
            break

print(res)
