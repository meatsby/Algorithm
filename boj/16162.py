# 정답 참고

N, A, D = map(int, input().split())
l = list(map(int, input().split()))
cnt, nte = 0, 0

for i in range(N):
    if l[i] == A + (nte*D):
        cnt += 1
        nte += 1

print(cnt)
