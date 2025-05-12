def check_upper(idx):
    for i in range(L, N):
        if board[idx][i] == board[idx][i - 1]:
            continue

        elif board[idx][i] == board[idx][i - 1] + 1:
            for j in range(i - L, L):
                if board[idx][j] != board[idx][i - 1]:
                    return False
                else:
                    upper[j] = 1
        else:
            return False
    
    return True

def check_lower(idx):
    for i in range(N - L - 1, -1, -1):
        if board[idx][i] == board[idx][i + 1]:
            continue

        elif board[idx][i] == board[idx][i + 1] + 1:
            for j in range(i + 1, i + L - 1):
                if board[idx][j] != board[idx][i + 1]:
                    return False
                else:
                    lower[j] = 1
        else:
            return False
    
    return True


N, L = map(int,input().split())
board = list(list(map(int,input().split())) for _ in range(N))
visited = [[False] * N for _ in range(N)]
ans = 0

for i in range(N):
    upper, lower = [0] * N, [0] * N
    u, l = check_upper(i), check_lower(i)

    flag = True

    if u and l:
        for i in range(N):
            if upper[i] == lower[i] == 1:
                flag = False
                break
    
    else:
        flag = False
    
    if flag:
        ans += 1
print(ans)



