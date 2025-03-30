H, W, X, Y = map(int,input().split())

nums = list(list(map(int,input().split())) for _ in range(H + X))

for i in range(X, H):
    for j in range(Y, W):
        nums[i][j] -= nums[i - X][j - Y]

for i in nums[:H]:
    print(*i[:W])