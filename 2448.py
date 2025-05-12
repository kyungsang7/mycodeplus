def cir(num):
    if num == 3:
        return ['  *  ', ' * * ', '*****']
    
    L = cir(num // 2)
    res = []

    for i in range(num // 2):
        res.append(' ' * (num // 2) + L[i] + ' ' * (num // 2))
    
    for i in range(num // 2):
        res.append(L[i] + ' ' + L[i])
    
    return res

N = int(input())
res = cir(N)

for i in range(N):
    print(''.join(map(str, res[i])))