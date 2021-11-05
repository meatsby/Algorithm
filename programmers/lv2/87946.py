# Lv2 피로도
from itertools import permutations
import sys
input = sys.stdin.readline

def solution(k, dungeons):
    answer = -1

    dg = [i for i in range(len(dungeons))]
    order = list(permutations(dg, len(dungeons)))

    for o in order:
        p = k
        cnt = 0
        for i in o:
            need = dungeons[i][0]
            loss = dungeons[i][1]
            if p >= need:
                p -= loss
                cnt += 1
            else:
                break
        answer = max(answer, cnt)

    return answer
