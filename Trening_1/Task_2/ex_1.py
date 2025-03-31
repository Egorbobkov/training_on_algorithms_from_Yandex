def mono_up(number):
    for i in range(1, len(number)):
        if number[i] <= number[i - 1]:
            return 'NO'
    return 'YES'

number = list(map(int, input().split()))
print(mono_up(number))
