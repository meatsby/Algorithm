n = int(input())

# 시작과 끝을 튜플로 저장 및 끝나는 시간순으로 정렬
conf = sorted([tuple(map(int, input().split())) for i in range(n)], key=lambda x:(x[1],x[0]))
ans = end = 0

# 정렬이 되어 있으므로 처음부터 iteration 을 돌려도 예외 X
for s, e in conf:
    if s >= end:
        ans += 1
        end = e

print(ans)
