x_list, y_list = [0, 0, 1, -1], [1, -1, 0, 0]

def DFS(x, y, count):
    global ans

    if x == x_goal and y == y_goal and count >= 4:
        ans = "Yes"
        return

    for i in range(4):
        nx, ny = x + x_list[i], y + y_list[i]
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and game_map[nx][ny] == game_map[x][y]:
            visited[nx][ny] = True
            DFS(nx, ny, count + 1)
            visited[nx][ny] = False
    

N, M = map(int,input().split())
game_map = list(list(input()) for _ in range(N))
visited = list([False] * M for _ in range(N))
ans = "No"

for i in range(N):
    for j in range(M):

        if ans == "Yes":
            continue

        x_goal, y_goal = i, j
        DFS(i, j, 0)

print(ans)