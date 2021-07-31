# Lv1 숫자 문자열과 영단어

def solution(s):
    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    word = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    while True:
        if s.isdecimal():
            answer = int(s)
            break
        else:
            for i in range(10):
                if word[i] in s:
                    s = s.replace(word[i], nums[i])
                    
    return answer