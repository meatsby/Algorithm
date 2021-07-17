N = int(input())
l = sorted(list(int(input())for i in range(N)))
result = 0

for i in range(N):
    if l[i] != i+1:
        result += abs(i+1-l[i])

print(result)
