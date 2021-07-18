T = int(input())

for i in range(T):
    N = int(input())
    num = list(map(int, input().split()))
    max = num[0]
    cnt = 0

    for i in range(1, N):
        if num[i] > max:
            max = num[i]
        elif num[i] == max - 1:
            cnt += 1
        elif num[i] < max:
            cnt += i

    print(cnt)
