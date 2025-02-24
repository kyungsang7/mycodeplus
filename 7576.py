from collections import deque
queue = deque()
x_list, y_list = [0, 0, -1, 1], [1, -1, 0, 0]

M, N = map(int,input().split())
tomato = []

for i in range(N):
    tomato.append(list(map(int,input().split())))

for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            queue.append((i, j))

while queue:
    x, y = queue.popleft()
    for i in range(4):
        n_x, n_y = x + x_list[i], y + y_list[i]
        if 0 <= n_x < N and 0 <= n_y < M:
            if not tomato[n_x][n_y] or tomato[n_x][n_y] > tomato[x][y] + 1:
                tomato[n_x][n_y] = tomato[x][y] + 1
                queue.append((n_x, n_y))

max_num = 0
ans = 0

for i in tomato:
    max_num = max(max_num, max(i))
    if 0 in i:
        ans = -1

if ans == -1:
    print(ans)
else:
    print(max_num - 1)