def cir(num):
    if num == 1:
        return ['*']
    
    S = cir(num // 3)
    L = []

    for i in S:
        L.append(i * 3)
    for i in S:
        L.append(i + ' ' * (num // 3) + i)
    for i in S:
        L.append(i * 3)

    return L

print('\n'.join(cir(int(input()))))