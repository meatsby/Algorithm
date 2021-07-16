N = int(input())
l = sorted(list(map(int, input().split())))
result = [l[i] + l[-i-1] for i in range(N)]

print(min(result))
