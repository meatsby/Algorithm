# 12782.py '비트 우정지수' 와 유사

T = int(input())
for i in range(T):
    N = int(input())
    srt = input()
    end = input()
    cnt = abs(srt.count('B') - end.count('B'))
    dif = 0
    for i in range(N):
        if srt[i] != end[i]:
            dif += 1
    print((dif-cnt)//2 + cnt)
