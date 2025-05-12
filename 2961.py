N = int(input())
ing = list(list(map(int,input().split())) for _ in range(N))
ans = float('inf')

for i in range(1, 1 << N):
    sower, bitter = 1, 0
    for j in range(N):
        if i & 1 << j:
            sower *= ing[j][0]
            bitter += ing[j][1]

    ans = min(ans, abs(sower - bitter))

print(ans)