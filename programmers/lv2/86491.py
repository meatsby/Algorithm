# Lv1 8주차_최소직사각형

def solution(sizes):
    for i in range(len(sizes)):
        sizes[i] = sorted(sizes[i])

    x, y = 0, 0

    for i in range(len(sizes)):
        x = max(x, sizes[i][0])
        y = max(y, sizes[i][1])

    return x * y
