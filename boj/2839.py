n = int(input())
b = 0

while n >= 0:
    if n % 5 == 0:
        b += n // 5
        print(b)
        break
    n -= 3
    b += 1
    if n == 0:
        print(b)
        break
    if n < 0:
        print(-1)
        break
