# 민균이의 비밀번호
import sys
input = sys.stdin.readline

strings = []
ans = ""

for _ in range(int(input())):
    s = input().rstrip()
    strings.append(s)
    if s[::-1] in strings:
        ans = s

print(len(ans), ans[len(ans)//2])
