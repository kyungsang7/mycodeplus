N = int(input())
houses_colors_cost_list = [list(map(int,input().split())) for _ in range(N)]
for i in range(1,N):
    houses_colors_cost_list[i][0] += min(houses_colors_cost_list[i-1][1], houses_colors_cost_list[i-1][2])
    houses_colors_cost_list[i][1] += min(houses_colors_cost_list[i-1][0], houses_colors_cost_list[i-1][2])
    houses_colors_cost_list[i][2] += min(houses_colors_cost_list[i-1][0], houses_colors_cost_list[i-1][1])
print(min(houses_colors_cost_list[-1]))