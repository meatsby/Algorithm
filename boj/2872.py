# 정답 참고

N = int(input())
books = list(int(input()) for i in range(N))
max = books[0]
cnt = 0

for i in range(1, N):
    if books[i] > max:
        if max + 1 != books[i]:
            cnt += 1
        max = books[i]
    else:
        cnt += 1

print(cnt)
