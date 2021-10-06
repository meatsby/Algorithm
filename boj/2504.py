# 괄호의 값

import sys
input = sys.stdin.readline

s = input().rstrip()

def check(s):
    stack = []
    flag = True

    for i in s:
        if i == "(" or i == "[":
            stack.append(i)
        elif i == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                flag = False
        elif i == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                flag = False

    if not stack and flag:  # 스택이 비어 있으며 맞는 괄호식일 경우
        return True
    return False

def calc(s):
    stack = []

    for i in s:
        if i == "(" or i == "[":
            stack.append(i)
        elif i == ")":
            if stack[-1] == "(":
                stack[-1] = 2
            else:
                temp = 0
                for j in range(len(stack)-1, -1, -1):
                    if stack[j] == "(":  # 괄호를 찾을 때 까지 정수끼리 더해주기
                        stack[-1] = temp * 2  # 찾으면 2 곱해주고 반복문 탈출
                        break
                    else:
                        d = stack.pop()
                        temp += d
        elif i == "]":
            if stack[-1] == "[":
                stack[-1] = 3
            else:
                temp = 0
                for j in range(len(stack)-1, -1, -1):
                    if stack[j] == "[":  # 괄호를 찾을 때 까지 정수끼리 더해주기
                        stack[-1] = temp * 3  # 찾으면 3 곱해주고 반복문 탈출
                        break
                    else:
                        d = stack.pop()
                        temp += d
    return sum(stack)

if check(s):
    print(calc(s))
else:
    print(0)
