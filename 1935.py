n = int(input())
exp = input()
res = 0
stack = []
ans = 0
un_num = []
for i in range(n):
    un_num.append(int(input()))

for i in exp:
    if i == '*':
        stack.append(stack.pop() * stack.pop())
    elif i == '/':
        x1 = stack.pop()
        x2 = stack.pop()
        stack.append(x2/x1)
    elif i == '+':
        stack.append(stack.pop() + stack.pop())
    elif i == '-':
        x1 = stack.pop()
        x2 = stack.pop()
        stack.append(x2-x1)
    else:
        stack.append(un_num[ord(i)-65])
print(format(stack.pop(),".2f"))