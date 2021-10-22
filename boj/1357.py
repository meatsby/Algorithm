# 뒤집힌 덧셈
import sys
input = sys.stdin.readline

def Rev(n):
    return n[::-1]

x, y = input().rstrip().split()
print(int(Rev(str(int(Rev(x)) + int(Rev(y))))))
