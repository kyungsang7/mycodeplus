def DFS(count):
    global recent, ans
    if count == K:
        ans = max(ans, recent)
        return
    
    for i in range(N):
        for j in range(M):
            if not visited[i][j]:
                flag = True
                for s in range(4):
                    nx, ny = i + x_list[s], j + y_list[s]
                    if 0 <= nx < N and 0 <= ny < M:
                        if visited[nx][ny]:
                            flag = False
                if flag:
                    visited[i][j] = True
                    recent += nums[i][j]
                    DFS(count + 1)
                    visited[i][j] = False
                    recent -= nums[i][j]


N, M, K = map(int,input().split())
nums = list(list(map(int,input().split())) for _ in range(N))
visited = [[False] * (M + 1) for _ in range(N + 1)]
x_list, y_list = [0, 0, 1, -1], [1, -1, 0, 0]
ans = -1e6
recent = 0

DFS(0)

print(ans)