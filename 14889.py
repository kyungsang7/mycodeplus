N = int(input())
pow = list(list(map(int,input().split())) for _ in range(N))
nums = set([i for i in range(N)])

team = []
ans = 10 ** 4

def Recrusive_call(num):
    global team, ans

    if len(team) == N // 2:
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
    for i in range(N // 2 - 1):
        for j in range(i + 1, N // 2):
            p += pow[power[i]][power[j]]
            p += pow[power[j]][power[i]]
    return p

Recrusive_call(0)
print(ans)
