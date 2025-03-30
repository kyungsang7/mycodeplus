from collections import deque
queue = deque([(0, 0)])

x_list, y_list = [0, 0, 1, -1], [1, -1, 0, 0]

M, N = map(int,input().split())
maze = list(list(map(int, input().strip())) for _ in range(N))
visited = [[10000] * M for _ in range(N)]
visited[0][0] = 0

while queue:
    x, y = queue.popleft()

    for i in range(4):
        nx, ny = x + x_list[i], y + y_list[i]

        if 0 <= nx < N and 0 <= ny < M:
            if visited[x][y] + maze[nx][ny] < visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + maze[nx][ny]
                queue.append((nx, ny))

print(visited[N - 1][M - 1])
