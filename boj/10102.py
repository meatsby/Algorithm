# TGN
import sys
input = sys.stdin.readline

v = int(input())
s = input().rstrip()
a, b = 0, 0
for i in s:
    if i == "A":
        a += 1
    else:
        b += 1
if a > b:
    print("A")
elif a == b:
    print("Tie")
else:
    print("B")
