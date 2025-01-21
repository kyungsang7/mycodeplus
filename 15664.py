import copy

a,b = map(int,input().split())
nums = sorted(list(map(int,input().split())))

ans_list = []
ans = []

def DFS(num):
    global ans, ans_list
    if len(ans) == b and not ans in ans_list:
        ans_list.append(copy.deepcopy(ans))
        return

    for i in range(num, a):
        ans.append(nums[i])
        DFS(i + 1)
        ans.pop()

DFS(0)

for i in ans_list:
    print(*i)