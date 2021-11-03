# 만취한 상범
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    cell = ["*"] + [1] * n
    for i in range(2, n+1):
        for j in range(i, n+1, i):
            cell[j] = 0 if cell[j] == 1 else 1
    print(sum(cell[1:]))
