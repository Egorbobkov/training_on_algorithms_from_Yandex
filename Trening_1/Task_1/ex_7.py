def salve_castle(A, B, C, D, E):
    if (A <= D and B <= E) or (A <= E and B <= D):
        return 'YES'
    if (A <= D and C <= E) or (A <= E and C <= D):
        return 'YES'
    if (B <= D and C <= E) or (B <= E and C <= D):
        return 'YES'
    else:
        return 'NO'

A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
print(salve_castle(A, B, C, D, E))