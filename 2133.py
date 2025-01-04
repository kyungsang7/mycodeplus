res = [0] * 31
res[2] = 3
for i in range(4, 31, 2):
    for j in range(i-1,0,-1):
        if res[i] == 0:
            res[i] += res[j] * 3
        else:
            res[i] += res[j] * 2
    res[i] += 2
print(res[int(input())])