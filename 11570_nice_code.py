counts = [[1] * 10 for _ in range(1001)]
for i in range(1,1001):
    for j in range(1,10):
        counts[i][j] = (counts[i][j-1] + counts[i-1][j]) % 10007
print(counts[int(input())][9] % 10007)