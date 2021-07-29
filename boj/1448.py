# 삼각형 만들기

N = int(input())
side = sorted([int(input()) for i in range(N)], reverse=True)
result = -1

for i in range(N-2):
    if side[i] < side[i+1] + side[i+2]:
        result = side[i] + side[i+1] + side[i+2]
        break

print(result)
