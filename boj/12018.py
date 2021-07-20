# Yonsei TOTO

n, m = map(int, input().split())
required = []
result = 0

for i in range(n):
    P, L = map(int, input().split())
    mile = sorted(list(map(int, input().split())),reverse=True)
    if P < L:
        required.append(1)
    else:
        required.append(mile[L-1])

for i in sorted(required):
    m -= i
    if m < 0:
        break
    result += 1

print(result)
