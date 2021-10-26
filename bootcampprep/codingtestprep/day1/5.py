# 방 번호
import sys
input = sys.stdin.readline

n = input().rstrip()
need = [0] * 10
nine = 0

for i in n:
    nn = int(i)
    if nn == 6 or nn == 9:
        nine += 1
    else:
        need[nn] += 1

print(max(max(need), (nine+1)//2))