n = int(input())
i = 2

while n != 1:
    if n % i == 0:
        n /= i
        print(i)
    else:
        i += 1

# 시간초과
# import math

# n = int(input())
# a = []
# b = []

# # 소수 판별
# def prime(x):
#     for i in range(2, int(math.sqrt(x)) + 1):
#         if x % i == 0:
#             return False
#     return True

# # 소인수분해
# for i in range(2, n):
#     if prime(i):
#         while n % i == 0:
#             n /= i
#             print(i)
