N = int(input())
operation = input()
adj_proc = [[0] * N for _ in range(N)]

p = 0
nums = [0] * (N)

for i in range(N):
    for j in range(i, N):
        if operation[p] == '+':
            adj_proc[i][j] = 1
        elif operation[p] == '-':
            adj_proc[i][j] = -1
        p += 1

def make_nums(num):
    if num == N:
        return True
    
    if adj_proc[num][num] == 0:
        nums[num] = 0
        return make_nums(num + 1)
    
    else:
        for i in range(1,11):
            nums[num] = i * adj_proc[num][num]
            if check(num) and make_nums(num + 1):
                return True
        return False

def check(num):
    s_num = 0
    for i in range(num, -1, -1):
        s_num += nums[i]
        if adj_proc[i][num] == 0 and s_num != 0:
            return False
        elif adj_proc[i][num] > 0 and not s_num > 0:
            return False
        elif adj_proc[i][num] < 0 and not s_num < 0:
            return False
    return True

make_nums(0)
print(*nums)