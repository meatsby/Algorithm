# 3개의 정수(a, b, c)가 입력되었을 때, 짝수만 출력해보자.

a = list(map(int, input().split()))

for i in range(len(a)):
    if a[i] % 2 == 0:
        print(a[i])
