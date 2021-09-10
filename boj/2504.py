# 괄호의 값

import sys

input = sys.stdin.readline

s = input().rstrip()
stack = []
ans = 0

for i in s:
    if i == ")":
        t = 0
        while len(stack) != 0:
            top = stack.pop()
            if top == "(":
                if t == 0:
                    stack.append(2)
                else:
                    stack.append(2*t)
                break
            elif top == "[":
                print(0)
                exit(0)
            else:
                t += top
    elif i == "]":
        t = 0
        while len(stack) != 0:
            top = stack.pop()
            if top == "[":
                if t == 0:
                    stack.append(3)
                else:
                    stack.append(3*t)
                break
            elif top == "(":
                print(0)
                exit(0)
            else:
                t += top
    else:
        stack.append(i)

for i in stack:
    if i == "(" or i == "[":
        print(0)
        exit(0)
    else:
        ans += i

print(ans)
