# 빙고

import sys
input = sys.stdin.readline

def hor_cnt(bingo):
    bng_cnt = 0
    for b in bingo:
        bng = 0
        for i in b:
            if i.isdigit():
                bng = 0
                break
            else:
                bng += 1
        if bng != 0:
            bng_cnt += 1
    return bng_cnt

def ver_cnt(bingo):
    bng_cnt = 0
    for j in range(5):
        bng = 0
        for i in range(5):
            if bingo[i][j].isdigit():
                bng = 0
                break
            else:
                bng += 1
        if bng != 0:
            bng_cnt += 1
    return bng_cnt

def r_cnt(bingo):
    bng_cnt = 0
    r = [bingo[4][0], bingo[3][1], bingo[2][2], bingo[1][3], bingo[0][4]]
    for i in r:
        bng = 0
        if i.isdigit():
            bng = 0
            break
        else:
            bng += 1
    if bng != 0:
        bng_cnt += 1
    return bng_cnt

def l_cnt(bingo):
    bng_cnt = 0
    l = [bingo[0][0], bingo[1][1], bingo[2][2], bingo[3][3], bingo[4][4]]
    for i in l:
        bng = 0
        if i.isdigit():
            bng = 0
            break
        else:
            bng += 1
    if bng != 0:
        bng_cnt += 1
    return bng_cnt

bingo = [input().rstrip().split() for _ in range(5)]
nums = []

for _ in range(5):
    for i in input().rstrip().split():
        nums.append(i)

for n in range(25):
    for i in range(5):
        for j in range(5):
            if bingo[i][j] == nums[n]:
                bingo[i][j] = "O"
                break
    # for b in bingo:
    #     print(b)
    # print(n, "--------------------", hor_cnt(bingo), ver_cnt(bingo), r_cnt(bingo), l_cnt(bingo))
    ttl = hor_cnt(bingo) + ver_cnt(bingo) + r_cnt(bingo) + l_cnt(bingo)
    if ttl >= 3:
        print(n+1)
        break
