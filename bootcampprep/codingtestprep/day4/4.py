# 셀프 넘버
import sys
input = sys.stdin.readline

nums = set([i for i in range(1, 10001)])
made = set([])

for i in range(1, 10001):
    new = i
    for s in str(i):
        new += int(s)
    if new not in made:
        made.add(new)

selfnum = nums - made

for i in sorted(selfnum):
    print(i)
