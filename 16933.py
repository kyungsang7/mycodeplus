from collections import deque

x_list, y_list = [0, 0, 1, -1], [1, -1, 0, 0]

N, M, K = map(int,input().split())
room = list(list(map(int,input())) for _ in range(N))
visited = [[[float('inf')] * M for _ in range(N)] for _ in range(11)]
queue = deque([(0, 0, 0, 1)])
ans = float('inf')

while queue:
    x, y, wall, count = queue.popleft()

    if wall > K or visited[wall][x][y] <= count:
        continue

    visited[wall][x][y] = count

    for i in range(4):
        nx, ny = x + x_list[i], y + y_list[i]

        if 0 <= nx < N and 0 <= ny < M:
            if room[nx][ny] == 1:
                if count % 2 == 1:
                    queue.append((nx, ny, wall + 1, count + 1))
                else:
                    queue.append((nx, ny, wall + 1, count + 2))
            else:
                queue.append((nx, ny, wall, count + 1))

for i in range(11):
    ans = min(ans, visited[i][N - 1][M - 1])

if ans == float('inf'):
    print(-1)
else:
    print(ans)