# Lv2 기능개발
import sys
input = sys.stdin.readline

def solution(progresses, speeds):
    answer = []
    idx = 0

    while sum(answer) < len(progresses):
        t_need = (100-progresses[idx])//speeds[idx] if (100-progresses[idx])%speeds[idx] == 0 else (100-progresses[idx])//speeds[idx] + 1

        for i in range(idx, len(progresses)):
            progresses[i] += t_need * speeds[i]

        cnt = 0
        for i in range(idx, len(progresses)):
            if progresses[i] >= 100:
                cnt += 1
            else:
                idx = i
                break
        answer.append(cnt)
    
    return answer
    

print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
print(solution([99, 98, 97], [1, 1, 1]))
print(solution([99, 99, 99, 97], [1, 1, 1, 1]))
