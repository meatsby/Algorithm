# 딱지놀이
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a, b = 0, 0
    al = list(map(int, input().split()))
    bl = list(map(int, input().split()))

    for n in al[1:]:
        a += 101**n
    for n in bl[1:]:
        b += 101**n
    
    if a > b:
        print("A")
    elif b > a:
        print("B")
    else:
        print("D")
