# Lv1 K번째수

def solution(array, commands):
    answer = []
    
    for p in range(len(commands)):
        i, j, k = commands[p][0] - 1, commands[p][1], commands[p][2] - 1
        answer.append(sorted(array[i:j])[k])
        
    return answer