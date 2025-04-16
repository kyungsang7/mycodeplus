from collections import deque

N, M, K = map(int,input().split())
room = list(list(map(int,input())) for _ in range(N))
visited = [[[False] * M for _ in range(N)] for _ in range(11)]
ans = -1

queue = deque([(0, 0, 1, 0)])

n_list = [[0, 1], [0, -1], [1, 0], [-1, 0]]

while queue:
    x, y, dist, walls = queue.popleft()
    
    if walls > K or visited[walls][x][y]:
        continue

    if x == N - 1 and y == M - 1:
        ans = dist
        break

    visited[walls][x][y] = True

    for i, j in n_list:
        nx, ny = x + i, y + j

        if 0 <= nx < N and 0 <= ny < M and not visited[walls][nx][ny]:

            if room[nx][ny] == 1:
                if walls < K:
                    queue.append((nx, ny, dist + 1, walls + 1))

            else:
                queue.append((nx, ny, dist + 1, walls))

print(ans)




