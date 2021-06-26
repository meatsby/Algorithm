import sys

n = int(sys.stdin.readline().rstrip())
elc = [int(sys.stdin.readline().rstrip()) for i in range(n)]
me = elc[0]
cmp = elc[1:]

if n == 1:
    print(0)
else:
    num = 0
    cmp.sort(reverse=True)
    while cmp[0] >= me:
        me += 1
        cmp[0] -= 1
        num += 1
        cmp.sort(reverse=True)
    print(num)
