# Lv2 문자열 압축

def solution(s):
    ans = len(s)
    for l in range(1, len(s)):
        temp = [0, ""]
        new = ""
        for i in range(0, len(s), l):
            t = s[i:i+l]
            if t == temp[1]:
                temp = [temp[0]+1, t]
            else:
                if temp[0] != 0:
                    new += str(temp[0]) + temp[1] if temp[0] > 1 else temp[1]
                temp = [1, t]
        if temp[0] > 0:
            new += str(temp[0]) + temp[1] if temp[0] > 1 else temp[1]
        ans = min(ans, len(new))
    return ans