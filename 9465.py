for _ in range(int(input())):
    N = int(input())
    stickes_value = [list(map(int,input().split())) for _ in range(2)]
    res_list = [[0]*(N+2) for _ in range(2)]
    for i in range(N):
        res_list[0][i] = max(res_list[0][i-1], res_list[1][i-1] + stickes_value[0][i], res_list[0][i-2] + stickes_value[0][i], res_list[1][i-2] + stickes_value[0][i])
        res_list[1][i] = max(res_list[1][i-1], res_list[0][i-1] + stickes_value[1][i], res_list[0][i-2] + stickes_value[1][i], res_list[1][i-2] + stickes_value[1][i])
    print(max(res_list[0][N-1], res_list[1][N-1]))