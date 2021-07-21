# 햄버거 분배
# 정답 참고
# 문자열 문제가 나오면 주저말고 리스트에 때려박자

N, K = map(int, input().split())
l = list(input())
cnt = 0

for i in range(N):
    if l[i] == 'P':
        for j in range(i-K, i+K+1):
            if 0 <= j < N and l[j] == 'H':
                cnt += 1
                l[j] = '0'
                break

print(cnt)
