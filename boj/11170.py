# 0의 개수
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    ans = 0
    
    for i in range(n, m+1):
        ans += str(i).count("0")
    
    print(ans)
