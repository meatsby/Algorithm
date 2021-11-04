# 후보 추천하기
import sys
input = sys.stdin.readline

n = int(input())
students = int(input())
name = list(map(int, input().split()))

board = dict()

for i in range(students):
    if name[i] in board:
        board[name[i]][0] += 1
    else:
        if len(board) < n:
            board[name[i]] = [1, i]
        else:
            del_student = sorted(board.items(), key=lambda x:(x[1][0], x[1][1]))
            del_name = del_student[0][0]
            del(board[del_name])
            board[name[i]] = [1, i]

print(*sorted(board.keys()))

