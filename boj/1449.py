# 정답 참고

N, L = map(int, input().split())
l = sorted(list(map(int, input().split())))
start = l[0]
end = l[0] + L
cnt = 1

for i in range(N):
    if start <= l[i] < end:
        continue
    else:
        start = l[i]
        end = l[i] + L
        cnt += 1

print(cnt)
