import sys

t = int(sys.stdin.readline())
sec = [300, 60, 10]
but = [0, 0, 0]

for s in sec:
    but[sec.index(s)] += t//s
    t %= s

if t == 0:
    print(*but)
else:
    print('-1')
