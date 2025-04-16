N, M = map(int,input().split())
x, y, direction = map(int,input().split())
room = list(list(map(int,input().split())) for _ in range(N))
visited = [[False] * M for _ in range(N)]

if direction == 1:
    direction = 3

elif direction == 3:
    direction = 1

directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
ans = 0

while True:
    if room[x][y] == 0 and not visited[x][y]:
        ans += 1
        visited[x][y] = True
    
    for i, j in directions[direction + 1 : 4] + directions[: direction + 1]:
        nx, ny = x + i, y + j
        direction = (direction + 1) % 4

        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and room[nx][ny] == 0:
            x, y = nx, ny
            break
    
    else:
        if room[x - directions[direction][0]][y - directions[direction][1]] == 0:
            x, y = x - directions[direction][0], y - directions[direction][1]
        
        else:
            break

print(ans)

        



