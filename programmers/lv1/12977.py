# Lv1 소수 만들기

def prime_number(number):
    if number != 1:
        for f in range(2, number):
            if number % f == 0:
                return False
    else:
        return False
    return True

def solution(nums):
    nums = sorted(nums)
    
    result = 0
    
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if prime_number(nums[i] + nums[j] + nums[k]):
                    result += 1
                    
    return result