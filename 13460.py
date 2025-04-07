from collections import deque

def get_location(x, y, p_x, p_y):
    nx, ny = x + p_x, y + p_y

    if bord[nx][ny] == 'O':
        return nx, ny

    if bord[nx][ny] == '#':
        return x, y
    
    return get_location(nx, ny, p_x, p_y)

x_list, y_list = [0, 0, 1, -1], [-1, 1, 0, 0]

N, M = map(int,input().split())
bord = list(list(input()) for _ in range(N))

for i in range(N):
    for j in range(M):
        if bord[i][j] == 'R':
            Rx, Ry = i, j
        elif bord[i][j] == 'B':
            Bx, By = i, j

queue = deque([(Rx, Ry, Bx, By, 0)])

while queue:
    Rx, Ry, Bx, By, count = queue.popleft()

    if count > 10:
        print(-1)
        break

    if bord[Bx][By] == 'O':
        continue

    if bord[Rx][Ry] == 'O':
        print(count)
        break

    for i in range(4):
        nRx, nRy = get_location(Rx, Ry, x_list[i], y_list[i])
        nBx, nBy = get_location(Bx, By, x_list[i], y_list[i])
        if i == 0:
            if nRx == nBx and nRy == nBy and bord[nBx][nBy] != 'O':
                if Ry < By:                    
                    nBx -= x_list[i]
                    nBy -= y_list[i]
                else:
                    nRx -= x_list[i]
                    nRy -= y_list[i]

        elif i == 1:
            if nRx == nBx and nRy == nBy and bord[nBx][nBy] != 'O':
                if Ry > By:                    
                    nBx -= x_list[i]
                    nBy -= y_list[i]
                else:
                    nRx -= x_list[i]
                    nRy -= y_list[i]

        elif i == 2:
            if nRx == nBx and nRy == nBy and bord[nBx][nBy] != 'O':
                if Rx > Bx:                    
                    nBx -= x_list[i]
                    nBy -= y_list[i]
                else:
                    nRx -= x_list[i]
                    nRy -= y_list[i]

        elif i == 3:
            if nRx == nBx and nRy == nBy and bord[nBx][nBy] != 'O':
                if Rx < Bx:                    
                    nBx -= x_list[i]
                    nBy -= y_list[i]
                else:
                    nRx -= x_list[i]
                    nRy -= y_list[i]

        queue.append((nRx, nRy, nBx, nBy, count + 1))
