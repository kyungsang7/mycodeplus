def GCD(num1, num2):
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    return num1

for _ in range(int(input())):
    nums = list(map(int,input().split()))
    res = 0
    for i in range(1, nums[0]):
        for j in range(i+1, nums[0]+1):
            res += GCD(nums[i], nums[j])
    print(res)