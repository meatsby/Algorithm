# 별 찍기 - 9

import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    print(i*" " + (n-i)*"*" + (n-1-i)*"*")

for i in range(1, n):
    print((n-1-i)*" " + (i+1)*"*" + i*"*")
