def GCD(n1,n2):
    while n2 != 0:
        n1,n2 = n2,n1 % n2
    return n1

N,S = map(int,input().split())
nums = list(map(int,input().split()))
gcd = abs(nums[0] - S)

for i in range(1,N):
    gcd = GCD(gcd, abs(nums[i]-S))
print(gcd)