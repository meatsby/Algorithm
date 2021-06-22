import sys

c = int(sys.stdin.readline())
test = [int(sys.stdin.readline()) for i in range(c)]

for t in test:
    rem = [25, 10, 5, 1]
    typ = [0, 0, 0, 0]
    for r in rem:
        typ[rem.index(r)] += t//r
        t %= r
    print(*typ)
