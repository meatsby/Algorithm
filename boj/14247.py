# 나무 자르기

n = int(input())
H = list(map(int, input().split()))
A = list(map(int, input().split()))
l = sorted([[A[i], H[i]] for i in range(n)])
ans = 0

for i in range(n):
    ans += l[i][1] + l[i][0] * i

print(ans)
