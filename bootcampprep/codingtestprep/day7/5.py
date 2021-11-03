# 참외밭
import sys
input = sys.stdin.readline

k = int(input())
tl = []
dl = [0, 0, 0, 0, 0]

for _ in range(6):
    d, l = map(int, input().split())
    dl[d] += l
    tl.append(l)

while True:
    if tl[0] in dl and tl[1] in dl:
        break
    tl.insert(0, tl.pop())

print(k * (tl[0]*tl[1] - tl[3]*tl[4]))
