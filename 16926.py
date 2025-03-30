def simulation():
    start = nums[count][count]

    for i in range(count, M - 1):
        nums[count][i] = nums[count][i + 1]

    for i in range(count, N - 1):
        nums[i][M - 1] = nums[i + 1][M - 1]

    for i in range(M - 1, count, -1):
        nums[N - 1][i] = nums[N - 1][i - 1]

    for i in range(N - 1, count + 1, -1):
        nums[i][count] = nums[i - 1][count]

    nums[count + 1][count] = start

N, M, R = map(int,input().split())
nums = list(list(map(int,input().split())) for _ in range(N))

for count in range(min(N, M) // 2):
    for _ in range(R % (N * 2 + M * 2 - 4 * count - 4)):
        simulation()
    N -= 1
    M -= 1

for i in nums:
    print(*i)