n = int(input())
nums = list(map(int, input().split()))
count = 0

for n in nums:
    b = 0
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                b += 1
        if b == 0:
            count += 1

print(count)
