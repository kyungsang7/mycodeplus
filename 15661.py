N = int(input())
pow = list(list(map(int,input().split())) for _ in range(N))
nums = set(i for i in range(N))

ans = 10 ** 4

def Recrusive_call(num):
    global team, ans, teammate_num

    if len(team) == teammate_num:
        p1 = calculate_team_power(team)
        p2 = calculate_team_power(list(nums - set(team)))
        ans = min(ans, abs(p1 - p2))
        return
    
    for i in range(num, N - 1):
        team.append(i)
        Recrusive_call(i + 1)
        team.pop()

def calculate_team_power(power):
    p = 0
    for i in range(len(power) - 1):
        for j in range(i + 1, len(power)):
            p += pow[power[i]][power[j]]
            p += pow[power[j]][power[i]]
    return p

for i in range(1, N - 1):
    team = []
    teammate_num = i
    Recrusive_call(0)

print(ans)