E,S,M = map(int,input().split())
earth, sun, moon = 1, 1, 1
day = 1

while True:
    if E == earth and S == sun and M == moon:
        print(day)
        break
    else:
        earth = (earth + 1) % 16
        sun = (sun + 1) % 29
        moon = (moon + 1) % 20
        day += 1
    if earth == 0:
        earth += 1
    if sun == 0:
        sun += 1
    if moon == 0:
        moon += 1