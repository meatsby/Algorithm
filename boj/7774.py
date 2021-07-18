# 콘센트

n, m = map(int, input().split())
a = sorted(list(map(int, input().split())), reverse=True)
b = sorted(list(map(int, input().split())), reverse=True)

if n == 0 or m == 0:
    print(1)
elif sum(a) < m:
    print(sum(b[:sum(a)]) - n + 1)
elif sum(a) >= m:
    for i in range(1, n+1):
        if sum(a[:i]) >= m:
            print(sum(b) - i + 1)
            break
