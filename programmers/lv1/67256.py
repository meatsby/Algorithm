# Lv1 키패드 누르기

def solution(numbers, hand):
    answer = ''
    lt = 10
    rt = 12
    for i in numbers:
        if i in [1, 4, 7]:
            answer += 'L'
            lt = i
        elif i in [3, 6, 9]:
            answer += 'R'
            rt = i
        else:
            i = 11 if i == 0 else i
            if sum(divmod(abs(i-lt), 3)) < sum(divmod(abs(i-rt), 3)):
                answer += 'L'
                lt = i
            elif sum(divmod(abs(i-lt), 3)) > sum(divmod(abs(i-rt), 3)):
                answer += 'R'
                rt = i
            else:
                if hand == 'left':
                    answer += 'L'
                    lt = i
                else:
                    answer += 'R'
                    rt = i
            
    return answer