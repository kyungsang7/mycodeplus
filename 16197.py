from collections import deque

def judge(x, y):
    if 0 <= x < N and 0 <= y < M:
        if board[x][y] == '#':
            return False, True
        else:
            return False, False
    else:
        return True, False
    
x_list, y_list = [0, 0, 1, -1], [1, -1, 0, 0]
coins = []
queue = deque()

N, M = map(int,input().split())
board = list(list(input()) for _ in range(N))
for i in range(N):
    for j in range(M):
        if board[i][j] == 'o':
            coins.append(i)
            coins.append(j)

queue.append(coins + [1])

while queue:
    x1, y1, x2, y2, count = queue.popleft()
    if count > 10:
        print(-1)
        break
    
    for i in range(4):
        nx1, ny1, nx2, ny2 = x1 + x_list[i], y1 + y_list[i], x2 + x_list[i], y2 + y_list[i]

        j1_out, j1_wall = judge(nx1, ny1)
        j2_out, j2_wall = judge(nx2, ny2)

        if j1_out or j2_out:
            if j1_out and j2_out:
                continue
            print(count)
            exit()
            break

        if j1_wall:
            nx1, ny1 = x1, y1
        
        if j2_wall:
            nx2, ny2 = x2, y2
        
        queue.append((nx1, ny1, nx2, ny2, count + 1))