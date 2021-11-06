def isEnd(answer, rows):
    isTrue = 0
    for a in answer:
        if 0 not in a:
            isTrue += 1
    if isTrue == rows:
        return True
    return False

def solution(rows, columns):
    answer = [[0]*columns for _ in range(rows)]
    x, y = 0, 0
    answer[x][y] = 1

    dx = [1, 0]
    dy = [0, 1]

    mx, mn = max(rows, columns), min(rows, columns)

    n = 0
    if mx%mn == 0 and rows > 2:
        n = mx*2 - 1

    t = 0
    while True:
        if n and n == t:
            break
        if not n and isEnd(answer, rows):
            break
        d = answer[x][y]%2
        nx = (x + dx[d])%rows
        ny = (y + dy[d])%columns
        answer[nx][ny] = answer[x][y] + 1
        x, y = nx, ny
        t += 1

    return answer