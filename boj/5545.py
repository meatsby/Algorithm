# 최고의 피자

N = int(input())
A, B = map(int, input().split())
dow = int(input())
topping = sorted(list(int(input()) for i in range(N)), reverse=True)
kcalperwon = []

for i in range(N+1):
    kcalperwon.append( (dow + sum(topping[:i])) // (A + (B*i)))

print(max(kcalperwon))
