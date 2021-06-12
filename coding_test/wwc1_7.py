# Recursively(재귀적으로)

cryptogram = input()

def solution(cryptogram):
    c = list(cryptogram)
    for i in range(len(c) - 1):
        if c[i+1] == c[i]:
            del c[i+1], c[i]
            return solution(''.join(c))
    return ''.join(c)

print(solution(cryptogram))
