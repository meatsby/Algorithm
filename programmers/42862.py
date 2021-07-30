# Level1 체육복
# 백준 2891 강풍과 카약과 유사한 문제

def solution(n, lost, reserve):
    zero = [0 for i in range(n+2)]
    
    for i in lost:
        zero[i] = -1
    
    for i in reserve:
        if zero[i] == -1:
            zero[i] = 0
        else:
            zero[i] = 1
    
    for i in range(1, n+1):
        if zero[i] == -1:
            if zero[i-1] == 1:
                zero[i] = 0
                zero[i-1] = 0
            elif zero[i+1] == 1:
                zero[i] = 0
                zero[i+1] = 0
    
    answer = 0
    
    for i in zero[1:n+1]:
        if i > -1:
            answer += 1
    
    return answer
