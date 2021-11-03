# 프로그래밍4
import sys
input = sys.stdin.readline

def isTrue(l):
    if l[0]%2 == 1 and l[1]%2 == 0 and l[1] - l[0] == 1 and 1 <= l[0] <= 400 and 1 <= l[1] <= 400 and l[0] != 1 and l[1] != 400:
        return True

    return False

def calculate(l):
    left = list(map(int, str(l[0])))
    right = list(map(int, str(l[1])))

    lsum, lpro = sum(left), 1
    rsum, rpro = sum(right), 1

    for i in left:
        lpro *= i
    for i in right:
        rpro *= i

    return max(lsum, lpro, rsum, rpro)

def solution(pobi, crong):
    result = -1

    if isTrue(pobi) and isTrue(crong):
        if calculate(pobi) < calculate(crong):
            result = 2
        if calculate(pobi) > calculate(crong):
            result = 1
        if calculate(pobi) == calculate(crong):
            result = 0

    return result

print(solution([97, 98], [197, 198]))
print(solution([131, 132], [211, 212]))
print(solution([99, 102], [211, 212]))
print(solution([3, 4], [235, 236]))
print(solution([1, 2], [235, 236]))
print(solution([3, 4], [399, 400]))
