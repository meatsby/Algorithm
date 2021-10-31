# 진법 변환
import sys
input = sys.stdin.readline

n, b = input().rstrip().split()
ans = 0

for i in range(len(n)):
    s = n[::-1][i]
    if s.isupper():
        s = ord(s) - 55
    else:
        s = int(s)
    ans += s * int(b)**i

print(ans)
