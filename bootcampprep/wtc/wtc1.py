# 프로그래밍1
import sys
input = sys.stdin.readline

def solution(money):
    result = []
    change = [50000, 10000, 5000, 1000, 500, 100, 50, 10, 1]
    
    for c in change:
        result.append(money//c)
        money %= c
    
    return result

print(solution(50237))
print(solution(15000))
