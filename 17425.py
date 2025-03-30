import sys
input = sys.stdin.readline

numns = [1] * (10 ** 6 + 1)

for i in range(2, 10 ** 6 + 1):
    j = 1
    while i * j <= 10 ** 6:
        numns[i * j] += i
        j += 1

sum_nums = [0] * (10 ** 6 + 1)

for i in range(1, 10 ** 6 + 1):
    sum_nums[i] = sum_nums[i - 1] + numns[i]

for i in range(int(input())):
    print(sum_nums[int(input())])