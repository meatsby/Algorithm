n = int(input())
dis = 1 # n번까지의 최단거리
cnt = 1 # 현재방
cnts = 6 # next level

while n > cnt:
    dis += 1
    cnt += cnts
    cnts += 6

print(dis)
