def solution(grid, clockwise):
    n = len(grid)
    l = n+(n-1)-1

    if clockwise == False:
        answer = [grid[-1][-1]]
        for i in range(n-3, -2, -1):
            ans = ""
            for j in range(n-1, i, -1):
                ans += grid[j][l-2:l]
            answer.append(ans[::-1])
            l -= 2

    elif clockwise == True:
        grid = [g[::-1] for g in grid]
        answer = [grid[-1][-1]]
        for i in range(n-3, -2, -1):
            ans = ""
            for j in range(n-1, i, -1):
                ans += grid[j][l-2:l]
            answer.append(ans[::-1])
            l -= 2
        answer = [a[::-1] for a in answer]

    return answer