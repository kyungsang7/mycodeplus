def bin(num):
    res = 0
    for i in trees:
        if i > num:
            res += i - num
    return res

N, M = map(int, input().split())
trees = list(map(int,input().split()))
left, right = 0, 2000000000

while left <= right:
    mid = (left + right) // 2
    res = bin(mid)

    if res < M:
        right = mid - 1
    else:
        left = mid + 1

print(right) 