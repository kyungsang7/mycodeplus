import sys
input = sys.stdin.readline

def counting_5(num):
    res = 0
    if num < 5:
        return res
    while num >= 5:
        res += num // 5
        num //= 5
    return res

def counting_2(num):
    res = 0
    if num < 2:
        return res
    while num >= 2:
        res += num // 2
        num //= 2
    return res

ans = 0
n,m = map(int,input().split())

fives = counting_5(n) - counting_5(n-m) - counting_5(m)
twoes = counting_2(n) - counting_2(n-m) - counting_2(m)

print(min(fives, twoes))