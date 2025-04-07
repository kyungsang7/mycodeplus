def _1():
    n_1 = dice[1]
    dice[1] = dice[4]
    dice[4] = dice[6]
    dice[6] = dice[3]
    dice[3] = n_1

def _2():
    n_1 = dice[1]
    dice[1] = dice[3]
    dice[3] = dice[6]
    dice[6] = dice[4]
    dice[4] = n_1

def _3():
    n_1 = dice[1]
    dice[1] = dice[5]
    dice[5] = dice[6]
    dice[6] = dice[2]
    dice[2] = n_1

def _4():
    n_1 = dice[1]
    dice[1] = dice[2]
    dice[2] = dice[6]
    dice[6] = dice[5]
    dice[5] = n_1


dice = [0] * 7
x_list, y_list = [0, 0, 0, -1, 1], [0, 1, -1, 0, 0]
N, M, x, y, K = map(int,input().split())
nums = list(list(map(int,input().split())) for _ in range(N))
operations = list(map(int,input().split()))

for i in operations:
    nx, ny = x + x_list[i], y + y_list[i]
    if 0 <= nx < N and 0 <= ny < M:
        if i == 1:
            _1()
        elif i == 2:
            _2()
        elif i == 3:
            _3()
        else:
            _4()
        print(dice[1])
        if nums[nx][ny] == 0:
            nums[nx][ny] = dice[6]
        else:
            dice[6] = nums[nx][ny]
            nums[nx][ny] = 0
        x, y = nx, ny

