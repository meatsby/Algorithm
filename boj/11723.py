# 집합
# 비트마스킹 새로 배움
# pypy3 는 메모리초과, python3 로 해결

import sys
input = sys.stdin.readline

M = int(input())
S = 0

for _ in range(M):
    inp = input()
    command = inp.split()[0]
    if command == "add":
        S |= (1 << int(inp.split()[1]))
    elif command == "remove":
        S &= ~(1 << int(inp.split()[1]))
    elif command == "remove":
        S &= ~(1 << int(inp.split()[1]))
    elif command == "check":
        if S & (1 << int(inp.split()[1])):
            print(1)
        else:
            print(0)
    elif command == "toggle":
        S ^= (1 << int(inp.split()[1]))
    elif command == "all":
        S = (1 << 21) - 1
    elif command == "empty":
        S = 0
