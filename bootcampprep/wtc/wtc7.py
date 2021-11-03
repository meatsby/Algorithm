# 프로그래밍7
import sys
input = sys.stdin.readline

def slice(word):
    for i in range(len(word)-1):
        if word[i] == word[i+1]:
            return word[:i] + word[i+2:]
    return word

def solution(cryptogram):
    word = cryptogram

    while True:
        new = slice(word)
        if new == word:
            result = word
            break
        word = new

    return result

print(solution("browoanoommnaon"))
print(solution("zyelleyz"))
print(solution("hello"))
print(solution("oomm"))
print(solution("oo"))
print(solution("ppleveloo"))
