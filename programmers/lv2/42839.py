# Lv2 소수 찾기
from itertools import permutations
import sys
input = sys.stdin.readline

def isPrime(n):
    for i in range(2, n):
        if n%i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    nums = list(map(int, list(numbers)))

    for i in range(2, len(numbers)+1):
        for l in list(permutations(list(numbers), i)):
            nums.append(int("".join(l)))

    nums = list(set(nums))
    if 0 in nums:
        nums.remove(0)
    if 1 in nums:
        nums.remove(1)

    for n in nums:
        if isPrime(n):
            answer += 1

    return answer

print(solution("17"))
print(solution("011"))
