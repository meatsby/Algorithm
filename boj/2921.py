# 도미노
import sys
input = sys.stdin.readline

ans = 0
for i in range(1, int(input())+1):
    ans += ((2*i+1-i) * (i +2*i)) // 2

print(ans)
