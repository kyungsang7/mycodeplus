N, M = map(int,input().split())
nums = list(list(map(int,input())) for _ in range(N))
goal_nums = list(list(map(int,input())) for _ in range(N))
ans = 0

for i in range(N - 2):
    for j in range(M - 2):
        if nums[i][j] != goal_nums[i][j]:
            ans += 1
            for x in range(i, i + 3):
                for y in range(j, j + 3):
                    nums[x][y] = (nums[x][y] + 1) % 2

if nums != goal_nums:
    print(-1)
else:
    print(ans)