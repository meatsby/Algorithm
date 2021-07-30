# Level1 로또의 최고 순위와 최저 순위

def solution(lottos, win_nums):
    cnt = 0
    for i in lottos:
        if i in win_nums:
            cnt += 1
    zeros = lottos.count(0)
    answer = [6 if 7-(cnt+zeros) == 7 else 7-(cnt+zeros), 6 if 7-cnt == 7 else 7-cnt]
    return answer
