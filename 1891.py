length, location = map(int,input().split())
plus_y, plus_x = map(int,input().split())
x, y = 0, 0

for i in range(length):
    num = int(str(location)[i])
    if num == 3 or num == 4:
        x += 2 ** (length - 1 - i)

    if num == 1 or num == 4:
        y += 2 ** (length - 1 - i)

x -= plus_x
y += plus_y
ans = ''

for i in range(length - 1, -1, -1):
    num = 2 ** i

    if x < num and y >= num:
        ans += '1'
        y -= num
    
    elif x < num and y < num:
        ans += '2'

    elif x >= num and y < num:
        ans += '3'
        x -= num
    
    else:
        ans += '4'
        x -= num
        y -= num

if x == y == 0:
    print(ans)

else:
    print(-1)