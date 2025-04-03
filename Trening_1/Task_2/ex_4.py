def max_value(numbers):
    count = 0
    for i in range(1, len(numbers) - 1):
        if numbers[i] > numbers[i - 1] and numbers[i] > numbers[i + 1]:
            count += 1
    return count


numbers = list(map(int, input().split()))
print(max_value(numbers))
