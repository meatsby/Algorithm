N = int(input())
h = list(map(int, input().split()))

now = h[0]
n = 0

ans = 0
for i in range(1, N):
    if h[i] < now:
        n += 1
    else:
        n = 0
        now = h[i]

    ans = max(ans, n)

print(ans)
