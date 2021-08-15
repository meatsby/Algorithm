# 날짜 계산

E, S, M = map(int, input().split())
a, b, c = 1, 1, 1
year = 1

while True:
    if [E, S, M] == [a, b, c]:
        print(year)
        break
    else:
        a += 1
        b += 1
        c += 1
        year += 1
        if a == 16:
            a = 1
        if b == 29:
            b = 1
        if c == 20:
            c = 1
