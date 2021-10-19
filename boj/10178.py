# 할로윈의 사탕
import sys
input = sys.stdin.readline

for t in range(int(input())):
    c, v = map(int, input().split())
    me, dad = c//v, c%v
    print(f"You get {me} piece(s) and your dad gets {dad} piece(s).")
