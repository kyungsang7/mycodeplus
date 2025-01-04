nums = list(int(input()) for _ in range(9)) 
nums_sum = []

def DFS(start, depth):
    if depth == 7:
        if sum(nums_sum) == 100:
            for j in sorted(nums_sum):
                print(j)
            exit()
        else:
            return
    else:
        for i in range(start, len(nums)):
            nums_sum.append(nums[i])
            DFS(i + 1, depth + 1)
            nums_sum.pop()

DFS(0,0)