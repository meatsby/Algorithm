# Pismo
# 영어문젠데 문제 이해를 잘 못한듯...

N = int(input())
A = list(map(int, input().split()))
v = []

for i in range(1, N):
    v.append(abs(A[i]-A[i-1]))

print(min(v))
