N = int(input())
colors = list(list(input()) for _ in range(N))

def count():
    global ans1, ans2
    for i in range(N):
        res = 1
        for j in range(1, N):
            if colors[i][j] == colors[i][j-1]:
                res += 1
            else:
                res = 1
            ans1 = max(res, ans1)
    
    for i in range(N):
        res = 1
        for j in range(1, N):
            if colors[j][i] == colors[j-1][i]:
                res += 1
            else:
                res = 1
            ans2 = max(ans2, res)

ans1, ans2 = 1, 1

for i in range(N):
    for j in range(N):
        if i != N-1:
            colors[i][j], colors[i+1][j] = colors[i+1][j], colors[i][j]
            count()
            colors[i][j], colors[i+1][j] = colors[i+1][j], colors[i][j]
        if j != N-1:
            colors[i][j], colors[i][j+1] = colors[i][j+1], colors[i][j]
            count()
            colors[i][j], colors[i][j+1] = colors[i][j+1], colors[i][j]

print(max(ans1,ans2))