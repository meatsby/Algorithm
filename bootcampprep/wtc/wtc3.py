# 프로그래밍3
import sys
input = sys.stdin.readline

def solution(word):
    result = ""

    for w in word:
        if w.isupper():
            result += chr(155 - ord(w))
        elif w.islower():
            result += chr(219 - ord(w))
        else:
            result += w

    return result

print(solution("I love you"))
