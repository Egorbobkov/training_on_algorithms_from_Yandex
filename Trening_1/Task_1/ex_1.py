troom, tcond = map(int, input().split())
regim = input()

if regim == 'freeze':
    print(min(troom, tcond))
elif regim == 'heat':
    print(max(troom, tcond))
elif regim == 'auto':
    print(tcond)
elif regim == 'fan':
    print(troom)

