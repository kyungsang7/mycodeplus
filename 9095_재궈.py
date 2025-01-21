def DFS():
    global nums, ans
    n_sum = sum(nums)
    if n_sum >= N:
        if n_sum == N:
            ans += 1
        return
    
    for i in range(1, 4):
        nums.append(i)
        DFS()
        nums.pop()

for _ in range(int(input())):
    N = int(input())
    nums = []
    ans = 0

    DFS()

    print(ans)