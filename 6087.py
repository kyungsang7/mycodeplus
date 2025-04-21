from collections import deque

W, H = map(int,input().split())
board = list(list(input()) for _ in range(H))
visited = [[[float('inf')] * W for _ in range(H)] for _ in range(4)]
C = []

x_list, y_list = [-1, 0, 1, 0], [0, 1, 0, -1]

queue = deque()
for i in range(H):
    for j in range(W):
        if board[i][j] == 'C':
            C.append((i, j))

queue.append((C[0][0], C[0][1], -1, 5))

x, y, count, direction = queue.popleft()
for i in range(4):
    nx, ny = x + x_list[i], y + y_list[i]
    if 0 <= nx < H and 0 <= ny < W and board[nx][ny] == '.':
        visited[i][nx][ny] = 0
        queue.append((nx, ny, 0, i))

while queue:
    x, y, count, direction = queue.popleft()

    for i in [(direction + 3) % 4, direction, (direction + 1) % 4]:
        nx, ny = x + x_list[i], y + y_list[i]

        if 0 <= nx < H and 0 <= ny < W and board[nx][ny] != '*':
            if direction == i:
                if visited[i][nx][ny] > count:
                    visited[i][nx][ny] = count
                    queue.append((nx, ny, count, direction))

            else:
                if visited[i][nx][ny] > count + 1:
                    visited[i][nx][ny] = count + 1
                    queue.append((nx, ny, count + 1, i))

c1 = C[1]
ans = float('inf')
for i in range(4):
    ans = min(ans, visited[i][c1[0]][c1[1]])

print(ans)