import sys
input = sys.stdin.readline

def circulation(count, rec):
    global max_ans, min_ans
    if count == N:
        max_ans = max(max_ans, rec)
        min_ans = min(min_ans, rec)
        return

    for i in range(4):
        if operations[i] != 0:
            if i == 0:
                operations[i] -= 1
                circulation(count + 1, rec + nums[count])
                operations[i] += 1

            elif i == 1:
                operations[i] -= 1
                circulation(count + 1, rec - nums[count])
                operations[i] += 1

            elif i == 2:
                operations[i] -= 1
                circulation(count + 1, rec * nums[count])
                operations[i] += 1

            elif i == 3:
                operations[i] -= 1
                circulation(count + 1, int(rec / nums[count]))
                operations[i] += 1
        

N = int(input())
nums = list(map(int,input().split()))
operations = list(map(int,input().split()))

max_ans = -float('inf')
min_ans = float('inf')

circulation(1, nums[0])

print(max_ans)
print(min_ans)