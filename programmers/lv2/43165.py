# Lv2 타겟 넘버

from itertools import combinations

def solution(numbers, target):
    ans = 0
    idx = [i for i in range(len(numbers))]

    for i in range(1, len(numbers)):
        com = list(combinations(idx, i))
        for c in com:
            total = sum(numbers)
            for n in c:
                total -= numbers[n]*2
            if total == target:
                ans += 1

    return ans
