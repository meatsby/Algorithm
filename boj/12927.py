light = list(input())
N = len(light)
cnt = 0

for p in range(N):
    if light[p] == 'Y':
        cnt += 1
        for i in range(p, N, p+1):
            if light[i] == 'Y':
                light[i] = 'N'
            elif light[i] == 'N':
                light[i] = 'Y'

print(cnt)
