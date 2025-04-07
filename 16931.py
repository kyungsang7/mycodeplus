N, M = map(int,input().split())
nums = list(list(map(int,input().split())) for _ in range(N))
ans = N * M * 2

x_list, y_list = [0, 0, 1, -1], [1, -1, 0, 0]

for i in range(N):
    for j in range(M):
        for s in range(4):
            nx, ny = i + x_list[s], j + y_list[s]
            if 0 <= nx < N and 0 <= ny < M:
                if nums[nx][ny] < nums[i][j]:
                    ans += nums[i][j] - nums[nx][ny]
            else:
                ans += nums[i][j]

print(ans)