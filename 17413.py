a = input()
stack_True = True
ans = ''
stack = ''
for i in a:
    if i == '<':
        stack_True = False
        ans += stack[::-1] 
        ans += i
        stack = ''
    elif i == '>':
        stack_True = True
        ans += i
    elif stack_True and i == ' ':
        ans += stack[::-1] + ' '
        stack = ''
    else:
        if stack_True:
            stack += i
        else:
            ans += i
ans += stack[::-1]
print(ans)