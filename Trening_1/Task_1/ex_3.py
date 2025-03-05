
a = int(input())
b = int(input())
c = int(input())

def coren(a, b, c):
    if c < 0:
        return 'NO SOLUTION'
    elif a == 0:
        if b == c ** 2:
            return 'MANY SOLUTIONS'
        else:
            return 'NO SOLUTION'

    elif (c ** 2 - b) % a == 0:
        return (c ** 2 - b) // a
    else:
        return 'NO SOLUTION'

print(coren(a, b, c))