bar = input()
stack = 1
ans = 0

# 무조건 "("로 시작하는 전제 하에 작성된 코드
for i in range(1,len(bar)):
    if bar[i] == '(':
        stack += 1
    else:
        stack -= 1
        if bar[i-1] == '(':
            ans += stack
        else:
            ans += 1
print(ans)