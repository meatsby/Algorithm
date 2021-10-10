# 소음
import sys
input = sys.stdin.readline

a = int(input())
op = input().rstrip()
b = int(input())

print(a * b) if op == "*" else print(a + b)
