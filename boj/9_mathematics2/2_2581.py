m = int(input())
n = int(input())
a = []

for num in range(m, n+1):
    error = 0
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                error += 1
                break
        if error == 0:
            a.append(num)

if sum(a) == 0:
    print(-1)
else:
    print(sum(a))
    print(min(a))
