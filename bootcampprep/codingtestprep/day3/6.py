# 수 이어 쓰기 1
import sys
input = sys.stdin.readline

n = int(input())
ans = 0
i = 1

while True:
    if n - (9 * 10**(i-1)) < 0:
        ans += n*i
        print(ans)
        break
    else:
        n -= (9 * 10**(i-1))
        ans += (9 * 10**(i-1) * i)
        i += 1
