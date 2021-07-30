# 체인
# cnt > connection : 나머지를 다 못 묶은 것
# cnt == connection : 나머지를 모두 묶고 하나 남은 자기 자신을 묶은 것
# cnt < connection : 나머지의 갯수만큼 묶은 것

N = int(input())
chain = sorted(list(map(int, input().split())))
connection = 0
cnt = 0

for i in range(N):
    cnt = N - 1 - i
    connection += chain[i]
    if connection >= cnt:
        print(cnt)
        break
