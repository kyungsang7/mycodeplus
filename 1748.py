N = int(input())
lap = 9
ans = 0

while True:
    if N > lap:
        ans += lap * len(str(lap))
        N -= lap
        lap *= 10
    else:
        ans += N * len(str(lap))
        break

print(ans)