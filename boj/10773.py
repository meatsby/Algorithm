# 제로

K = int(input())
nums = []
for i in range(K):
    num = int(input())
    if num == 0:
        nums.pop()
    else:
        nums.append(num)

print(sum(nums))
