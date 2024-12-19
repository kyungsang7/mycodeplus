n = int(input())
ans = [-1] * n
nums = list(map(int,input().split()))
nums_freq = {}
nums_freq_list = [0] * n
stack = []

for i in nums:
    if i in nums_freq:
        nums_freq[i] += 1
    else:
        nums_freq[i]= 1

for i in range(n):
    nums_freq_list[i] = nums_freq[nums[i]]

for i in range(n):
    while stack and nums_freq_list[stack[-1]] < nums_freq_list[i]:
        ans[stack.pop()] = nums[i]
    stack.append(i)

print(*ans)