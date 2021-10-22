# 첫 글자를 대문자로
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    s = input().rstrip()
    print(s[0].upper() + s[1:])
