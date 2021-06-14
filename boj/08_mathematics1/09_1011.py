import math

t = int(input())

for i in range(t):
    x, y = map(int, input().split())
    dis = y - x
    count = 0

    num = math.floor(math.sqrt(dis))
    num_sq = num ** 2
    inc_num = math.sqrt(num_sq)

    if dis > num_sq + inc_num:
        count = 2 * num + 1
    elif dis > num_sq and dis <= num_sq + inc_num:
        count = 2 * num
    elif dis == num_sq:
        count = 2 * num - 1

    if dis < 4:
        count = dis

    print(count)
