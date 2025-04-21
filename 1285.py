N = int(input())
board = [list(input().strip()) for _ in range(N)]

# H = 0, T = 1로 변환
for i in range(N):
    for j in range(N):
        board[i][j] = 1 if board[i][j] == 'T' else 0

min_t = N * N

# 모든 행 뒤집기 조합 (2^N)
for mask in range(1 << N):
    temp = [row[:] for row in board]

    # 행 뒤집기
    for i in range(N):
        if mask & (1 << i):
            for j in range(N):
                temp[i][j] ^= 1

    # 열 뒤집기: 열마다 'T' 개수가 더 많으면 뒤집는 게 이득
    total = 0
    for j in range(N):
        t_count = sum(temp[i][j] for i in range(N))
        total += min(t_count, N - t_count)

    min_t = min(min_t, total)

print(min_t)
