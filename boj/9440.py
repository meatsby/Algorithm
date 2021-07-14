# 런타임 에러 왜?

while True:
    l = list(map(int, input().split()))
    N = l[0]

    if N == 0:
        break

    num = sorted(l[1:])
    zeros = num.count(0)
    num = num[zeros:]
    sum = 0
    pwr = 0

    for i in range(zeros):
        num[i] *= 10

    num.reverse()

    for i in num:
        sum += i * 10**int(pwr)
        pwr += 0.5

    print(sum)
