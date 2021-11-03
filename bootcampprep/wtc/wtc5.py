# 프로그래밍5
import sys
input = sys.stdin.readline

def solution(number):
    result = 0

    for n in range(1, number+1):
        for i in ["3", "6", "9"]:
            if i in str(n):
                result += str(n).count(i)

    return result

print(solution(13))
print(solution(33))
