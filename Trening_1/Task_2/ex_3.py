def min_dist(n, arr, x):
    return min(arr, key=lambda num: abs(num - x))

n = int(input())
arr = list(map(int, input().split()))
x = int(input())

print(min_dist(n, arr, x))