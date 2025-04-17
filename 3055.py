from collections import deque

N, M = map(int,input().split())
board = list(list(input()) for _ in range(N))
visited = [[False] * M for _ in range(N)]
x_list, y_list = [0, 0, 1, -1], [1, -1, 0, 0]

S_queue = deque()
water_queue = deque()

for i in range(N):
    for j in range(M):
        if board[i][j] == 'S':
            S_queue.append((i, j, 0))
            visited[i][j] = True

        if board[i][j] == '*':
            water_queue.append((i, j))

while S_queue:
    for _ in range(len(S_queue)):
        x, y, time = S_queue.popleft()

        if board[x][y] == 'D':
            print(time)
            exit()

        if board[x][y] == '*':
            continue

        for i in range(4):
            nx, ny = x + x_list[i], y + y_list[i]
            if 0 <= nx < N and 0 <= ny < M and (board[nx][ny] == '.' or board[nx][ny] == 'D') and not visited[nx][ny]:
                visited[nx][ny] = True
                S_queue.append((nx, ny, time + 1))
    
    for _ in range(len(water_queue)):
        x, y = water_queue.popleft()

        for i in range(4):
            nx, ny = x + x_list[i], y + y_list[i]
            if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == '.':
                board[nx][ny] = '*'
                water_queue.append((nx, ny))

print('KAKTUS')




