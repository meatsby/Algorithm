T = int(input())

for i in range(T):
    N = int(input())
    num = list(map(int, input().split()))
    result = 0

    for i in range(N):
        cnt = 0
        for j in num[:i]:
            if j > num[i]:
                cnt += 1
        result += cnt
        
    print(result)
