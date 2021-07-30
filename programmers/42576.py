# Level1 완주하지 못한 선수

def solution(participant, completion):
    
    for i in participant[:]:
        if i in completion:
            participant.remove(i)
            completion.remove(i)
    
    answer = participant[0]
    
    return answer