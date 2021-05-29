n = int(input())
new_n = n
count = 0

while True:
    new_n = new_n % 10 * 10 + (new_n // 10 + new_n % 10) % 10
    count += 1
    if new_n == n:
        break

print(count)
