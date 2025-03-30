N = int(input())
ans = 0

for num in range(1, N + 1):
    ans += (N // num) * num
            
print(ans)

