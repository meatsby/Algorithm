n, x = map(int, input().split())
a = list(map(int, input().split()))
list = []

for i in a:
    if i < x:
        list.append(i)

print(*list)
