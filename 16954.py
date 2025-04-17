bord = list(list(input()) for _ in range(8))
location = [(7, 0)]
visited = [[False] * 8 for _ in range(8)]
x_list, y_list = [1, 1, 1, 0, 0, 0, -1, -1, -1], [-1, 0, 1, 1, 0, -1, 1, 0, -1]

while location:
    new_location = []

    for x, y in location:
        if x == 0 and  y == 7:
            print(1)
            exit()

        if bord[x][y] == '#':
            continue

        visited[x][y] = True

        for i in range(9):
            nx, ny = x + x_list[i], y + y_list[i]
            if 0 <= nx < 8 and 0 <= ny < 8:
                if x == nx and  y == ny:
                    if bord[nx][ny] == '.':
                        new_location.append((nx, ny))
                        
                elif not visited[nx][ny]:
                    if bord[nx][ny] == '.':
                        new_location.append((nx, ny))
    
    for i in range(7, 0, -1):
        bord[i] = bord[i - 1]

    bord[0] = ['.'] * 8

    location = new_location[::]

print(0)

