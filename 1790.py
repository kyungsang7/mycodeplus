def calc(num):
    length = len(str(num)) - 1
    if length == 0:
        return num
    
    res = (num - int('9' * length)) * (length + 1)
    for i in range(length):
        res += 9 * 10 ** i

    return res

N, k = map(int,input().split())

left, right = 0, 10 ** 8

while left <= right:
    middle = (left + right) // 2
    res = calc(middle)

    if res >= k:
        right = middle - 1
    
    else:
        left  = middle + 1


if N < left:
    print(-1)

else:
    idx = k - calc(left - 1) - 1
    print(int(str(left)[idx]))

