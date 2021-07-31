# Lv1 내적

def solution(a, b):
    answer = 0
    
    for i in range(len(a)):
        answer += a[i] * b[i]

    return answer

# zip(), lambda 활용 가능