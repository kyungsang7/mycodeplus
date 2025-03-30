def _1():
    n_nums = [[0] * (M) for _ in range(N)]

    for i in range(N):
        for j in range(M):
            n_nums[N - i - 1][j] = nums[i][j]

    return n_nums

def _2():
    n_nums = [[0] * (M) for _ in range(N)]

    for i in range(N):
        for j in range(M):
            n_nums[i][M - j - 1] = nums[i][j]
    
    return n_nums

def _3():
    global N, M

    n_nums = [[0] * (N) for _ in range(M)]

    for i in range(N):
        for j in range(M):
            n_nums[j][N - i - 1] = nums[i][j]
    
    N, M = M ,N
    
    return n_nums

def _4():
    global N, M

    n_nums = [[0] * (N) for _ in range(M)]

    for i in range(N):
        for j in range(M):
            n_nums[M - j - 1][i] = nums[i][j]
    
    N, M = M ,N
    
    return n_nums

def _5():
    n_nums = [[0] * (M) for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if 0 <= i < N // 2 and 0 <= j < M // 2:
                n_nums[i][j + M // 2] = nums[i][j]
            elif 0 <= i < N // 2 and M // 2 <= j:
                n_nums[i + N // 2][j] = nums[i][j]
            elif N // 2 <= i and M // 2 <= j:
                n_nums[i][j - M // 2] = nums[i][j]
            else:
                n_nums[i - N // 2][j] = nums[i][j]
    
    return n_nums

def _6():
    n_nums = [[0] * (M) for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if 0 <= i < N // 2 and 0 <= j < M // 2:
                n_nums[i + N // 2][j] = nums[i][j]
            elif 0 <= i < N // 2 and M // 2 <= j:
                n_nums[i][j - M // 2] = nums[i][j]
            elif N // 2 <= i and M // 2 <= j:
                n_nums[i - N // 2][j] = nums[i][j]
            else:
                n_nums[i][j - M // 2] = nums[i][j]
    
    return n_nums

N, M, R = map(int,input().split())
nums = [list(map(int,input().split())) for _ in range(N)]
s = list(map(int,input().split()))

for n in s:
    if n == 1:
        nums = _1()
    elif n == 2:
        nums = _2()
    elif n == 3:
        nums = _3()
    elif n == 4:
        nums = _4()
    elif n == 5:
        nums = _5()
    elif n == 6:
        nums = _6()

for i in nums:
    print(*i)