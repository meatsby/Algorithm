# 더하기 사이클
import sys
input = sys.stdin.readline

n = int(input())
num = n
i = 0

while True:
    new = n%10*10 + (n//10 + n%10)%10
    i += 1
    if new == num:
        print(i)
        break
    n = new
