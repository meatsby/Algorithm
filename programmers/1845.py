# Level1 포켓몬

def solution(nums):
    types = len(set(nums))
    most = len(nums)//2
    if most > types:
        answer = types
    else:
        answer = most
    return answer