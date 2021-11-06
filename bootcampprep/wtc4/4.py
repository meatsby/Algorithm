def solution(s):
    s = list(s)
    while True:
        if s[0] == s[-1]:
            s += s[0]
            del s[0]
        else:
            break
    s.append(0)

    answer = []
    l = 1
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            l += 1
        else:
            answer.append(l)
            l = 1

    return sorted(answer)

print(solution("aaabbaaa"))
print(solution("wowwow"))