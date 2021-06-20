import sys

number = int(sys.stdin.readline())
result = 0

if number < 1 or number > 10000:
    print('error')
else:
    for i in range(1, number + 1):
        for c in str(i):
            if int(c) == 3 or int(c) == 6 or int(c) == 9:
                result += 1
    print(number, result)
