# 수위 아저씨의 고민
# 나중에 다시 풀어봐요... 넘 어려움... ㅠㅠ

# T = int(input())
F, R, N = map(int, input().split())
result = (F+1)*2 + R - 1
lights = sorted([list(map(int, input().split())) for i in range(N)])
maxs = []

if R%2 == 0:
    for i in range(1, F+1):
        lmax = 0
        rmax = 0
        for j in lights:
            if j[0] == i and j[1] <= R//2 and j[1] > lmax:
                lmax = j[1]
            elif j[0] == i and j[1] > R//2 and R - j[1] + 1 > rmax:
                rmax = R - j[1] + 1

        if lmax != 0:
            maxs.append(lmax)
        if rmax != 0:
            maxs.append(rmax)

else:
    for i in range(1, F+1):
        lmax = 0
        mid = 0
        rmax = 0
        for j in lights:
            if j[0] == i and j[1] < R//2+1 and j[1] > lmax:
                lmax = j[1]
            elif j[0] == i and j[1] > R//2+1 and R - j[1] + 1 > rmax:
                rmax = R - j[1] + 1
            elif j[0] == i and j[1] == R//2+1:
                mid = R//2+1
        print(lmax, mid, rmax)
        if mid == 0:
            if lmax != 0:
                maxs.append(lmax)
            if rmax != 0:
                maxs.append(rmax)
        else:
            maxs.append(mid)
            if min(lmax, rmax) != 0:
                maxs.append(min(lmax, rmax))

for i in maxs:
    result += i*2

# 마지막 층이 1층일때
print(lights)
print(maxs)
print(result)
