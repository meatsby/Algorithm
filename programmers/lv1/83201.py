# Lv1 위클리 챌린지 2주차

def solution(scores):
    n = len(scores)
    
    lst = list(map(list, zip(*scores)))
    
    avg = []
    for i in range(n):
        if (lst[i][i] == max(lst[i]) or lst[i][i] == min(lst[i])) and lst[i].count(lst[i][i]) == 1:
            avg.append((sum(lst[i]) - lst[i][i])/(n-1))
        else:
            avg.append(sum(lst[i])/n)
    
    answer = []
    for i in avg:
        if i >= 90:
            answer.append('A')
        elif i >= 80:
            answer.append('B')
        elif i >= 70:
            answer.append('C')
        elif i >= 50:
            answer.append('D')
        else:
            answer.append('F')
    
    answer = ''.join(answer)
    return answer