# 뒤집기 II
# if문 안에 있는 이중루프를 def 로 정의해서 재귀로 만들었을수도 있었을 듯

N, M = map(int, input().split())
coins = [list(map(int, list(input()))) for i in range(N)]
cnt = 0

for a in range(N-1, -1, -1):
    for b in range(M-1, -1, -1):
        if coins[a][b] == 1:
            cnt += 1
            for i in range(a+1):
                for j in range(b+1):
                    if coins[i][j] == 1:
                        coins[i][j] = 0
                    else:
                        coins[i][j] = 1

print(cnt)
