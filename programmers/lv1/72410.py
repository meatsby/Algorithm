# Lv1 신규 아이디 추천
# 정규식 표현 사용 가능
# while '..' in answer: answer = answer.replace('..', '.') 사용 가능

def solution(new_id):
    id = list(new_id)
    l = []
    for i in id[:]:
        l.append(i.lower())

    id = l
    l = []
    for i in id[:]:
        if 45 <= ord(i) <= 46 or 48 <= ord(i) <= 57 or ord(i) == 95 or 97 <= ord(i) <= 122:
            l.append(i)

    id = l
    l = [id[0]]
    if len(id) > 2:
        for i in range(1, len(id)):
            if id[i-1] == '.' and id[i-1] == id[i]:
                continue
            else:
                l.append(id[i])

    id = l
    if len(id) > 0:
        if id[0] == '.':
            del id[0]
    if len(id) > 0:
        if id[-1] == '.':
            del id[-1]
    
    if len(id) == 0:
        id = ['a']
    
    if len(id) > 15:
        id = id[:15]
    if id[-1] == '.':
        del id[-1]
    
    while len(id) < 3:
        id.append(id[-1])
    
    answer = ''.join(id)
    return answer