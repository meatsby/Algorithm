# 약수들의 합
import sys
input = sys.stdin.readline

while True:
    nums = []
    n = int(input())
    if n == -1:
        break
    for i in range(1, (n//2)+1):
        if n%i == 0:
            nums.append(i)
    if n == sum(nums):
        nums = list(map(str, nums))
        print(f"{n} = " + " + ".join(nums))
    else:
        print(f"{n} is NOT perfect.")
