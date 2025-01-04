num = int(input())
colors = [list(input()) for _ in range(num)]
ans = 1

def find_rowed_nums():
    global ans
    for i in range(num):
        res = 1
        for j in range(1,num):
            if colors[i][j] == colors[i][j-1]:
                res += 1
            else:
                res = 1
            ans = max(ans, res)

    for i in range(num):
        res = 1
        for j in range(1,num):
            if colors[j][i] == colors[j-1][i]:
                res += 1
            else:
                res = 1
            ans = max(ans, res)

for i in range(num):
    for j in range(num-1):
        colors[i][j], colors[i][j+1] = colors[i][j+1], colors[i][j]
        find_rowed_nums()
        colors[i][j], colors[i][j+1] = colors[i][j+1], colors[i][j]

        colors[j][i] , colors[j+1][i] = colors[j+1][i], colors[j][i]
        find_rowed_nums()
        colors[j][i] , colors[j+1][i] = colors[j+1][i], colors[j][i]
print(ans)