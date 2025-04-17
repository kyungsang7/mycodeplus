from collections import deque

x_list, y_list = [0, 0, 1, -1], [1, -1, 0, 0]

N, M, K = map(int,input().split())
room = list(list(map(int,input())) for _ in range(N))
visited = [[[False] * M for _ in range(N)] for _ in range(11)]
queue = deque([(0, 0, 0, 1)])
ans = -1

while queue:
    x, y, wall, count = queue.popleft()

    if x == N - 1 and y == M - 1:
        ans = count
        break

    for i in range(4):
        nx, ny = x + x_list[i], y + y_list[i]

        if 0 <= nx < N and 0 <= ny < M:
            if room[nx][ny] == 1 and wall < K and not visited[wall][nx][ny]:
                if count % 2 == 1:
                    visited[wall][nx][ny] = True
                    queue.append((nx, ny, wall + 1, count + 1))
                else:
                    queue.append((x, y, wall, count + 1))

            elif room[nx][ny] == 0 and not visited[wall][nx][ny]:
                visited[wall][nx][ny] = True
                queue.append((nx, ny, wall, count + 1))

print(ans)