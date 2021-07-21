# 안테나
# 어디에 집이 위치하건 가운데 있는 집이 제일 최소값을 냄

N = int(input())
l = sorted(list(map(int, input().split())))

if len(l)%2 == 0:
    print(l[N//2-1])
else:
    print(l[N//2])
