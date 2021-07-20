# 에리 - 카드

N, K = map(int, input().split())
share = list(map(int, input().split()))
team = list(map(int, input().split()))
ans = []

for i in team:
    result = []
    for j in share:
        result.append(i*j)
    ans.append(sorted(result, reverse=True)[0])

print(sorted(ans, reverse=True)[K])
