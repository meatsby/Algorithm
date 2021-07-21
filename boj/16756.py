# Pismo
# 111, max-min = 1-1 = 0, minimum value of the interval = 0
# 112, max-min = 2-1 = 1, minimum value of the interval = 0
# 181, max-min = 8-1 = 7, minimum value of the interval = 0
# 181의 경우 어짜피 value 가 7이 나오기 때문에 굳이 길이가 2 이상인 interval이 필요없음

N = int(input())
A = list(map(int, input().split()))
v = []

for i in range(1, N):
    v.append(abs(A[i]-A[i-1]))

print(min(v))
