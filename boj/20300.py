N = int(input())
l = sorted(list(map(int, input().split())))
result = []

if len(l)%2 == 1:
    result.append(l[-1])
    for i in range((N-1)//2):
        result.append(l[i] + l[-i-2])
else:
    for i in range(N//2):
        result.append(l[i] + l[-i-1])

print(max(result))
